# -*- coding: utf-8 -*-
"""hangman game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCUjHAKU6TLG5ab3V0PHNZmFF47c_oUh

# #**Hangman game using python **

---
"""

file = open("/content/words.txt","r")
texts= (file.read())
p=texts.split("\n")
print(p)

import random
words = p
sy = random.choice(words) # it will randomly give otput from the given list
#print(sy)
l = []
for i in sy:
  l.append("_")
#print(l)
lives =len(sy)
c = False
while not c:
  guess = input("Enter your guess:-")
  for j in range(len(sy)):
      if sy[j] == guess:
        l[j] = guess
  print(l)
  if guess not in sy:
    lives = lives -1
    if lives == 0:
        c = True
        print("you lose....!!")
        print("game over !!!")
        print(f"The word is:-{sy}")
  if "_" not in l:
    c= True
    print("you won")