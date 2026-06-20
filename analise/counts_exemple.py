import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('analise/titanic.csv')

survived_counts = df['Survived'].value_counts()

print(survived_counts)

# criação do gráfico

plt.figure(figsize=(8,6))

plt.bar(survived_counts.index, survived_counts, color='pink')

plt.title('Contagem de sobreviventes')
plt.xlabel('Survived (0 / 1)')
plt.ylabel('Contagem')

plt.show()