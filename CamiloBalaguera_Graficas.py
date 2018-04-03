import matplotlib.pyplot as plt
import numpy as np
# Se cargan los archivos de tiempos para cada codigo.
python = np.genfromtxt("times_python.csv", usecols = 0, 1)
cpp = np.genfromtxt("times_cpp.csv", delimiter = ",", usecols = 0, 1)

# Se crea la gráfica que compara ambos archivos de texto
plt.figure()
plt.plot(np.transpose(python)[0], np.transpose(python)[1], label = "Python3")
plt.plot(np.transpose(cpp)[1], np.transpose(cpp)[0], label = "C++")
plt.legend(loc=0)
plt.savefig("cpp_vs_python.png")


