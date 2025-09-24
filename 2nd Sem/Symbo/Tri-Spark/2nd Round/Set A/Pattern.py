import matplotlib.pyplot as plt
Mul = []
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]
'''for i in range(len(values)):
    Mul.append(values[i] * 20)'''
plt.bar(categories, Mul, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()