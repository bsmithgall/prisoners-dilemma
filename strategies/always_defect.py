#!/usr/bin/env python

from base import PrisonersDilemmaStrategy

class AlwaysDefect(PrisonersDilemmaStrategy):
    def main(self, foo, bar, baz):
        return False