#!/usr/bin/env python

from base import PrisonersDilemmaStrategy

class TitForTwoTats(PrisonersDilemmaStrategy):
    def main(self, strategy_a, strategy_b, history):
        '''
        Always leads with cooperate, then cooperate if the
        opponent has cooperated in either of the past two rounds
        '''

        if len(history) == 0:
            return True
        else:
            return any([
                history[len(history) - 1][self.opposition_strategy],
                history[len(history) - 2][self.opposition_strategy]
            ])
