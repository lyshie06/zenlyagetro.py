from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
  return "iloveyousomuch my love")
@app.route("/about")
def about():
  return "this is my page"
@app.route("/contact")
def contact():
  return " this is for you"
if __name__ == "__main__":
  app.run()
  
