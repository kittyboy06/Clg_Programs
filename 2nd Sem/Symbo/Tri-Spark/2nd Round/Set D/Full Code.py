import matplotlib.pyplot as plt

E_X = [3, 0, 0, 3, 0, 0, 3]
E_Y = [0,0,-2,-2,-2,-4,-4]

Z_X = [4,7,4,7]
Z_Y = [0, 0, -4, -4]

plt.plot(E_X, E_Y, 'k')
plt.plot(Z_X, Z_Y, 'k')

plt.axis('equal')
plt.title("EZ")
plt.show()
