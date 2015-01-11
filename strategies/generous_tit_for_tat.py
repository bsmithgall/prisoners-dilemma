#!/usr/bin/env python

import random
from base import PrisonersDilemmaStrategy

class GenerousTitForTat(PrisonersDilemmaStrategy):
    def main(self, strategy_a, strategy_b, history):
        '''
        Always leads with cooperate, then cooperate if the
        opponent cooperated in the past round and in 25% of
        the opponent's defections.

        (see GTFT in http://plato.stanford.edu/entries/prisoner-dilemma/)
        '''

        if len(history) == 0:
            return True
        else:
            return history[len(history) - 1][self.opposition_strategy] or random.random() < 0.25
