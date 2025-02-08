import random
def volume(radius):
    return float(((4*3.14159265359)/3)* (radius**3))

name = str(input('Hello! What is your name? '))
count = 0
our_num=random.randint(1,20)
print(f'Well, {name}, I am thinking of a number between 1 and 20. ', end = '\n')
while True:
    number = int(input('Take a guess.'))
    if number == our_num:
        print(f'Good job, {name}! You guessed my number in {count} guesses! ')
        break
    if number > our_num:
        print(f'Your guess is too high. ')
    if number < our_num:
        print(f'Your guess is too low. ')
    count+=1
answer = str(input('Do you want to know what whould be volume of sphere which radius is the same with this number? \n type YES or NO'))
if answer == 'YES':
    print(f'Volume of the sphere with radius {our_num} is {volume(our_num)} unit cube ')
else:
    print(f"I will say it anyway, it's {volume(our_num)} unit cube!) ")