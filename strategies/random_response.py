#!/usr/bin/env python

import random
from base import PrisonersDilemmaStrategy

class RandomResponse(PrisonersDilemmaStrategy):
    def main(self, foo, bar, baz):
        if random.random() > 0.5:
            return False
        return True
