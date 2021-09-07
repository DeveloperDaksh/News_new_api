from newsapi import NewsApiClient

News = NewsApiClient(api_key='d7ea451af97842bcaaf40d479460dfb9')
top_headlines = News.get_top_headlines(sources='bbc-news')
print(top_headlines)
