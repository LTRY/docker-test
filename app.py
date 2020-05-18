from flask import Flask, request, jsonify, Response
import json
import mysql.connector

app = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='db', port='3306', password='root', database='dockertest')

@app.route('/')
def hello():
    return 'Docker-Flask-test'

@app.route('/api/test', methods=['GET'])
def sql_test():
    db = getMysqlConnection()
    cur = db.cursor()
    try:
        cur.execute('DROP TABLE tabletest;')
    except:
        pass
    cur.execute('CREATE TABLE tabletest (name VARCHAR(20));')
    cur.execute('INSERT INTO tabletest (name) VALUES (%(name)s);', {'name':'hello from sql'})
    cur.execute('SELECT * from tabletest;')
    rep = [name for name in cur][0]
    db.close()

    return rep

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
