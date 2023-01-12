import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/Modern/Desktop/Thesis big files/12-12-22 Spheroids FH/Dish 0.3/Dark/Counted/Spheroids_filtered.csv"

spheroids_df = pd.read_csv(path)

labels = spheroids_df.columns.values

spheroids_compact_df = spheroids_df[["ObjectNumber","AreaShape_Area","AreaShape_MeanRadius",
    "AreaShape_FormFactor","Intensity_IntegratedIntensity_Grayscale"]]

spheroids_compact_df["Type"] = "Agarose_300"

#ADD OBJECT TYPE LABELS FOR DIFFEREND KINDS OF SPHEROIDS

# print(labels)

print(spheroids_compact_df) #IN PIXELS!!

# sns.scatterplot(data=spheroids_df, x="AreaShape_Area", y="AreaShape_Eccentricity", color=".15")
# sns.kdeplot(data=spheroids_df, x="AreaShape_Area", y="AreaShape_Eccentricity", levels=5, color="b", linewidths=1)

# plt.show()