import sqlite3

from flask import Flask, request, render_template_string, redirect, url_for
import os


application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

if ENV == 'dev':
    pass
    # ustawienia dla wersji developerskiej
else:
    pass
    # ustawienia dla wersji produkcyjnej


def init_db():
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

init_db()

BASE_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>CRUD w BigData z Pythonem!</title>
</head>
    <h1>Witaj, BigData z Pythonem!</h1>
    <p>Przykład CI/CD - automatyczne wdrożenie!</p>
    <p>Środowisko: <b>{{ ENV }}</b></p>
    <h2>Dodaj zadanie</h2>
    <form action="/add" method="post">
        <input type="text" name="title" placeholder="Tytuł zadania" required>
        <button type="submit">Dodaj</button>
    </form>
    <h2>Zadania</h2>
    <ul>
    {% for task in tasks %}
        <li>
        {% if task[2] == 1 %}
        <s>{{ task[1] }}</s>
        {% else %}
        {{ task[1] }}
        {% endif %}
        <a href="/complete/{{ task[0] }}">[Zakończ]</a>
        <a href="/delete/{{ task[0] }}">[Usuń]</a>
    {% endfor %}
</html>
'''





@application.route('/')
def index():
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute("SELECT id, title, completed FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template_string(BASE_HTML, tasks=tasks, ENV=ENV)

@application.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@application.route('/complete/<int:task_id>')
def complete(task_id):
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@application.route('/delete/<int:task_id>')
def delete(task_id):
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)