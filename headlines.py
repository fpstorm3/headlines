from flask import Flask, render_template, request
import html
import feedparser

app = Flask(__name__)

RSS_FEEDS = {'bbc':"https://feeds.bbci.co.uk/news/rss.xml",
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'reddit': 'http://www.reddit.com/r/python/.rss',
            'iol': 'http://www.iol.co.za/cmlink/1.640'}


# @app.route('/bbc')
# def bbc():
#     return get_news('bbc')

# @app.route('/cnn')
# def cnn():
#     return get_news('cnn')

# @app.route('/fox')
# def fox():
#     return get_news('fox')

# @app.route('/iol')
# def iol():
#     return get_news('iol')

# @app.route('/reddit')
# def reddit():
#     return get_news('reddit')

# to test --> http://localhost:5000/?publication=fox
@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication='bbc'
    else:
        publication= query.lower()
    feed  = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

# @app.route('/')
# @app.route('/<publication>')
# def get_news(publication="bbc"):
#     feed = feedparser.parse(RSS_FEEDS[publication])
#     return render_template("home.html", heading=feed.feed.title, articles=feed["entries"])

    # first_article = feed['entries'][0]
    # return render_template("home.html", headline=feed.feed.title, article=first_article)

    # return render_template("home.html",headline=feed.feed.title, title=first_article.get("title"), published=first_article.get("published"), summary=first_article.get("summary"))
    
    # return """
    #     <html>
    #         <body>
    #             <h1> {0} </h1>
    #             <b>{1}</b><br/>
    #             <i>{2}</i><br/>
    #             <p>{3}</p><br/>
    #         </body>
    #     </html>
    # """.format(feed.feed.title, first_article.get("title"), first_article.get("published"), first_article.get("description"))  # first_article.get("summary")

if __name__ == '__main__':
    app.run(port=5000, debug=True)