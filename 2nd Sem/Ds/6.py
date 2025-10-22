import matplotlib.pyplot as plt
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter plot')
x=[1,2,3,7,2,9]
y=[2,4,1,8,2,5]
plt.plot(x,y,"or")
plt.show()

plt.title("Temperature vs Days")
plt.xlabel("Day --->")
plt.ylabel("Temp --->")

a = [1, 2, 3, 4, 5]
b = [0.06, 0.2, 15, 10, 8, 16, 21]
c = list(range(0, 22, 3))

plt.plot(a, label="A")
plt.plot(b, label="B")
plt.plot(c, label="C")

plt.legend()
plt.xticks(list(range(0, 20)))
plt.yticks(list(range(0, 25, 2)))

plt.annotate("Temperature vs Days", xy=(1, 12))
plt.show()

import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0.06, 0.2, 0.15, 10, 0.8, 16, 21]
c = [1, 2, 6, 8, 3, 20, 13, 15]

fig = plt.figure(figsize=(10, 10))

# 1st subplot
sub1 = plt.subplot(2, 2, 1)
sub1.plot(a, 'o-')
sub1.set_title("1st Rep")

# 2nd subplot
sub2 = plt.subplot(2, 2, 2)
sub2.plot(b, 's-')
sub2.set_xticks(list(range(0, 10, 1)))
sub2.set_title("2nd Rep")

# 3rd subplot
sub3 = plt.subplot(2, 2, 3)
sub3.plot(list(range(0, 22, 3)), 'v-')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title("3rd Rep")
plt.show()
