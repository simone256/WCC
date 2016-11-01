print("Begin Boolean operators")
print(1 == 2) # Expected output: False

print(1 > 2) # Expected output: False

print(2 > 1) # Expected output: True

print(1 >= 1) # Expected output: True

print(2 == 2) # Expected output: True

print(2 != 2) # Expected output: False

print("Begin Boolean operators using variable 'age'")
age = 30

print(age > 10) # Expected outcome: True

print(10 < age) # Expected outcome: True

print(age > 10 + 20) # Expected outcome: False

print(age + 20 > 10) # Expected outcome: True

print("Begin Comparing Strings")
print('a' > 'z') # Expected outcome: False

print('z' > 'a') # Expected outcome: True

print('apples' > 'oranges') # Expected outcome: False

print('oranges' > 'apples') # Expected outcome: True

print('cat' > 'car') # Expected outcome: True

print('car' > 'cat') # Expected outcome: False

print("Begin Logical operators")
age = -1
print(age > 12 and age < 19) # Expected outcome:

age = 10
print(age > 25 and age < 15) # Expected outcome:   False


print("Begin Rock, Paper, Scissors")
gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True

gesture = 'pape'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: false because gesture is "pape" not "paper"

print("Code test 1")
age = int(raw_input('How old are you? '))
print(age > 4 and age < 11)

age = int(raw_input('How old are you? '))
print(age >= 5 and age <= 10)

age = int(raw_input('How old are you? '))
print(age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10)
