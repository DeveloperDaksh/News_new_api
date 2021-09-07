from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from .models import SearchForm
import requests

# Create your views here.

# Search news articles by some specific search term

def topic(request):
    search_query = request.GET.get('search_term')
    if request.session.get('search_query') is None: 
        request.session['search_query'] = search_query
    url = settings.NEWS_API_BASE_URL
    url += "/everything?q="+request.session['search_query']+"&"
    url += str(timezone.datetime.now().date())+"&"
    url += "sortBy=relevancy&"
    url += "pageSize=100&apiKey=d7ea451af97842bcaaf40d479460dfb9"+settings.NEWS_API_KEY
    #print(timezone.datetime.now().date())
    article_list = requests.get(url)
    errorStatus = False
    if article_list.json()['status'] == 'error':
        errorStatus = True
    else:
        article_list = article_list.json()['articles']
    #print("Total Results = ",article_list.json()['totalResults'])
    #article_list = article_list.json()['articles']
    is_paginated = True
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    for article in articles:
        x = article['publishedAt']
        article['publishedAt'] = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%B %d %Y, %I:%M %p")

    return render(request, 'news/index.html', {'article_list':articles, 'status': errorStatus} )


def category(request):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    is_paginated = True
    paginate_by = 5

    selected_category = request.GET.get('c')
    if selected_category:
        if request.session.get('selected_category') is None or selected_category != request.session.get('selected_category'):
            request.session['selected_category'] = selected_category
    url = settings.NEWS_API_BASE_URL
    url += "/top-headlines?"
    url += "language=en&"
    url += "country=us&"
    if selected_category:
        url += "category="+request.session['selected_category']+"&"
    url += "apiKey=d7ea451af97842bcaaf40d479460dfb9"+settings.NEWS_API_KEY

    response = requests.get(url)
    articles = response.json()['articles']
    # pagination
    paginator = Paginator(articles, paginate_by)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    for article in article_list:
        x = article['publishedAt']
        article['publishedAt'] = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%B %d %Y, %I:%M %p")

    return render(request, template_name, {'article_list': article_list, 'selected_category': request.session['selected_category'].upper() })

def source(request):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    is_paginated = True
    paginate_by = 5
    
    selectedSource = request.GET.get('source')
    url = settings.NEWS_API_BASE_URL
    url += "/top-headlines?"
    url += "country=us&"

    print(selectedSource)
    if selectedSource:
        url += "source="+selectedSource+"&"
    
    url += "apiKey=d7ea451af97842bcaaf40d479460dfb9"+settings.NEWS_API_KEY
    print(url)
    response = requests.get(url)
    articles = response.json()['articles']
    # pagination
    paginator = Paginator(articles, paginate_by)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    
    for article in article_list:
        x = article['publishedAt']
        article['publishedAt'] = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%B %d %Y, %I:%M %p")

    return render(request, template_name, {'article_list': article_list})

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'article_list'
    is_paginated = True
    paginate_by = 5
    """
    News API usage.
    """
    #print(settings.NEWS_API_KEY)

    url = settings.NEWS_API_BASE_URL+"/top-headlines?country=us&apiKey=d7ea451af97842bcaaf40d479460dfb9"+settings.NEWS_API_KEY
    print(url)
    response = requests.get(url)
    #print("Total Results = ",response.json()['totalResults'])
    #print(response.json()['articles'])
    #print(response.json())
    
    def get_queryset(self):
        """Return the last five published questions."""
        articles = self.response.json()['articles']
        for article in articles:
            x = article['publishedAt']
            article['publishedAt'] = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime("%B %d %Y, %I:%M %p")
        return articles