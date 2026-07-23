import httpx 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def getdata():
    return render_template('users.html')
if __name__ == "_main_":
    app.run(debug=True)
