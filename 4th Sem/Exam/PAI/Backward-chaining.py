# Backward Chaining

rules = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

facts = ["D", "E"]

def backward_chaining(goal):

    if goal in facts:
        return True

    if goal not in rules:
        return False

    subgoals = rules[goal]

    for g in subgoals:
        if not backward_chaining(g):
            return False

    return True

goal = "A"

if backward_chaining(goal):
    print(goal, "can be proved.")
else:
    print(goal, "cannot be proved.")