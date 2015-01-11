#!/usr/bin/env python

import random

def main(strategy_a, strategy_b, history):
    '''
    Similar to TIT FOR TAT: lead with cooperation, and then
    do whatever the opponent did last round. However, also
    have a 10% chance of defecting instead of cooperating
    '''

    opposition_strategy = 'strategy_b' if strategy_a == 'strategies.joss' else 'strategy_a'

    if len(history) == 0:
        return True
    else:
        strategy = history[len(history) - 1][opposition_strategy]

        if strategy is True and random.random() < 0.10:
            strategy = False

        return strategy