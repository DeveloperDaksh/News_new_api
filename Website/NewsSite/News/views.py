from django.shortcuts import render
from datetime import datetime
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    sport_top_headlines = News.get_top_headlines(category='sports')
    sport_art=sport_top_headlines['articles']
    sport_title=[]
    sport_img=[]
    for article in range(len(sport_art)):
        f=sport_art[article]
        sport_title.append(f['title'])
        sport_img.append(f['urlToImage'])
    sport_src = zip(sport_title,sport_img)
    sport_data = list(sport_src)

    tech_top_headlines = News.get_top_headlines(category='technology')
    tech_art=tech_top_headlines['articles']
    tech_title=[]
    tech_img=[]
    for article in range(len(tech_art)):
        f=tech_art[article]
        tech_title.append(f['title'])
        tech_img.append(f['urlToImage'])
    tech_src = zip(tech_title,tech_img)
    tech_data = list(tech_src)

    bus_top_headlines = News.get_top_headlines(category='business')
    bus_art=bus_top_headlines['articles']
    bus_title=[]
    bus_img=[]
    for article in range(len(bus_art)):
        f=bus_art[article]
        bus_title.append(f['title'])
        bus_img.append(f['urlToImage'])
    bus_src = zip(bus_title,bus_img)
    bus_data = list(bus_src)

    enter_top_headlines = News.get_top_headlines(category='entertainment')
    enter_art=enter_top_headlines['articles']
    enter_title=[]
    enter_img=[]
    for article in range(len(enter_art)):
        f=enter_art[article]
        enter_title.append(f['title'])
        enter_img.append(f['urlToImage'])
    enter_src = zip(enter_title,enter_img)
    enter_data = list(enter_src)
    
    all_articles = News.get_everything(q='bitcoin',sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-09-04',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    arti=all_articles['articles']
    title=[]
    img=[]
    
    for article in range(len(arti)):
        f=arti[article]
        title.append(f['title'])
        img.append(f['urlToImage'])
    src = zip(title,img)
    source_data1 = list(src)
    return render(request, 'news/index.html',{'enter_data':enter_data[:4],'bus_data':bus_data[:4],'tech_data':tech_data[:4],'sport_data':sport_data[:4],'source_data1':source_data1[:9]})


def contact(request):
    return render(request, 'news/contact.html')

def source(request):
    
    selected_source = request.GET.get('source')
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    sources = News.get_sources()
    top_headlines = News.get_top_headlines(sources=selected_source)
    art=top_headlines['articles']
    src=sources['sources']
    title=[]
    img=[]
    sour=[]
    for article in range(len(art)):
        f=art[article]
        title.append(f['title'])
        img.append(f['urlToImage'])
    source_data = zip(title,img)
    for source in src:
        sour.append(source['name'])
    return render(request, 'news/sources.html',{'selected_source':selected_source,'source_data':source_data})
    

def source_singlenews(request):
    selected_title = request.GET.get('source_news')
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    top_headlines = News.get_top_headlines(sources='bbc-news,the-verge')
    art=top_headlines['articles']
    t=next(item for item in art if item['title'] == selected_title)
    title=t['title']
    author=t['author']
    desc=t['description']
    img=t['urlToImage']
    content=t['content']
    publish=t['publishedAt']

    all_articles = News.get_everything(q='bitcoin',sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-09-04',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='popularity',
                                      page=2)
    arti=all_articles['articles']
    title1=[]
    img1=[]
    
    for article in range(len(arti)):
        f=arti[article]
        title1.append(f['title'])
        img1.append(f['urlToImage'])
    src = zip(title1,img1)
    source_data1 = list(src)
    #publish = datetime.strptime(publish, '%Y-%m-%dT%H:%M:%SZ')
    return render(request, 'news/singlenews.html',{'title':title,'author':author,'description':desc,'image':img,'content':content,'publish':publish,'source_data1':source_data1[:3]})


def category(request):
        
    selected_category = request.GET.get('category')
    request.session['selected_category']= selected_category
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    sources = News.get_sources()
    top_headlines = News.get_top_headlines(category=selected_category)
    art=top_headlines['articles']
    title=[]
    img=[]
    for article in range(len(art)):
        f=art[article]
        title.append(f['title'])
        img.append(f['urlToImage'])
    source_data = zip(title,img)
    
    return render(request, 'news/category.html',{'selected_source':selected_category,'source_data':source_data})
    

def general(request):
    selected_general = request.GET.get('general')
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    all_articles = News.get_everything(q='bitcoin',sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-09-04',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='popularity',
                                      page=2)
    arti=all_articles['articles']
    title1=[]
    img1=[]
    for article in range(len(arti)):
        f=arti[article]
        title1.append(f['title'])
        img1.append(f['urlToImage'])
    src = zip(title1,img1)
    return render(request, 'news/general.html',{'selected_source':selected_general,'source_data':src})



def category_singlenews(request):
    selected_category = request.session['selected_category']
    selected_title = request.GET.get('category_news')
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    top_headlines = News.get_top_headlines(category=selected_category)
    art=top_headlines['articles']
    t=next(item for item in art if item['title'] == selected_title)
    title=t['title']
    author=t['author']
    desc=t['description']
    img=t['urlToImage']
    content=t['content']
    publish=t['publishedAt']

    all_articles = News.get_everything(q='bitcoin',sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-09-04',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='popularity',
                                      page=2)
    arti=all_articles['articles']
    title1=[]
    img1=[]
    
    for article in range(len(arti)):
        f=arti[article]
        title1.append(f['title'])
        img1.append(f['urlToImage'])
    src = zip(title1,img1)
    source_data1 = list(src)
    #publish = datetime.strptime(publish, '%Y-%m-%dT%H:%M:%SZ')
    return render(request, 'news/singlenews.html',{'title':title,'author':author,'description':desc,'image':img,'content':content,'publish':publish,'source_data1':source_data1[:3]})


def general_singlenews(request):
    selected_title = request.GET.get('news')
    News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
    all_articles = News.get_everything(q='bitcoin',sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-09-04',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='popularity',
                                      page=2)
    arti=all_articles['articles']
    t=next(item for item in arti if item['title'] == selected_title)
    title=t['title']
    author=t['author']
    desc=t['description']
    img=t['urlToImage']
    content=t['content']
    publish=t['publishedAt']
    title1=[]
    img1=[]
    
    for article in range(len(arti)):
        f=arti[article]
        title1.append(f['title'])
        img1.append(f['urlToImage'])
    src = zip(title1,img1)
    source_data1 = list(src)
    return render(request, 'news/singlenews.html',{'title':title,'author':author,'description':desc,'image':img,'content':content,'publish':publish,'source_data1':source_data1[:3]})