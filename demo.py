
#modifyfordemo
#modifynumber
import matplotlib.pyplot as plt
x = [3, 5, -1, 0, 1, 2, 3, 4]
n = [-3, -2, -1, 0, 1, 2, 3, 7]

#plt.plot(n,x)


plt.figure(1)
plt.stem(n,x)

plt.figure(2)
plt.stem(x)
plt.show()

