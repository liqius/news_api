#coding:utf-8
import flask, requests

app = flask.app(__name__)
try:
    import api.news_get

news = news_get.main()
if type(news) == dict:
    @app.route(/)
    def index():
        return '''ERROR'''
else:
    @app.route(/)
    def index():
        
