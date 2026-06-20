import matplotlib.pyplot as plt

# criando um grafico de linhas 
#plt.plot([1, 2, 3], [2, 6, 7])

# imprimindo o gráfico
#plt.show()

# Dados
x = ['Maçãs', 'Laranjas', 'Uva']
y = [5, 3, 7]

plt.bar(x, y, color= 'orange')

# adicionando rotulos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()