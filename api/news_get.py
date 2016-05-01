#coding:utf-8
import requests

def main():
    news = get_news()
    #check if it is error
    if not check_err():
        return {
        'error' : 1,
        'reason' : str(news.newsshowapi_res_error)
        }
    else:
        page = eval(str(eval(str(news['showapi_res_body']))['pagebean']))['currentPage']
        news = eval(str(eval(str(news['showapi_res_body']))['pagebean']))['contentlist']
        news = str(news).encode('utf-8')
        news = eval(news)
        news_No = 0
        news_list = []
        for news_content in news:
            news_No += 1
            news_list.append(news_content)
        return news_list

def check_err():
    news = get_news()
    if news["showapi_res_code"] == 0:
        return True
    else:
        return False

def get_news():
    url = 'http://apis.baidu.com/showapi_open_bus/channel_news/search_news'
    args = {'apikey':'8aefa7b16f762c8ee3f959387f520292'}
    news_text = requests.post(url, headers=args)
    return news_text.json()

if __name__ == '__main__':
    print(main())
