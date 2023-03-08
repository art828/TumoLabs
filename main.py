import template1
import template2
import template3

print('''
Stories
1.About the hospital
2.About the hike
3.Letter from the enchanted forest

In which story 
do you want to insert 
words in the missing places?: 1, 2 or 3
''')
while True:
  choose_story = input("Write the story number: ")

  if choose_story == '1':
    template1.text_no1()
  elif choose_story == '2':
    template2.text_no2()
  elif choose_story == '3':
    template3.text_no3()
  else:
    print("There is no history with this number")