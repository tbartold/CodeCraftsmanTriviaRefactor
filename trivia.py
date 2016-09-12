#!/usr/bin/env python

class Game:
    def __init__(self,filename):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.pop_answers = []
        self.science_answers = []
        self.sports_answers = []
        self.rock_answers = []

        self.current_player = -1
        self.is_getting_out_of_penalty_box = False

        self.read_in_questions(filename)


    def read_in_questions(self,filename):
        file = open(filename,"r")
        data = file.readlines()
        file.close()
        for line in data:
            words = line.strip("\n").split(",")
            #print words
            if words[0] == "Pop":
                self.pop_questions.append(words[1])
                self.pop_answers.append("True"==words[2])
            if words[0] == "Science":
                self.science_questions.append(words[1])
                self.science_answers.append("True"==words[2])
            if words[0] == "Sports":
                self.sports_questions.append(words[1])
                self.sports_answers.append("True"==words[2])
            if words[0] == "Rock":
                self.rock_questions.append(words[1])
                self.rock_answers.append("True"==words[2])

    #    for i in range(50):
    #        self.pop_questions.append("Pop Question %s" % i)
    #        self.science_questions.append("Science Question %s" % i)
    #        self.sports_questions.append("Sports Question %s" % i)
    #        self.rock_questions.append("Rock Question %s" % i)


    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        print player_name + " was added"
        print "They are player number %s" % len(self.players)
        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        self._increment_player()
        print "%s is the current player" % self.players[self.current_player]
        print "They have rolled a %s" % roll
        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True
                print "%s is getting out of the penalty box" % self.players[self.current_player]
                self._move(roll)
            else:
                print "%s is not getting out of the penalty box" % self.players[self.current_player]
                self.is_getting_out_of_penalty_box = False
        else:
            self._move(roll)

    def _move(self,roll):
        self._increment_location(roll)
        self._print_location()
        print "The category is %s" % self._current_category
        self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop':
            self._current_question = self.pop_questions.pop(0)
            self._current_answer = self.pop_answers.pop(0)
        if self._current_category == 'Science':
            self._current_question = self.science_questions.pop(0)
            self._current_answer = self.science_answers.pop(0)
        if self._current_category == 'Sports':
            self._current_question = self.sports_questions.pop(0)
            self._current_answer = self.sports_answers.pop(0)
        if self._current_category == 'Rock':
            self._current_question = self.rock_questions.pop(0)
            self._current_answer = self.rock_answers.pop(0)
        print self._current_question

    def get_question(self):
        return self._current_question;

    def get_answer(self):
        return self._current_answer;

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def points_earned_with_answer(self,answer):
        if answer == self.get_answer: return 1
        return 0

    def answer(self,reply):
        if reply: self.was_correctly_answered()
        else: self.wrong_answer()

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player] and not self.is_getting_out_of_penalty_box:
            return False
        print 'Answer was correct!!!!'
        self._increment_gold()
        self._print_gold()
        return self._did_player_win()

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print self.players[self.current_player] + " was sent to the penalty box"
        self.in_penalty_box[self.current_player] = True
        return False

    def _did_player_win(self):
        return (self.purses[self.current_player] == 6)

    def _increment_player(self):
        self.current_player += 1
        self.current_player = self.current_player % len(self.players)

    def _increment_location(self,roll):
        self.places[self.current_player] = (self.places[self.current_player] + roll) % 12

    def _increment_gold(self):
        self.purses[self.current_player] += 1

    def _print_location(self):
        print self.players[self.current_player] + \
            '\'s new location is ' + \
            str(self.places[self.current_player])

    def _print_gold(self):
        print self.players[self.current_player] + \
            ' now has ' + \
            str(self.purses[self.current_player]) + \
            ' Gold Coins.'
