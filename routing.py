from flask import Flask
app = Flask(__name__)

@app.route ("/")
def error():
    return "If you are seeing this than something is wrong"

if __name__=="__main__":
    app.run(debug=True)