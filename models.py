import datetime
from peewee import *
from flask_admin.contrib.peewee import ModelView

db = SqliteDatabase('my_app.db',pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})
class BaseModel(Model):
    class Meta:
        database = db



class User(BaseModel):
    username = CharField(unique=True)
    join_date = DateTimeField()
    about_me = TextField()
    email = CharField(max_length=120)
    def __unicode__(self):
        return self.username
class UserInfo(BaseModel):
    key = CharField(max_length=64)
    value = CharField(max_length=64)
    user = ForeignKeyField(User)
    def __unicode__(self):
        return '%s - %s' % (self.key, self.value)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    body = TextField()
    send_date = DateTimeField(default=datetime.datetime.now)
class UserAdmin(ModelView):
    inline_models = (UserInfo,)
class PostAdmin(ModelView):
    # Visible columns in the list view
    #column_exclude_list = ['body']

    # List of columns that can be sorted. For 'user' column, use User.email as
    # a column.
    column_sortable_list = (('user', User.email), 'send_date')

    # Full text search
    column_searchable_list = (User.email,User.username)

    # Column filters
    column_filters = ('body',
                    'send_date',
                    User.username)

    form_ajax_refs = {
        'user': {
            'fields': (User.username, 'email')
        }
    }



# >>> print(some_message.user.username)
# Some User

# >>> for message in some_user.messages:
# ...     print(message.body)
# some message
# another message
# yet another message
db.create_tables((User,Tweet,Message,UserInfo))

# tweets = (Tweet
#         .select(Tweet, User)
#         .join(User)
#         .order_by(Tweet.created_date.desc()))
# for tweet in tweets:
#     print(tweet.user.username, tweet.message)
