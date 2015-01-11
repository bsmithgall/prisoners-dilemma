#!/usr/bin/env python

import random
from base import PrisonersDilemmaStrategy

class Joss(PrisonersDilemmaStrategy):
    def main(self, strategy_a, strategy_b, history):
        '''
        Similar to TIT FOR TAT: lead with cooperation, and then
        do whatever the opponent did last round. However, also
        have a 10% chance of defecting instead of cooperating
        '''

        if len(history) == 0:
            return True
        else:
            strategy = history[len(history) - 1][self.opposition_strategy]

            if strategy is True and random.random() < 0.10:
                strategy = False

            return strategy