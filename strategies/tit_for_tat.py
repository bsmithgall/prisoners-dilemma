#!/usr/bin/env python

def main(strategy_a, strategy_b, history):
    '''
    Always leads with cooperate, then do whatever the opponent
    did last round
    '''

    opposition_strategy = 'strategy_b' if strategy_a == 'strategies.tit_for_tat' else 'strategy_a'

    if len(history) == 0:
        return True
    else:
        return history[len(history) - 1][opposition_strategy]