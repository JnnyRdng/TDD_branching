def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    length = len(scores) if len(scores) < 3 else 3
    return scores[:length]

def highest_to_lowest(scores):
    scores.sort(reverse=True)
    return scores