import random

def text_no2():
    print('''
That is text.''')
    print('''
This weekend I am going camping with ( Proper Noun (Person’s Name)). 
I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. 
I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and (Verb2). 
I have heard that the (Color) lake is great for ( Verb (ending in ing) ). 
Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). 
If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! 
At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!
''')
    print('Insert words in the missing places.')
    name = input("Write the person's name: >")
    noun = input("Enter 2 nouns, split with spaces: > ")
    noun = noun.split(" ")
    random.shuffle(noun)
    adj_feeling = input("Enter 2 adjectives that are feelings and split with spaces: >")
    adj_feeling = adj_feeling.split()
    random.shuffle(adj_feeling)
    verb = input("Enter 2 verbs, split with spaces: >")
    verb = verb.split()
    random.shuffle(verb)
    verb_in_ing = input("Enter a verb that ends in -ing: >")
    animal = input("Writ name of animal: >")
    color = input("Enter color: >")
    adverb = input("Enter a adverb that ends in -ly: >")
    number = input(str("Enter number: >"))
    m_of_time = input("Enter measure of time: ")
    word = input('Enter the silly word: > ')
    print(f"""
This weekend I am going camping with {name}. 
I packed my lantern, sleeping bag, and {noun[0]}. I am so {adj_feeling[0]} to {verb[0]} in a tent. 
I am {adj_feeling[1]} we might see a(n) {animal}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {verb[1]}. 
I have heard that the {color} lake is great for {verb_in_ing}. 
Then we will {adverb} hike through the forest for {number} {m_of_time}. 
If I see a {color} {animal} while hiking, I am going to bring it home as a pet! 
At night we will tell {number} {word} stories and roast {noun[1]} around the campfire!!
    """)
