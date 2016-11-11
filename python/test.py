def judge(moveA, moveB):
    if moveA == 'rock' and moveB == 'paper':
        return False
    if moveA == 'rock' and moveB == 'scissors':
        return True
    if moveA == 'paper' and moveB == 'rock':
        return True
    if moveA == 'paper' and moveB == 'scissors':
        return False
    if MoveA == 'scissors' and moveB == 'rock':
        return False
    if moveA == 'scissors' and moveB == 'paper':
        return True

print judge('rock','paper') # Expected: False
print judge('rock','scissors') # Expected: True
print judge('paper','rock') # Expected: True
print judge('paper','scissors') # Expected: False
print judge('scissors','rock') # Expected: False
print judge('scissors','paper') # Expected: True
