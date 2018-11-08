from collections import Counter
from itertools import product
from itertools import repeat


def voting_based_strategy(i, n, other_hats):
    """Choose a number between 1 and n by letting the other_hats vote
    and choosing the winner in place i, according to some fixed tie-breaking
    scheme.
    """
    tally = Counter(other_hats)
    outcome = list(sorted(list(range(n)), key=lambda i: (-tally[i], -i)))
    print("i={}, votes={}, outcome={}, choice={}".format(i, tally, outcome, outcome[i]))
    return outcome[i]


def without_index(L, i):
    return [x for (j, x) in enumerate(L) if j != i]


def try_all(n, strategy_chooser):
    """Run the hat puzzle for n people and n possible hats, with
    strategy_chooser(i) outputting a function (n, [int]) -> int that
    outputs player i's choice based on the (n-1)-length list of other hats.
    """
    all_hat_configurations = product(*repeat(list(range(n)), n))
    for configuration in all_hat_configurations:
        print("Trying %s" % (configuration,))
        hat_choices = list(
            strategy_chooser(i)(n, without_index(configuration, i))
            for i in range(n)
        )
        print("hat_choices={}".format(hat_choices))

        hat_versus_choice = list(zip(configuration, hat_choices))
        if all(x != y for (x, y) in hat_versus_choice):
            raise Exception("Configuration {} fails: {}".format(configuration, hat_versus_choice))


if __name__ == "__main__":
    def voting_strategy_chooser(i):
        return lambda n, other_hats: voting_based_strategy(i, n, other_hats)

    try_all(3, voting_strategy_chooser)
