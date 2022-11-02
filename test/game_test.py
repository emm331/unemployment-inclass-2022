#
# if you want to setup your winner determination function to return a message about who won,
# use this test:
#

#from app.game import winner
#
#def test_winner():
#    tie_message = "It's a tie!"
#    win_message = "The user wins"
#    lose_message = "The computer wins"
#
#    assert winner(user_choice="rock", computer_choice="paper") == lose_message
#    assert winner(user_choice="rock", computer_choice="rock") == tie_message
#    assert winner(user_choice="rock", computer_choice="scissors") == win_message
#
#    assert winner(user_choice="paper", computer_choice="paper") == tie_message
#    assert winner(user_choice="paper", computer_choice="rock") == win_message
#    assert winner(user_choice="paper", computer_choice="scissors") == lose_message
#
#    assert winner(user_choice="scissors", computer_choice="paper") == win_message
#    assert winner(user_choice="scissors", computer_choice="rock") == lose_message
#    assert winner(user_choice="scissors", computer_choice="scissors") == tie_message

#
# if you want to setup your winner determination function to return the winning choice,
# use this test:
#

from app.game import determine_winner

def test_winning_choice():
    assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    assert determine_winner(user_choice="rock", computer_choice="rock") == None
    assert determine_winner(user_choice="rock", computer_choice="scissors") == "rock"

    assert determine_winner(user_choice="paper", computer_choice="paper") == None
    assert determine_winner(user_choice="paper", computer_choice="rock") == "paper"
    assert determine_winner(user_choice="paper", computer_choice="scissors") == "scissors"

    assert determine_winner(user_choice="scissors", computer_choice="paper") == "scissors"
    assert determine_winner(user_choice="scissors", computer_choice="rock") == "rock"
    assert determine_winner(user_choice="scissors", computer_choice="scissors") == None