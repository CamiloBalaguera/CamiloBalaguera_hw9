import matplotlib.pyplot as plt
import numpy as np

python = np.genfromtxt("times_python.csv", usecols = 0, 1)
c++ = np.genfromtxt("times_cpp.csv", delimiter = ",", usecols = 0, 1)

plt.figure()
plt.plot(np.transpose(python)[0], np.transpose(python)[1], label = "Python3")
plt.plot(np.transpose(c++)[1], np.transpose(c++)[0], label = "C++")
plt.legend(loc=0)
plt.savefig("cpp_vs_python.png")


