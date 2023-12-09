from boggle import Boggle
from flask import Flask, session, request, render_template, jsonify

app=Flask(__name__)
#originally had "fdfgkjtjkkg45yfdb"
app.config["SECRET_KEY"] = "mine"
#instantiate Boggle class; now have access to its attributes and methods
boggle_game = Boggle()

@app.route('/')
def set_up_board_etc():
#--call make_board method; returns a list with 5 sublists; each sublist has 5 random capital letters
    gameBoard = boggle_game.make_board()
#review
#--store newly made board in session; flask uses session object to store data that is supposed to persist across multiple requests
    session['gameBoard'] = gameBoard
#--retrieve users highscore from session; if none, default to 0
#when would new value be stored in key?  after finishing a game?
    highscore = session.get("highscore", 0)
#--retrieve number of times user has played; if none, default to zero
    nplays = session.get("nplays", 0)
#--call render_template function; function that combines template file with data to produce final html content that is sent to browser
#sned gameboard list to for loop in main.html
    return render_template('main.html', gameBoard=gameBoard,
#review
                            highscore=highscore, nplays=nplays)
#--methods['POST']?
@app.route('/handle_guess')
def handle_guess():
    """Check if the guess is in the dictionary"""
#--name for user input is 'inputValue'
    guess = request.args['inputValue']
#--assign stored dict/session info to gameBoard; will pass as argument in method call below
    gameBoard = session['gameBoard']
#method call on object instance 'boggle_game'; pass in gameboard info and user guess; checks the word submitted
    response = boggle_game.check_valid_word(gameBoard, guess)
#review
    return jsonify({'result': response})


#--at end of game; in js will update score and return message
@app.route('/gameover', methods=['POST'])
def score_and_times_played():
#--used to parse and retrieve data from incoming request
    response = request.json['score']
    nplays = session.get("nplays", 0)
    session[nplays] += 1
    return render_template('gameover.html', score=response)
#their code:
#   highscore = session.get("highscore", 0)
    # nplays = session.get("nplays", 0)
    # session['nplays'] = nplays + 1
    # session['highscore'] = max(score, highscore)
    #return jsonify(brokeRecord=score > highscore)
    



