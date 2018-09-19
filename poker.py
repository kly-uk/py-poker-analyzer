# /usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
from copy import deepcopy

class PokerHand:
	def __init__(self, name, hand):
		self.name = name
		self.hand = hand
		self.combo = {"title": "", "cards": ""}
		self.rank = 0
		self.analyse_hand()

	def compare_hand_with(self, opponent):
		higher_rank = 0
		print("TEST 1")
		for i in range(len(opponent)):
			print(self.hand + " ----- " + opponent[i].hand)
			if self.rank < opponent[i].rank:
				print(f" Player has HIGHER combo than {opponent[i].name}...\n.")
				if higher_rank != 2:
					higher_rank = 1
			elif self.rank == opponent[i].rank:
				print(f" Player has SAME combo as {opponent[i].name} !!\n. Analysing combo...")
				if higher_rank != 2:
					higher_rank = self.compare_same_combo_with(opponent[i])
				else:
					self.compare_same_combo_with(opponent[i])
			else:
				print(f" XXX {opponent[i].name} has HIGHER combo than Player...\n.")
				higher_rank = 2
		if higher_rank == 2:
			print("LOSE\n")
		elif higher_rank == 1:
			print("WIN\n")
		return higher_rank

	def compare_same_combo_with(self, opponent):
		value, opp_value, higher_combo = 0, 0, 0
		if self.rank == opponent.rank:
			for x in range(len(self.combo["cards"].split())):
				value += self.card_value(self.combo["cards"].split()[x])
				opp_value += opponent.card_value(opponent.combo["cards"].split()[x])
			print(f"... Player's hand has a value of: {value}\n... This Opponent's hand has a value of: {opp_value}\n")
			if value > opp_value:
				print("... Player has HIGHER '{0}' than {1}...\n.".format(self.combo["title"], opponent.name))
				higher_combo = 1
			elif value == opp_value:
				if self.rank == 9 or self.rank == 8:
					# KICKER CARD decides higher hand for Pairs, or Two Pairs
					last_card = self.get_kickercard()
					opp_last_card = opponent.get_kickercard()
					print(".. Kicker card: " + last_card)
					print(".. Kicker card for Opponent: " + opp_last_card)
					if self.card_value(last_card) > opponent.card_value(opp_last_card):
						print("... Player has HIGHER '{0}' than Opponent...\n.".format(self.combo["title"]))
						higher_combo = 1
					else:
						print("... LOSE | {0} has HIGHER '{1}' than Player...\n.".format(opponent.name, self.combo["title"]))
						higher_combo = 2
				else:
					print("... Player's hand has SAME value as {0}'s hand...\n.".format(opponent.name))
					return 0
			else:
				print("... LOSE | {0} has HIGHER '{1}' than Player...\n.".format(opponent.name, self.combo["title"]))
				higher_combo = 2
		return higher_combo

	def find_highest_opp(self, opponent):
		value, opp_values, opp_ranks, kicker_cards, winner, new_highest = 0, [], [], [], "", 0
		print("\nTEST 2")
		for x in range(len(self.combo["cards"].split())):
			value += self.card_value(self.combo["cards"].split()[x])
		for i in range(len(opponent)):
			opp_value = 0
			for y in opponent[i].combo["cards"].split():
				opp_value += opponent[i].card_value(y)
			opp_values.append(opp_value)
			opp_ranks.append(opponent[i].rank)
			kicker_cards.append(0)

		for q in range(len(opp_ranks)):
			if opp_ranks.count(min(opp_ranks)) == 1:
				if opponent[q].rank == min(opp_ranks):
					winner = opponent[q].name
			else:
				if opp_ranks[q] != min(opp_ranks):
					opp_values[q] = 0
		highest = max(opp_values)

		print("Player's hand is: " + self.combo["title"] + "\n")
		for e in range(len(opp_values)):
			print(opponent[e].name + "'s hand:    " + opponent[e].combo["title"])
			if opp_ranks.count(min(opp_ranks)) > 1:
				if opp_ranks[e] == min(opp_ranks):
					if opp_values.count(highest) == 1:
						if highest == opp_values[e]:
							winner = opponent[e].name
					elif opp_values.count(highest) > 1:
						if highest == opp_values[e]:
							if opponent[e].rank == 8 or opponent[e].rank == 9:
								print("Detecting multiple hands with same value !\nAnalysing combos...\n")
								kicker_cards[e] = opponent[e].card_value(opponent[e].get_kickercard())
								print(f"{opponent[e].name}'s kicker card is: {kicker_cards[e]}\n")
								if e == len(opp_values) - 1:
									new_highest = highest + max(kicker_cards)
									for j in range(len(kicker_cards)):
										if new_highest == (kicker_cards[j] + highest):
											winner = opponent[j].name
							else:
								winner += "(" + opponent[e].name + ")"

		print(winner + " has the highest hand out of your opponents\n")

		if self.rank < min(opp_ranks):
			winner = self.name
		elif self.rank == min(opp_ranks):
			if value > highest:
				winner = self.name
			elif value == highest:
				if self.rank == 9 or self.rank == 8:
					kicker_card = self.get_kickercard()
					if (self.card_value(kicker_card) + value) > new_highest:
						winner = self.name
				else:
					winner = winner + " and " + self.name
					print("TIE")
					print(f"The highest hand belongs to {winner}")
					return 0

		print(f"The highest hand belongs to {winner}")
		if winner == self.name:
			print("WIN")
			return 1
		else:
			print("LOSE")
			return 2

	def sort_cards(self):
		global items
		a = self.card_value(self.hand.split()[0])
		b = self.card_value(self.hand.split()[1])
		c = self.card_value(self.hand.split()[2])
		d = self.card_value(self.hand.split()[3])
		e = self.card_value(self.hand.split()[4])
		items = [a, b, c, d, e]
		result = ""
		for i in sorted(items):
			if i == items[0]:
				result = result + self.hand.split()[0] + " "
			elif i == items[1]:
				result = result + self.hand.split()[1] + " "
			elif i == items[2]:
				result = result + self.hand.split()[2] + " "
			elif i == items[3]:
				result = result + self.hand.split()[3] + " "
			elif i == items[4]:
				result = result + self.hand.split()[4] + " "

		return result.rstrip()

	def card_value(self, n):
		values = {}
		card_value = {
			"2": "1",
			"3": "2",
			"4": "3",
			"5": "4",
			"6": "5",
			"7": "6",
			"8": "7",
			"9": "8",
			"T": "9",
			"J": "10",
			"Q": "11",
			"K": "12",
			"A": "13"
		}
		suit_value = {"D": ".2", "C": ".4", "H": ".6", "S": ".8"}
		values.update({"num": card_value.get(n[0], "")})
		values.update({"suit": suit_value.get(n[1], "")})
		output = float(values["num"]) + float(values["suit"])
		return output

	def get_rank(self):
		ranking = {
			"Royal Flush": "1",
			"Straight Flush": "2",
			"Four of a kind": "3",
			"Full house": "4",
			"Flush": "5",
			"Straight": "6",
			"Three of a kind": "7",
			"Two pairs": "8",
			"Pair": "9",
			"High card": "10"
		}
		rank = ranking.get(self.combo["title"], "")
		return rank

	def get_kickercard(self):
		o = []
		p = self.hand
		for index in self.combo["cards"].split():
			p = p.replace(index, "")
		p = p.split()
		kicker_card = p[len(p) - 1]
		return kicker_card

	def analyse_hand(self):
		same_values, last_card = "", ""
		self.hand = self.sort_cards()
		print("\n %s's hand:  %s" % (self.name, self.hand))
		s = self.hand.split()
		n = sorted(items)
		for i in range(5):
			n[i] = floor(float(n[i]))
		k = deepcopy(n)

		# Pair/triple/Four of a kind
		for i, e in enumerate(k):
			if k[i] != "-":
				init_val = k[i]
				if k.count(k[i]) - 1 == 1:
					if self.combo["title"] == "Pair":
						self.combo["title"] = "Two pairs"
					elif self.combo["title"] == "Three of a kind":
						self.combo["title"] = "Full house"
					else:
						self.combo["title"] = "Pair"
					for j in range(len(k)):
						if k[j] == init_val:
							same_values += "{0} ".format(s[j])
							k[k.index(init_val)] = "-"
					self.combo["cards"] = same_values
				elif k.count(k[i]) - 1 == 2:
					if self.combo["title"] == "Pair":
						self.combo["title"] = "Full house"
					else:
						self.combo["title"] = "Three of a kind"
					for j in range(len(k)):
						if k[j] == init_val:
							same_values += "{0} ".format(s[j])
							k[k.index(init_val)] = "-"
					self.combo["cards"] = same_values
				elif k.count(k[i]) - 1 == 3:
					self.combo["title"] = "Four of a kind"
					for j in range(len(k)):
						if k[j] == init_val:
							k[k.index(init_val)] = "-"
					self.combo["cards"] = self.hand
			print(k)

		# Straight > Straight Flush > Royal Flush
		if n[0] + 1 == n[1] and n[1] + 1 == n[2] and n[2] + 1 == n[3] and n[3] + 1 == n[4]:
			if s[0][1] == s[1][1] and s[0][1] == s[2][1] and s[0][1] == s[3][1] and s[0][1] == s[4][1]:
				if s[0][0] == "T" and s[1][0] == "J" and s[2][0] == "Q" and s[3][0] == "K" and s[4][0] == "A":
					self.combo["title"] = "Royal Flush"
				else:
					self.combo["title"] = "Straight Flush"
			else:
				self.combo["title"] = "Straight"
			self.combo["cards"] = self.hand
		# Flush
		elif s[0][1] == s[1][1] and s[0][1] == s[2][1] and s[0][1] == s[3][1] and s[0][1] == s[4][1]:
			self.combo["title"] = "Flush"
			self.combo["cards"] = self.hand
		# High card
		if self.combo["title"] == "":
			self.combo["title"] = "High card"
			self.combo["cards"] = s[4]

		print(self.combo)
		self.rank = int(self.get_rank())
		print(f"Rank: {self.rank}\n")
