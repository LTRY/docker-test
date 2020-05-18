from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='db', port='3306', password='root', database='dockertest')

@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route('/api/test', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_months():
    db = getMysqlConnection()
    cur = db.cursor()
    try:
        cur.execute('CREATE TABLE tabletest (name VARCHAR(20));')
        cur.execute('INSERT INTO tabletest (name) VALUES (%(name)s);', {'name':'hello from sql'})
    except:
        pass
    
    cur.execute('SELECT * from tabletest;')
    rep = [name for name in cur][0]
    db.close()

    return rep

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
