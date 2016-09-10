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
        not_a_winner = game.wrong_answer()
    else:
        not_a_winner = game.was_correctly_answered()

    if not not_a_winner: break
