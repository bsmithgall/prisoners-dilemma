#!/usr/bin/env python

import random

def main(foo, bar, baz):
    '''
    Randomly cooperates and defects
    '''
    if random.random() > 0.5:
        return True
    return False