from flask import redirect, render_template, request, url_for
from project import app, db, cache 
from project.model import Todo

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
 
@app.route('/')
def index():
    return 'Success'

@app.route('/set_cache/<country>/<capital>')
def set_cache(country, capital):

    cache.set(country, capital)
    return 'Success'

@app.route('/get_cache/<country>')
def get_cache(country):

    capital = cache.get(country)
    return capital if capital else 'No value'