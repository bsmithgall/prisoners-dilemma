#!/usr/bin/env python

from base import PrisonersDilemmaStrategy

class TitForTat(PrisonersDilemmaStrategy):
    def main(self, strategy_a, strategy_b, history):
        '''
        Always leads with cooperate, then do whatever the opponent
        did last round
        '''

        if len(history) == 0:
            return True
        else:
            return history[len(history) - 1][self.opposition_strategy]
