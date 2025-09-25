import matplotlib.pyplot as plt
labels = ["TAMIL", "ENGLISH", "MATHS", "PHYSICS", "CHEMISTRY", "CS"]
usage = [79.8, 67.3, 77.8, 68.4, 70.2, 88.5]
sq = []
y_positions = range (len(labels))
'''for i in range(len(usage)):
    sq.append(pow(usage[i],2))'''
plt.bar (y_positions, sq)
plt.xticks (y_positions, labels)
plt.ylabel ("RANGE")
plt.title ("MARKS")
plt.show()