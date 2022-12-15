import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm

df = pd.read_csv("C:/Users/Modern/Мой диск/Диссертация/Data/Diametres.csv")


x_list = [0,350, 840] #X coordinates of circles

diameter_list = [100,150,200]



fig, ax = plt.subplots() 

i = 0
colors = ['b','g','r']

# text_kwargs = dict(ha='center', va='center', fontsize=28, color='C1')

for column in df:
    print('Column Name: ', column)

    std_column = df[column].std()
    mean_column = df[column].mean()

    print(mean_column)
    print(std_column)

    circle_base = plt.Circle((x_list[i], 0), diameter_list[i], facecolor='none', alpha=1, edgecolor=colors[i], linestyle='dashed', label = column)
    circle_mean = plt.Circle((x_list[i], 0), mean_column/2, facecolor='none', alpha=1, edgecolor=colors[i], label = 'Mean')
    circle_std = plt.Circle((x_list[i], 0), mean_column/2, facecolor='none', alpha=0.2, edgecolor=colors[i], linewidth=std_column, label = "Standart devitaion")
    plt.text(x_list[i], 0, column, color=colors[i], fontsize=12, ha='center',va='center')


    ax.add_patch(circle_base)
    ax.add_patch(circle_mean)
    ax.add_patch(circle_std)

    i = i+1

# legend = ax.legend()

ax.set_aspect('equal')
plt.xticks([])
plt.autoscale() 
plt.ylabel('Equivalent diameter, μm')
ax.set(ylim=(-300, 300))
plt.show()
# plt.savefig('C:/Users/Modern/Мой диск/Диссертация/Images/Graphs/Circle graph.png', bbox_inches='tight')