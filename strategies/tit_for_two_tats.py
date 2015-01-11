#!/usr/bin/env python

def main(strategy_a, strategy_b, history):
    '''
    Always leads with cooperate, then cooperate if the
    opponent has cooperated in either of the past two rounds
    '''

    opposition_strategy = 'strategy_b' if strategy_a == 'strategies.tit_for_two_tats' else 'strategy_a'

    if len(history) == 0:
        return True
    else:
        return any([
            history[len(history) - 1][opposition_strategy], 
            history[len(history) - 2][opposition_strategy]
        ])