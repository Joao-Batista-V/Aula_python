import matplotlib.pyplot as plt

# Definindo variáveis
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 5, 6, 4, 8, 5, 4, 6, 3, 11]

# Criando um gráfico
plt.scatter(x, y, label = 'Pontos', color= 'b', marker=',', s=100)

plt.legend()

plt.show()
