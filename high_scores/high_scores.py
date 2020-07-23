def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    return scores[-3:]

def highest_to_lowest(scores):
    scores.sort()
    return scores