from flask import Flask, render_template, request, session
import random

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'


def initialize_scores():
  if 'player_score' not in session:
    session['player_score'] = 0
  if 'computer_score' not in session:
    session['computer_score'] = 0


@app.route('/')
def index():
  initialize_scores()  
  return render_template('index.html',
                         player_score=session['player_score'],
                         computer_score=session['computer_score'])


@app.route('/play', methods=['POST'])
def play():
  initialize_scores() 
  if request.method == 'POST':
    choices = ['Wand', 'Spellbook', 'Potion', 'Thestral', 'Phoenix']


    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    player_choice = request.form.get('choice')
    if player_choice not in choices:
      return "Invalid choice. Please select Wand, Spellbook, Potion, Thestral, or Phoenix.", 400  # Bad Request

    print(f"Player chose: {player_choice}")

    result = determine_winner(player_choice, computer_choice)

    print(f"Result: {result}")


    if result == "You win!":
      session['player_score'] += 1
    elif result == "Computer wins!":
      session['computer_score'] += 1

    return render_template('result.html',
                           player_choice=player_choice,
                           computer_choice=computer_choice,
                           result=result,
                           player_score=session['player_score'],
                           computer_score=session['computer_score'])
  else:
    return "Method Not Allowed", 405 


def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "It's a tie!"
  elif (player_choice == 'Wand' and computer_choice == 'Spellbook') or \
       (player_choice == 'Spellbook' and computer_choice == 'Potion') or \
       (player_choice == 'Potion' and computer_choice == 'Wand') or \
       (player_choice == 'Thestral' and (computer_choice == 'Wand' or computer_choice == 'Spellbook')) or \
       (player_choice == 'Phoenix' and (computer_choice == 'Potion' or computer_choice == 'Thestral')):
    return "You win!"
  else:
    return "Computer wins!"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
