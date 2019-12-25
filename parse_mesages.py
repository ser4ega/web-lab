from bs4 import BeautifulSoup
import requests

messages=[]
for i in range(300):
    contents = requests.get('https://randomtextgenerator.com/')    
    soup = BeautifulSoup(contents.text, 'lxml')
    new=str(soup.find("textarea", id="generatedtext")).split('.')
    messages.extend(new[1:len(new)-2:])
print(messages)
f = open("data_txt/messages.txt", "w",encoding='utf-8')
for message in messages:
    message=message.replace('\n','')
    message=message.replace('\r','')
    f.write(message+"\n")
f.close()
