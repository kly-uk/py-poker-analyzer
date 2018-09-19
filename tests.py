# /usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand


class TestCase(unittest.TestCase):
	# To test if player's hand is higher than opponent's
	def test_higher_hand(self):
		self.assertEqual(hand.compare_hand_with(opponent), 1)

	# To test if player has the highest hand
	def test_highest_hand_is_player(self):
		self.assertEqual(hand.find_highest_opp(opponent), 1)


def check_hand(currentHand):
	_count, used_cards = 0, [player]
	number = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
	suit = ["D", "C", "H", "S"]
	if len(currentHand.split()) == 5:
		for card in currentHand.split():
			if len(card) == 2:
				for u in number:
					for j in suit:
						if card[0] == u and j in card:
							_count += 1
	if len(opp) >= 1:
		used_cards += opp
	if currentHand != player:
		for card in currentHand.split():
			for index in used_cards:
				for usedcard in index.split():
					if card == usedcard:
						_count -= 1
	print(used_cards)
	print(opp)
	if _count == 5:
		_pass = "Valid"
	else:
		print("\nInvalid! Use the correct format e.g. 3D 4C 3S 5D TH\nAnd DON'T use the same cards!\n")
		_pass = "Invalid"
	return _pass


if __name__ == '__main__':
	opp, opponent, name = [], [], []
	check = "Invalid"
	NumberOfPlayers = ""
	while NumberOfPlayers.isdigit() is False:
		NumberOfPlayers = input("How many players are in your Poker game? Enter here: ")

	print("\nThe characteristics of the string of cards are:\n- A space is used as card seperator\n- Each card consists of two characters\n- The \
first character is the value of the card, valid characters are:\n\
	`2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `T`(en), `J`(ack), `Q`(ueen), `K`(ing), `A`(ce)\n\
- The second character represents the suit, valid characters are: `S`(pades), `H`(earts), `D`(iamonds), `C`(lubs)\n\n\
	For example... Queen of Hearts, Ten of Spades, and Nine of Diamonds = 'QH TS 9D'\n")

	while check != "Valid":
		player = input("Please enter the 5 cards in your hand: ")
		check = check_hand(player.upper())
		if check == "Valid":
			hand = PokerHand("Player", player.upper())
	for i in range(int(NumberOfPlayers) - 1):
		check = "Reset"
		name.append(input("Enter the next opponent's name: "))
		while check != "Valid":
			o = input(f"Enter {name[i]}'s hand: ")
			check = check_hand(o.upper())
			if check == "Valid":
				opp.append(o)

	for i, k in enumerate(opp):
		opponent.append(PokerHand(name[i], k.upper()))

	unittest.main()
