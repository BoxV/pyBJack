from Card import *
import random

Hand = []

def Hit ():
  Hand.append(Cards(random.randint(1, 13)))


print "Hi! This is a game of Black Jack."

Hit()
Hit()

total = 0
for card in Hand:
  print card.getName()
  total += card.getPoints()

#print "Your current total is: %d" % (total)
#print "If you would like to hit, type \"hit\"."
#print "If you would like to stand, type \"stand\"."
#choice = raw_input("").lower()

count = 2
for count in range(2, 11):
  
  if (total == 21):
    print "You win!1!"
    break

  elif (total > 21):
    print "You lose :((((("
    break

  else:

    print "If you would like to hit, type \"hit\"."
    print "If you would like to stand, type \"stand\"."
    choice = raw_input("").lower()

    if (choice == "hit"):
      Hit()
      total += Hand[count].getPoints()
      print Hand[count]
      print total

    elif (choice == "stand"):
      break


















