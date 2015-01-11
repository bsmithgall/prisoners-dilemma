#!/usr/bin/env python

import random

def main(strategy_a, strategy_b, history):
    '''
    Always leads with cooperate, then cooperate if the
    opponent cooperated in the past round and in 25% of
    the opponent's defections.

    (see GTFT in http://plato.stanford.edu/entries/prisoner-dilemma/)
    '''

    opposition_strategy = 'strategy_b' if strategy_a == 'strategies.generous_tit_for_tat' else 'strategy_a'

    if len(history) == 0:
        return True
    else:
        return history[len(history) - 1][opposition_strategy] or random.random() < 0.25
