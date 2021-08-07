import sqlite3
from sqlite3 import Error

from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb02820a3e94d72c9f950ee10ef7e3f7a35b3f5b'


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_list(data):
    matrix = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            row.append(data[i][j])
        matrix.append(row)
    return matrix


def execute_request(request1):
    connection = create_connection("data.sqlite")
    try:
        cursor = connection.cursor()
        cursor.execute(request1)
    except Error:
        return -1
    connection.commit()
    if cursor.description is None:
        return None
    headers = [description[0] for description in cursor.description]
    table = cursor.fetchall()
    cursor.close()
    return [headers, create_list(table)]


def get_page(r, number_page):
    res = []
    for i in range(10):
        if (number_page - 1) * 10 + i >= len(r):
            break
        res.append(r[(number_page - 1) * 10 + i])
    return res


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST' and not "to_main_button" in request.form:
        if not 'number_page' in session:
            session['number_page'] = 1
        if "request_button" in request.form:
            result = execute_request(request.form['data'])
            session['headers'] = result[0]
            session['data'] = result[1]

            if result == -1:
                return render_template('error.html')
            elif result is not None:
                return render_template('table.html', columns=result[0],
                                       items=get_page(result[1], session['number_page']),
                                       page=session['number_page'])
            else:
                return render_template('index.html')
        elif "back_button" in request.form:
            if session['number_page'] > 1:
                session['number_page'] -= 1
        elif "next_button" in request.form:
            coef = (session['number_page'] + 1) * 10 - len(session['data'])
            if coef <= 0 or (coef > 0 > (session['number_page'] + 1) * 10 - 9 - len(session['data'])):
                session['number_page'] += 1
        return render_template('table.html', columns=session['headers'],
                               items=get_page(session['data'], session['number_page']),
                               page=session['number_page'])
    return render_template('index.html')


app.run()
