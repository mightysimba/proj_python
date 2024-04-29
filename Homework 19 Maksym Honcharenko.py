import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Homework 19 Maksym Honcharenko

# Перше завдання
zeros_array = np.zeros((4, 3))
print("Array of zeros:")
print(zeros_array)


ones_array = np.ones((4, 3))
print("\nArray of ones:")
print(ones_array)


sequential_array = np.arange(12).reshape(4, 3)
print("\nArray of numbers from 0 to 11:")
print(sequential_array)


x = np.arange(1, 101)
f_x = 2 * x**2 + 5

print("\nx\tF(x)")
for i in range(len(x)):
    print(f"{x[i]}\t{f_x[i]}")


x = np.arange(-10, 11)
f_x = np.exp(-x)

print("\nx\tF(x)")
for i in range(len(x)):
    print(f"{x[i]}\t{f_x[i]}")


# Друге завдання

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)
df_cards = df[['Team', 'Yellow Cards', 'Red Cards']]

teams_count = df['Team'].nunique()

teams_more_than_6_goals = df[df['Goals'] > 6]['Team']

print(df_cards)
print("Кількість команд які прийняли участь в Евро 2012:", teams_count)
print("Команди, які забили більше 6 голів: ", teams_more_than_6_goals)


# DataViz
glue = sns.load_dataset("glue")
glue.head()

sns.displot(data=glue, x="Score")
plt.title('Rating-count plot')
plt.show()


sns.regplot(x="Score", y="Year", data=glue)
plt.title('Score-Year regression plot')
plt.show()


sns.boxplot(x="Task", y="Score", data=glue)
plt.title('Score rating for different tasks')
plt.show()

sns.scatterplot(x="Task", y="Score", data=glue)
plt.title('Task-score scatterplot')
plt.show()

