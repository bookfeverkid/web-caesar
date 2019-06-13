from flask import Flask
from flask import request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/rotate" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0" />
            <textarea name="text"></textarea>
            <input type ="submit" />
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/rotate", methods=['POST'])
def rotate():
    rotate_by = request.form['rot']
    return '<h1> Hello ' + rotate_by + '</h1'

app.run()