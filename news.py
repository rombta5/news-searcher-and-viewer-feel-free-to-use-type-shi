import requests
import time
from datetime import date
from newsapi import NewsApiClient
fileDict={}
responce=requests.get('https://newsapi.org/v2/everything')
print('welcome to the money-maker 3000!')
time.sleep(0.5)
today=date.today()
def newsSearcher():
    question1=input("what news do you want to search? ")
    question2=input('sort by (relevancy, popularity, publishedAt?) ') 
    newsapi = NewsApiClient(api_key='b31f1c87370e4563bb3f1a05be508b4b')
    responce=newsapi.get_everything(
        q=question1,
        sort_by=question2

    )
    articles=responce.get('articles',[])
    for i, article in enumerate(articles, start=1):
        print(f"Article {i}:")
        print(f"  Title: {article['title']}")           # Print the title
        print(f"  Author: {article.get('author', 'N/A')}")  # Print the author
        print(f"  Source: {article['source']['name']}") # Print the source name
        print(f"  URL: {article['url']}")              # Print the URL
        print(f"  Published At: {article['publishedAt']}")  # Print the publication date
        print("-"*40)
        fileDict.update({i: article['url']})
    ques3=input('would you like to view an article? ')
    if ques3=='yes' or ques3=='y':
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        from newspaper import Article
        from newspaper.article import ArticleException
        ques4str=input('number of article ')
        ques4=int(ques4str)
        articleUrl=fileDict.get(ques4)  
        response = requests.get(articleUrl, headers=headers)

        articleReal=Article(articleUrl)
        articleReal.set_html(response.text)
        articleReal.download()
        articleReal.parse()
        print (articleReal.text)
        newsSearcher()
    else:
        newsSearcher()
newsSearcher()
exit=input('input to exit ')
