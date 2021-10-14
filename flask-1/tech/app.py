from flask import Flask,render_template,request
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='836bbe1a307d471db9c49e10e7f6af1b')

# /v2/top-headlines

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',news='')


@app.route('/results/',methods=['POST'])
def get_results():
    keyword = request.form['keyword']
    top_headlines = newsapi.get_top_headlines(q=keyword,
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')
    data= top_headlines['articles']
    return render_template('index.html',news=data)


if __name__=="__main__":
    app.run()  