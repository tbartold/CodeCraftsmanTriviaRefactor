import trivia


from random import randrange, seed

not_a_winner = False

game = trivia.Game("questions.txt")

game.add('Chet')
game.add('Pat')
game.add('Sue')

def test_loading():
    assert len(game.pop_questions) == 50
    assert len(game.sports_questions) == 50
    assert len(game.science_questions) == 50
    assert len(game.rock_questions) == 50

    assert len(game.pop_answers) == 50
    assert len(game.sports_answers) == 50
    assert len(game.science_answers) == 50
    assert len(game.rock_answers) == 50

def test_give_wrong_answer():
    game.roll(1)
    assert game.get_question() == "Science Question 0"
    assert game.get_answer() == False
    assert game.points_earned_with_answer(True) == 0
    assert game.wrong_answer() == False
