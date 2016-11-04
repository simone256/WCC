

# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):
    if move == 'rock':
        return True #Make sure you capitalize these boolean outcomes
    elif move == 'paper':
        return True
    elif move == 'scissors':
        return True
    else:
        return False

print check_move('rock') # Expects: True
print check_move('paper') # Expects: True
print check_move('scissors') # Expects: True
print check_move('roc') # Expects: False
print check_move(1) # Expects: False
