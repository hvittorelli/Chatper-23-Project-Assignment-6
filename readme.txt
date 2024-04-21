Feature List:
    *Player can choose from a selection of magical options: Wand, Spellbook, Potion, Thestral, Phoenix.
    *Computer randomly selects a magical option.
    *Determine the winner based on the interactions between player and computer choices.
    *Display the outcome of each round.
    *Keep track of player and computer scores.
    *Display scores after each round.
    *Option to play again.
    *Include Harry Potter themed visuals and styling.
    *Introduce magical creatures with specific strengths and weaknesses.


Required Inputs/Outputs:
    *Inputs: Player choice (selected option via form), Session-based scores for the player and the computer.
    *Outputs: Outcome of each round (win, lose, tie), updated scores, visual representation of choices and outcome.

Outline of Functions:
  *initialize_scores():
    **Parameters: None
    **Return Value: None
    **Initializes the session scores for the player and the computer if not already initialized.
  *index():
    **Parameters: None
    **Return Value: Rendered template for the main page ('index.html') with session scores passed as context variables.
  *play():
    **Parameters: None
    **Return Value:
        ***Rendered template for the result page ('result.html') with game result and updated session scores passed as context variables.
        ***Error message if the request method is not allowed or if the player makes an invalid choice.
    **Functionality:
        ***Initializes scores.
        ***Randomly selects the computer's choice.
        ***Determines the winner based on player's choice and computer's choice.
Updates session scores accordingly.
  *determine_winner(player_choice, computer_choice):
    **Parameters:
      **player_choice: Choice made by the player.
      **computer_choice: Choice randomly selected for the computer.
    **Return Value: String indicating the game result.
    **Determines the winner based on the choices made by the player and the computer.
