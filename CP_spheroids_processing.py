import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/Modern/Desktop/Thesis big files/12-12-22 Spheroids FH/Dish 0.3/Dark/Counted/Spheroids_filtered.csv"
path_2 = "C:/Users/Modern/Desktop/Thesis big files/29-12-2022 FH on Matrix E 300-20/48H/Counted/Spheroids.csv"

spheroids_df = pd.read_csv(path)
spheroids_df_2 = pd.read_csv(path_2)

labels_2 = spheroids_df_2.columns.values

spheroids_compact_df = spheroids_df[["ObjectNumber","AreaShape_Area","AreaShape_MeanRadius",
    "AreaShape_FormFactor","Intensity_IntegratedIntensity_Grayscale"]]

spheroids_compact_df_2 = spheroids_df_2[["ObjectNumber","AreaShape_Area","AreaShape_MeanRadius",
    "AreaShape_FormFactor","Intensity_IntegratedIntensity_Grayscale"]]

spheroids_compact_df["Type"] = "Agarose_300"
spheroids_compact_df_2["Type"] = "EDC_300-20"


# print(spheroids_compact_df_2)

frames_df = [spheroids_compact_df,spheroids_compact_df_2]
ultimate_df = pd.concat(frames_df)

print(ultimate_df)

# print(spheroids_compact_df) #IN PIXELS!!

sns.scatterplot(data=ultimate_df, x="AreaShape_MeanRadius", y="AreaShape_FormFactor", hue = "Type")
sns.kdeplot(data=ultimate_df, x="AreaShape_MeanRadius", y="AreaShape_FormFactor", hue = "Type", levels=5, color="b", linewidths=1)

plt.show()