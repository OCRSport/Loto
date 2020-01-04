import sys
from old_loto.loto_classes import Bochonok, Card, Player


def main():
    game = Card(2)
    bochonok = Bochonok(90)
    player1 = Player('Ваша карточка')
    player2 = Player('Карточка компьютера')
    while True:
        num_bochonok = next(bochonok.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)

        inp_user = input('Зачеркнуть цифру? (y/n)')
        if inp_user == 'y':
            if player1.search(game.card_user, num_bochonok):
                continue
            else:
                print('Game Over')
                sys.exit(1)
        if inp_user == 'n':
            if player1.search(game.card_user, num_bochonok):
                print('Game Over')
                sys.exit(1)
            elif player2.search(game.card_comp, num_bochonok):
                continue
        if inp_user != 'n' and inp_user != 'y':
            print('Введите y or n')
            continue

main()