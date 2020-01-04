import random
import sys


class Bochonok:
    def __init__(self, amount):
        self.amount = amount
        self.gen = self.get_bochonok()

    # Достаем бочонки по 1 шт.
    def get_bochonok(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('Новый бочонок: {} (осталось {})'.format(y, self.amount - (i+1)))
            yield y


class Card:
    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.__set_card()

    # Делаем карточки
    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)
        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]
        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    # Поиск номера на карточке и определение победителя
    def search(self, card_player, num_cask):
        for i, n in enumerate(card_player):
            if num_cask in n:
                card_player[i][n.index(num_cask)] = '-'
                self.score += 1
                if self.score == 15:
                    print('{} Победила!'.format(self.name))
                    sys.exit(1)
                return True
        return False
