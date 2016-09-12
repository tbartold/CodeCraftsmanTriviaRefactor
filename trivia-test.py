import trivia


from random import randrange, seed

not_a_winner = False

game = trivia.Game("questions.txt")

game.add('Chet')
game.add('Pat')
game.add('Sue')

seed(42)

while True:
    game.roll(randrange(5) + 1)

    if randrange(9) > 4:
        a_winner = game.answer(False)
    else:
        a_winner = game.answer(True)

    if a_winner: break
