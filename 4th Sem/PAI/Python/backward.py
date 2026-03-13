facts = {"fever", "cough"}

rules = {
    "flu": ["fever", "cough"],
    "infection": ["flu"]
}

def backward_chaining(goal):
    
    # If goal is already a known fact
    if goal in facts:
        return True
    
    # If goal has a rule
    if goal in rules:
        subgoals = rules[goal]
        
        for subgoal in subgoals:
            if not backward_chaining(subgoal):
                return False
        
        return True
    
    return False


# Main program
goal = input("Enter the goal to prove: ")

if backward_chaining(goal):
    print("Goal", goal, "is achieved (True)")
else:
    print("Goal", goal, "cannot be achieved (False)")