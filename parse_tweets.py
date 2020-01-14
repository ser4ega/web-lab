from bs4 import BeautifulSoup
import requests

tweets=[]
for i in range(300):
    contents = requests.get('https://randomtextgenerator.com/')    
    soup = BeautifulSoup(contents.text, 'lxml')
    new=str(soup.find("textarea", id="generatedtext")).split('.')
    tweets.extend(new[1:len(new)-2:])
print(tweets)
f = open("data_txt/tweets.txt", "w",encoding='utf-8')
for tweet in tweets:
    tweet=tweet.replace('\n','')
    tweet=tweet.replace('\r','')
    f.write(tweet+"\n")
f.close()
