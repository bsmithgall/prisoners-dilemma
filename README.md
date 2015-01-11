### Prisoner's Dilemma Simulator

`main.py` contains a simulation engine that grabs two random strategies from the `strategies` module and simulates them an indetermine number of times (0.00346% chance of each round being the final round).

### Implementing New Strategies

To implement a new strategy, simply create a new file with the strategy name in the `strategies` module, import the base class `PrisonersDilemmaStrategy` from `strategies/base.py` and override the `main` method. The base class provides you with whether the strategy is the a strategy or the b strategy, and a property named `opposition_strategy`, which will give you the proper key for the key/value pairs in the history that is passed when the simulator runs the strategies against each other. For a simple example, look at `strategies/always_defect.py`, and for a more complex example, look at `strategies/joss.py`.