import pandas as pd
import matplotlib.pyplot as plt
from numpy import array

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

# Read the CSV file into a DataFrame
df = pd.read_csv("24.csv",encoding='UTF-8')

# Extracting columns 'name' and 'score'
names = df['name']
score1 = df['score1']
score2 = df['score2']
score = df['score']

plt.figure(figsize=(10, 6))  # Adjust size as needed
plt.bar(names, score1, color='skyblue')
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores by Name')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
score = array(score)
score.sort()
print(score)