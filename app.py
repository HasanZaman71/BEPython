
from flask import Flask, redirect, url_for, render_template, request
import flask_sqlalchemy
import psycopg2
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('DATABASE_URL') or \
    'postgresql://postgres:1234@localhost:5432/postgres_db'  
    #  'sqlite:///' + os.path.join(basedir, 'app.db')
    
# Postgres db connection format: 'postgresql://username:password@hostname:port/dbname'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    complete = db.Column(db.Boolean, nullable=True)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete 
    
    



# data = {}
# count = 0


# conn = psycopg2.connect(
#     host= "localhost",
#     database= "beflask",
#     user= "postgres",
#     password= "1234"
# )

# cur = conn.cursor()

# @app.route('/get-db')
# def get_db():
#     cur.execute('SELECT version()')
#     db_version = cur.fetchone()
    
#     print(db_version)
#     #CLose the Cursor
#     cur.close()
#     return "True"



# class Todo:
#     def __init__(self, id, title):
#         self.id = id
#         self.title = title
#         self.complete = False


@app.route('/new-todo', methods=['POST'])
def new_todo():
    print(request.get_data)
    title = request.form['text-1655139979076']
    # global count
    # count = count + 1

    new_todo = Todo(title=title, complete=False)
    # data[todo.id] = todo

    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('show_todo'))


@app.route('/show-todo')
def show_todo():
    # return render_template('todo.html') 
    todo_list = Todo.query.all()

    return render_template('todo.html', todo_list = todo_list)
    

@app.route('/update/<int:todo_id>')
def update(todo_id):
    # todo = data[id]
    # todo.complete = True

    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()    

    return redirect(url_for('show_todo'))
 

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # todo = data[id]
    # todo.complete = True

    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()    

    return redirect(url_for('show_todo'))
 

# @app.route('/<name>')
# @app.route('/') 
# def index(name=None):
#     return render_template("index.html", my_name = name)

# @app.route('/home/<int:value>/<value2>')
# def home(value, value2): 
#     return f"Hello to home {value} {value2}" 
#     #return redirect(url_for('index'))


# @app.route('/new_value', methods = ['POST'])
# def new_value():
#     data = request.get_json()
#     data['body'] = "Hasan"
#     #return f"The key is title and value is {data['title']}"
#     print(data)
#     return data 

if __name__ == '__main__':
    app.run()

 