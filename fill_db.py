import datetime
from models import *
from peewee import *
from random import choice, random,randint
from datetime import datetime, timedelta

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]
def get_one_random_name(letters):
    return ''.join(choice(letters) for i in range(randint(5,8)))
def generate_random_email():
    return get_one_random_name(letters) + '@' + choice(domains)

def gen_datetime(min_year=2000, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random()

db = SqliteDatabase('my_app.db',pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})


Message.delete().execute()
Tweet.delete().execute()
User.delete().execute()
UserInfo.delete().execute()
f = open("data_txt/names.txt", "r")
usernames=f.read().splitlines()
n=len(usernames)
f.close()
for i in range (n):
    User.insert(
        {
            User.username:usernames.pop(randint(0,len(usernames)-1)),
            User.join_date:gen_datetime(),
            User.about_me:"",
            User.email:generate_random_email()
        }
    ).execute()

f = open("data_txt/messages.txt", "r")
messages=f.read().splitlines()
m=len(messages)
f.close()
for i in range (m):
    Message.insert(   
        {     
        Message.user: randint(1,n-1),
        Message.body: messages.pop(randint(0,len(messages)-1)),
        Message.send_date: gen_datetime()
        }
        
    ).execute()

f = open("data_txt/tweets.txt", "r")
tweets=f.read().splitlines()
t=len(tweets)
f.close()
for i in range (t):
    Tweet.insert(   
        {     
        Tweet.user: randint(1,n-1),
        Tweet.message: tweets.pop(randint(0,len(tweets)-1)),
        Tweet.created_date: gen_datetime(),
        Tweet.is_published: randint(0,1)
        }
        
    ).execute()
    

