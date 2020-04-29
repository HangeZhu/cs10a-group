from flask import Flask, render_template, request
import crosswordapp
app = Flask(__name__)


global state
state = {'done':False,
         'Correct':0}


@app.route('/')
@app.route('/main')
def main():
    return render_template('crossword.html')

@app.route('/start')
def play():
    global state
    word=crossword.select()
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])


@app.route('/about')
def about():
    return render_template('teamprofile.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000,debug=True)
