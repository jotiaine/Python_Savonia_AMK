import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y2points = np.array([5, 5, 2, 8, 7, 1, 2, 3, 4, 5])

# plot 1
plt.subplot(1, 2, 1)
plt.plot(ypoints, '*:r', ms=20, mec='black')
plt.plot(y2points, '*:b', ms=20, mec='y')
plt.title("Testing")
plt.xlabel("X-label")
plt.ylabel("Y-label")

# plot 2
ypoints = np.array([5, 2, 1, 4, 5, 9, 9, 1, 1, 10])
y2points = np.array([5, 1, 1, 4, 9, 9, 2, 3, 4, 5])
plt.subplot(1, 2, 2)
plt.plot(ypoints, '*:r', ms=20, mec='black')
plt.plot(y2points, '*:b', ms=20, mec='y')
plt.title("Testing")
plt.xlabel("X-label")
plt.ylabel("Y-label")


plt.grid()
plt.show()


x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()


y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
