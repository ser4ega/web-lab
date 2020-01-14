from flask import Flask, render_template, request
from flask_admin import Admin
import sqlite3
#from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from peewee import SqliteDatabase
from models import User, UserAdmin, PostAdmin, Message

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:my_app.db'
app.config['SECRET_KEY'] = '123456790'

db = SqliteDatabase('my_app.db',pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})


# Flask and Flask-SQLAlchemy initialization here

#admin.add_view(ModelView(Post, db.session))

@app.route("/")
@app.route("/index")
def index():    
    return render_template(
        "index.html"
    )
# def index():
#     user = { 'username': 'terri' } # выдуманный пользователь
#     posts = [ # список выдуманных постов
#         { 

#             'author': { 'username': 'John' }, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': { 'username': 'Susan' }, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
#     return render_template("index.html",
#         title = 'Home',
#         user = user,
#         posts = posts)
#########################################################
# @app.route('/ajax/delete/<name>')
# def ajax_delete(name):
#     con = sqlite3.connect("tmp.db")
#     cur = con.cursor()
#     sql = "DELETE FROM tmp WHERE name=?"
#     cur.execute(sql, (name,))
#     con.commit()
#     return "OK"
# @app.route("/ajax/data/")
# @app.route("/ajax/data/<int:offset>")
# def ajax_rows(offset=0):
#     limit = request.args.get("limit", 10)
#     con = sqlite3.connect("tmp.db")
#     cur = con.cursor()
#     sql = "SELECT name, quantity FROM tmp ORDER BY quantity LIMIT ? OFFSET ?"
#     cur.execute(sql, (limit, offset))
#     res = cur.fetchall()
#     return render_template("ajax_table.html", rows=res)
# @app.route("/ajax/")
# def ajax_table():
#     return render_template("ajax.html")
# @app.route("/")
# @app.route("/<int:offset>")
# def index(offset=0):
#     limit = request.args.get("limit", 10)
#     con = sqlite3.connect("tmp.db")
#     cur = con.cursor()
#     sql = "SELECT name, quantity FROM tmp ORDER BY quantity LIMIT ? OFFSET ?"
#     cur.execute(sql, (limit, offset))
#     res = cur.fetchall()
#     return render_template(
#         "index.html",
#         rows=res,
#         offset_after=offset + 10,
#         offset_before=offset - 10 if offset > 10 else 0,
#     )
if __name__ == "__main__":
    admin = Admin(app, name='main', template_mode='bootstrap3')
    admin.add_view(UserAdmin(User))
    admin.add_view(PostAdmin(Message))
    app.debug = True
    app.run()
