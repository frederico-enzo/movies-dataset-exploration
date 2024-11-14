import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset fornecido pelo usuário
file_path = 'data\movie_metadata.csv'
movies_df = pd.read_csv(file_path)

# Mostrar as primeiras linhas do dataset e informações básicas
movies_df.head(), movies_df.info()
# Estatísticas descritivas para as colunas de orçamento e bilheteira
budget_gross_stats = movies_df[['budget', 'gross']].describe()

# Remover dados nulos para análise de correlação e visualização
budget_gross_data = movies_df[['budget', 'gross']].dropna()

# Calcular a correlação entre orçamento e bilheteira
correlation = budget_gross_data.corr().loc['budget', 'gross']

# Configurar visualizações
plt.figure(figsize=(14, 6))

# Histograma para Orçamento
plt.subplot(1, 2, 1)
sns.histplot(movies_df['budget'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribuição de Orçamento')
plt.xlabel('Orçamento')
plt.ylabel('Frequência')

# Histograma para Bilheteira
plt.subplot(1, 2, 2)
sns.histplot(movies_df['gross'].dropna(), bins=30, kde=True, color='green')
plt.title('Distribuição de Bilheteira')
plt.xlabel('Bilheteira')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

# Gráfico de dispersão entre Orçamento e Bilheteira
plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='gross', data=budget_gross_data, alpha=0.5)
plt.title('Relação entre Orçamento e Bilheteira')
plt.xlabel('Orçamento')
plt.ylabel('Bilheteira')
plt.show()

# Exibir estatísticas descritivas e correlação
budget_gross_stats, correlation