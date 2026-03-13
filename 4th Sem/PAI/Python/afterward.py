facts = ["fever", "cough"]
rules = [
    (["fever", "cough"], "flu"),
    (["flu"], "infection")
]
def forward_chaining(goal):
    inferred = facts.copy()

    
    added = True
    while added:
        added = False
        for condition, result in rules:
            if all(c in inferred for c in condition):
                
                if result not in inferred:
                    inferred.append(result)
                    added = True
                    
                    if result == goal:
                        return True
    return False
goal = input("Enter the goal to check: ")
if forward_chaining(goal):
    print("Goal", goal, "is achieved (True)")
else:
    print("Goal", goal, "cannot be achieved (False)")