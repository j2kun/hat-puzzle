from collections import Counter
from itertools import product
from itertools import repeat


def strategy(i, n, other_hats):
    """ Choose a number between 1 and n by letting the other_hats vote
    and choosing the winner in place i, according to some fixed tie-breaking
    scheme.
    """
    tally = Counter(other_hats)
    outcome = list(sorted(list(range(n)), key=lambda i: (-tally[i], -i)))
    print("i={}, votes={}, outcome={}, choice={}".format(i, tally, outcome, outcome[i]))
    return outcome[i]


def without_index(L, i):
    return [x for (j, x) in enumerate(L) if j != i]


def try_all(n):
    all_hat_configurations = product(*repeat(list(range(n)), n))

    for configuration in all_hat_configurations:
        print("Trying %s" % (configuration,))
        hat_choices = list(strategy(i, n, without_index(configuration, i)) for i in range(n))
        print("hat_choices={}".format(hat_choices))

        hat_versus_choice = list(zip(configuration, hat_choices))
        if all(x != y for (x, y) in hat_versus_choice):
            raise Exception("Configuration {} fails: {}".format(configuration, hat_versus_choice))
