from flask import Flask, render_template

#create instance of flask class
app = Flask(__name__) #placeholder for current module


@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
