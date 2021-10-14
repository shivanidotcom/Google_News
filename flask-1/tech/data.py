from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='836bbe1a307d471db9c49e10e7f6af1b')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')
print(top_headlines['articles'])

data= top_headlines['articles']

for post in data:
    print(post['title'])
    print('')
    print(post['publishedAt'])
    print('')
    print(post['description'])