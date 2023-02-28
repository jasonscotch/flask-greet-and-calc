"""Simple Greet Flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Show homepage"""
    
    return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """

@app.route('/welcome')
def welcome():
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def welcome_home():
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcome_back():
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html