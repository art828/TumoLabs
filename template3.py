import random

def text_no3():
    print('''
That is text.''')
    print("""
Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. 
I found myself here one day after going for a ride on a (Color) (Animal) in (Place). 
There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! 
In the ( Room in a House) there is a pool full of (Noun). 
I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). 
It feels as though I have lived here for (Number) ( Measure of time). 
I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!
    """)
    print('Insert words in the missing places.')
    name = input("Write the person's name: >")
    adjectives = input("Enter 5 adjectives, split with spaces: > ")
    adjectives = adjectives.split(" ")
    random.shuffle(adjectives)
    color = input("Enter color: >")
    animal = input("Writ name of animal: >")
    place = input("Enter name of place: >")
    m_creature = input("Enter 2 manes of magical creatures in the plural: >")
    m_creature = m_creature.split()
    random.shuffle(m_creature)
    room = input("Enter the name of one of the rooms in the house: >")
    noun = input("Enter 5 noun, split with spaces: > ")
    noun = noun.split(" ")
    random.shuffle(noun)
    number = input(str("Enter number: >"))
    measure_of_time = input("Enter measure of time: ")
    verb_in_ing = input("Enter a verb that ends in -ing: >")
    print(f"""
Dear {name}, I am writing to you from a {adjectives[0]} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {color} {animal} in {place}. 
There are {adjectives[1]} {m_creature[0]} and {adjectives[2]} {m_creature[1]} here! 
In the {room} there is a pool full of {noun[0]}. 
I fall asleep each night on a {noun[1]} of {noun[2] + "s"} and dream of {adjectives[3]} {noun[3] + "s"}. 
It feels as though I have lived here for {number} {measure_of_time}. 
I hope one day you can visit, although the only way to get here now is {verb_in_ing} on a {adjectives[4]} {noun[4]}!!""")