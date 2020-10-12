from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Successfully Deployed Flask App to server"

if __name__=='__main__':
    app.run()