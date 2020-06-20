from django.shortcuts import render,HttpResponse,redirect
from article.models import ArticlePost,Category
from article.forms import ArticlePostForm
from comment.forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
import markdown
from comment.models import Comment
# Create your views here.

def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    tag = request.GET.get('tag')
    article_list = ArticlePost.objects.all()
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |Q(content__icontains=search)| Q(category__name__icontains=search))
    else:
        search = ''
    if tag and tag!= 'None':
        article_list = article_list.filter(tags__name__in=[tag])
    if order == 'total_views':#比较与默认最热的参数是否相同
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request,'article/list.html',{'articles':articles,'order':order,'search':search,'tag':tag})

def article_detail(request,id):
    article = ArticlePost.objects.get(id=id)
    article.total_views += 1
    article.save(update_fields=['total_views'])#指定只更新total_views
    comments = Comment.objects.filter(article=id)
    comments_form = CommentForm()#评论form表单
    # 将markdown语法渲染成html样式
    md = markdown.Markdown(
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    article.content = md.convert(article.content)
    return render(request, 'article/detail.html', {'article': article,'toc':md.toc, 'comments': comments,'comment_form':comments_form})

@login_required(login_url='/user/login/')
def article_create(request):
    categorys = Category.objects.all()
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST,request.FILES)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['category'] != 'none':
                new_article.category = Category.objects.get(id=request.POST['category'])
            new_article.save()
            article_post_form.save_m2m()
            return redirect("article:article_list")
        else:
            return render(request, 'article/create.html',{ 'categorys':categorys})
    else:
        return render(request, 'article/create.html',{ 'categorys':categorys})

@login_required(login_url='/user/login/')
def article_delete(request,id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:article_list')

@login_required(login_url='/user/login/')
def article_update(request, id):
    categorys = Category.objects.all()
    article = ArticlePost.objects.get(id=id)
    if request.method == "POST":
        article_post_form = ArticlePostForm(request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.save()
            return redirect("article:article_detail", id=id)
    else:
        article_post_form = ArticlePostForm()
        return render(request, 'article/update.html',{ 'article': article, 'article_post_form': article_post_form,'categorys':categorys})

def archive(request, year, month):#归档标签
    post_list = ArticlePost.objects.filter(created__year=year,created__month=month).order_by('-created')#
    return render(request, 'sidebar/archives_index.html', {'post_list': post_list})

def category(request,id):#分类标签
    category = ArticlePost.objects.filter(category_id=id)
    return  render(request,'sidebar/category_index.html',{'category':category})

def about(request):
    if request.method =='GET':
        return render(request,'about.html')