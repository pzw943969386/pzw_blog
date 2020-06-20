from django import template
from article.models import ArticlePost,Category
from django.db.models.aggregates import Count
register = template.Library()

@register.inclusion_tag('sidebar/archives.html')
def show_archives():
    date_list = ArticlePost.objects.dates('created', 'month', order='DESC')
    return {
        'date_list': date_list
    }

@register.inclusion_tag('sidebar/category.html')
def show_categories():
    category_list = Category.objects.annotate(num_posts=Count('articlepost')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }

@register.inclusion_tag('sidebar/recent_article.html')
def show_recent_article():
    recent_article_list = ArticlePost.objects.all().order_by('-created')[:5]
    return {
        'recent_article_list': recent_article_list

    }

@register.inclusion_tag('sidebar/hot_article.html')
def show_hot_article():
    hot_article_list = ArticlePost.objects.all().order_by('-total_views')[:5]
    return {'hot_article_list':hot_article_list}