import matplotlib.pyplot as plt
x = [5,2,8,3,130]
y = [25,36,9,49,121]
rt = []
for i in range(len(y)):
    rt.append(y[i]**0.5)
plt.plot(x,rt)
plt.xlabel("X")
plt.ylabel ("Y")
plt.show()