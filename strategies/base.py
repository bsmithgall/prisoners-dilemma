#!/usr/bin/env python

class PrisonersDilemmaStrategy:
    def __init__(self, a):
        '''
        Initializes as either the A or B strategy
        '''
        self.a = a
        self.opposition_strategy = 'strategy_b' if a else 'strategy_a'

    def main(self):
        raise NotImplementedError