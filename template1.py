import random

def text_no1():
    print('''
That is text.''')
    print('''
It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). 
The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). 
If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). 
Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast.
The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !
    ''')
    print('Insert words in the missing places.')
    numbers = input(str("Enter 3 numbers, split with spaces: > "))
    numbers = numbers.split()
    random.shuffle(numbers)
    measure_of_time = input("Enter measure of time: ")
    mode_of_tr = input('Enter mode of transportation: > ')
    adjectives = input("Enter 3 adjectives, split with spaces: > ")
    adjectives = adjectives.split(" ")
    random.shuffle(adjectives)
    color = input('Enter color: > ')
    p_of_the_b = input("Enter 2 part of the body, split with spaces: > ")
    p_of_the_b = p_of_the_b.split(" ")
    random.shuffle(p_of_the_b)
    noun = input("Enter 3 nouns, split with spaces: > ")
    noun = noun.split(" ")
    random.shuffle(noun)
    verb = input('Enter verb: > ')
    word = input('Enter the silly word: > ')
    print(f"""
It was about {numbers[0]} {measure_of_time} ago when I arrived at the hospital in a {mode_of_tr}.
The hospital is a {adjectives[0]} place, there are a lot of {adjectives[1]} {noun[0]} here. There are nurses here who have {color} {p_of_the_b[0]}.
If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {numbers[1]} {noun[1]}.
Today I talked to a doctor and they were wearing a {numbers[2]} on their {p_of_the_b[1]}.
I heard that all doctors {verb} {noun[2]} every day for breakfast. The most {adjectives[2]} thing about being in the hospital is the {word} {noun[0]} !""")

