import matplotlib.pyplot as plt 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Scatter Plot') 
x = [1, 2, 3, 7, 2, 9]
y = [2, 4, 1, 8, 2, 5] 
plt.plot(x, y, "or") 
plt.show()

# A LINE GRAPH BETWEEN TEMPERATURE AND DAY
import matplotlib.pyplot as plt

# gives a title to the Graph
plt.title('TEMPERATURE vs DAYS')

# naming the x-axis and y-axis
plt.xlabel('Day --->')
plt.ylabel('Temp --->')
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
plt.plot(a)
plt.plot(b)
c = list(range(0, 22, 3))
plt.plot(c)

plt.legend(["A", "B", "C"])

# set the interval by which the x-axis and y-axis set the marks
plt.xticks(list(range(0, 10)))
plt.yticks(list(range(0, 25, 3)))

# annotate command helps to write – on the graph any text xy denotes the position on the graph
plt.annotate('Temperature vs Days', xy = (1, 18))
plt.show()
