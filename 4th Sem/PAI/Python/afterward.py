facts = ["A","B"]
rules ={
"C": ["A","B"],
"D": ["C"],
"E": ["D"]
}
def backward_chaining(goal):
    if goal in facts:
        return True
    if goal in rules:
        subgoals = rules[goal]
        for subgoal in subgoals:
            if not backward_chaining(subgoal):
                return False
        return True
    return False

goal = input ("Enter the goal:")
if backward_chaining(goal):
    print("Goal is achieved using Backward Chaining.")
else:
    print("Goal cannot be achieved.")