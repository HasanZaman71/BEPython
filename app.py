from flask import Flask, redirect, url_for, render_template, request
#import psycopg2


app = Flask(__name__)

data = {}
count = 0

class Todo:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.complete = False


@app.route('/new-todo', methods=['POST'])
def new_todo():
    title = request.form['title']
    global count
    count = count + 1
    todo = Todo(count, title)
    data[todo.id] = todo
    return "Success"

@app.route('/show-todo')
def show_todo():
    return render_template('todo.html', todo_list = data)

@app.route('/<name>')
@app.route('/') 
def index(name=None):
    return render_template("index.html", my_name = name)

@app.route('/home/<int:value>/<value2>')
def home(value, value2): 
    return f"Hello to home {value} {value2}" 
    #return redirect(url_for('index'))


@app.route('/new_value', methods = ['POST'])
def new_value():
    data = request.get_json()
    data['body'] = "Hasan"
    #return f"The key is title and value is {data['title']}"
    print(data)
    return data 

if __name__ == '__main__':
    app.run()

 