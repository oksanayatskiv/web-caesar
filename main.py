from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']= True

form = """
        <!DOCTYPE html>

        <html>
            <head>
                <style>
                    form {{
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }}
                    textarea {{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>
            <body>
            <!-- create your form here -->
                <form method="POST">
                    <label for = "rot">Rotate by:</label>
                    <input type = "text" id = "rot" value= 0 name = "rot"/>
                    <textarea name="text" id = "text ">{0}</textarea> 
                    <input type="submit"/>
                </form>
            </body>
        </html>
        """

@app.route("/")
def index():
   return form.format()


#@app.route('/encrypt', methods=['POST'])
@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    text = request.form['text']
    rotated_text = rotate_string (text, rotation)
    #return '<h1>' + rotated_text +'</h1>'
    return form.format(rotated_text)
app.run()
