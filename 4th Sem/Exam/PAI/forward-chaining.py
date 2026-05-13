# Forward Chaining

facts = ["A", "B"]

rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

inferred = facts.copy()

changed = True

while changed:
    changed = False

    for condition, result in rules:

        if all(f in inferred for f in condition) and result not in inferred:
            inferred.append(result)
            changed = True

print("Inferred Facts:")
for fact in inferred:
    print(fact)