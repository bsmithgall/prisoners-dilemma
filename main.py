#!/usr/bin/env python

import pkgutil
import strategies
from strategies.base import PrisonersDilemmaStrategy
import random

class PrisonersDilemma:
    '''
    Tracks historical performance, and allows different strategies
    to compete with one another. Individual strategies should
    return True if they plan to cooperate and False if they plan to
    defect. Individual strategies can be implemented in strategies module.
    '''
    def __init__(self, strategy_a=None, strategy_b=None):

        generated_strategies = self.select_strategies()

        strategy_a_class = self.get_subclass(generated_strategies[0], PrisonersDilemmaStrategy)
        strategy_b_class = self.get_subclass(generated_strategies[1], PrisonersDilemmaStrategy)

        self.strategy_a = strategy_a_class(True)
        self.strategy_b = strategy_b_class(False)

        self.end_probability = 0.00346

        # history is a list of dictionaries. each element in
        # the list is a dictionary which contains the the a response,
        # b response, and scores for that round
        self.history = []

    def select_strategies(self):
        '''
        Takes all strategies from the strategies module and randomly
        selects two (with replacement)
        '''
        all_strategies = [i[1] for i in pkgutil.iter_modules(strategies.__path__, 'strategies.')]
        all_strategies.remove('strategies.base')
        all_strategies.remove('strategies.downing') # TODO: implement DOWNING

        # dummy fromlist allows direct import of strategies
        strategy_a = __import__(all_strategies[random.randint(0, len(all_strategies) - 1)], fromlist='dummy')
        strategy_b = __import__(all_strategies[random.randint(0, len(all_strategies) - 1)], fromlist='dummy')

        return strategy_a, strategy_b

    def get_subclass(self, module, base_class):
        '''
        Extract the subclass that will actually be excecuting
        the strategy
        '''
        for name in dir(module):
            obj = getattr(module, name)
            try:
                if issubclass(obj, base_class) and not obj is base_class:
                    return obj
            except TypeError:  # If 'obj' is not a class
                pass
        return None

    def calculate_result_points(self, a_result, b_result):
        if a_result and b_result:
            return 3, 3
        if not a_result and not b_result:
            return 1, 1
        if a_result and not b_result:
            return 0, 5
        if b_result and not a_result:
            return 5, 0

    def play_round(self):
        '''
        All strategies must implement a main() method that takes in the names
        of the two strategies and the history of the performance so far. An
        incorrectly implemented strategy will raise an Exception.
        '''
        try:

            strategy_a_result = self.strategy_a.main(self.strategy_a, self.strategy_b, self.history)
            strategy_b_result = self.strategy_b.main(self.strategy_a, self.strategy_b, self.history)
            a_points, b_points = self.calculate_result_points(strategy_a_result, strategy_b_result)

            self.history.append({
                'strategy_a': strategy_a_result,
                'strategy_b': strategy_b_result,
                'strategy_a_points': a_points,
                'strategy_b_points': b_points
            })

        except AttributeError, NotImplementedError as detail:
            raise Exception("Could not play this round: " + detail.message)

    def report_stats(self):
        num_rounds = len(self.history)
        strategy_a_score = sum(i['strategy_a_points'] for i in self.history)
        strategy_b_score = sum(i['strategy_b_points'] for i in self.history)

        print '''
        Through {num_rounds} rounds, {a} scored {a_points} and {b} scored {b_points}. 
        The total points scored this round is {total}. An optimal game would have had {optimal} points.
        These two strategies combined for {percent:.2%} of the optimal points.
        '''.format(
            num_rounds=num_rounds, a=self.strategy_a.__module__, b=self.strategy_b.__module__,
            a_points=strategy_a_score, b_points=strategy_b_score,
            optimal=num_rounds * 6, total=strategy_a_score + strategy_b_score,
            percent=(strategy_a_score + strategy_b_score)/(num_rounds * 6.)
        )

def main():
    game = PrisonersDilemma()
    while True:
        if random.random() <= game.end_probability:
            game.report_stats()
            return
        else:
            game.play_round()

if __name__ == '__main__':
    main()