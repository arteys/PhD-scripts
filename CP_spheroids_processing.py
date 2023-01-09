import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_spheroids_processing/Spheroids.csv"

spheroids_df = pd.read_csv(path)

labels = spheroids_df.columns.values

# print(labels)

sns.scatterplot(data=spheroids_df, x="AreaShape_Area", y="AreaShape_Eccentricity")

plt.show()