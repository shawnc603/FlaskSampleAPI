from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

def hello_world2():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug='true')