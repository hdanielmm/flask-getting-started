from flask import Flask, render_template
from model import db

app = Flask(__name__)


@app.route('/')
def welcome():
    message = ''
    other_message = ''
    context = {
        "message": "Here's a message from the view",
        "other_message": "Other message"
    }
    return render_template("welcome.html", **context)

@app.route('/card')
def card_view():
    card = db[0]
    
    context = {
        "question": card['question'],
        "answer": card['answer']
    }
    
    return render_template("card.html", **context)



# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8000, debug=True)
 