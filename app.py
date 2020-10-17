import os
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
hostname = os.uname()[1]
print(hostname)
@app.route('/')
def todo():
    return "<HTML><BODY><H1>HELLO - I am from <i style=\"color:red\">"+hostname+"</i></H1></BODY></HTML>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
