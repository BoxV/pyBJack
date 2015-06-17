from Card import *
import random

#start 2 random num, 1-10 
#
#

print "Hi! This is a game of Black Jack."

Hand = []

Hand.append(Cards(random.randint(1, 13)))
Hand.append(Cards(random.randint(1, 13)))

total = 0
for card in Hand:
	print card.getName()
	total += card.getPoints()

print "Your current total is: %d" % (total)
print "If you would like to hit, type \"hit\"."
print "If you would like to stand, type \"stand\"."
choice = raw_input("").lower()

if (choice == "hit"):
	add = Hand.append(Cards(random.randint(1, 13)))
	total += add
	print total