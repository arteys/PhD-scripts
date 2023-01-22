import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "C:/Users/Modern/Desktop/Thesis big files/26-12-2022 FH on Matrix S/Counted/Shperoids_filtered.csv"
path_2 = "C:/Users/Modern/Desktop/Thesis big files/29-12-2022 FH on Matrix E 300-20/48H/Counted/Spheroids.csv"
path_3 = "C:/Users/Modern/Desktop/Thesis big files/12-12-22 Spheroids FH/Dish 0.4/Counted/Shperoids_filtered.csv"

spheroids_df = pd.read_csv(path)
spheroids_df_2 = pd.read_csv(path_2)
spheroids_df_3 = pd.read_csv(path_3)

labels_2 = spheroids_df_2.columns.values
print(labels_2)

spheroids_df["AreaShape_EquivalentDiameter"] = spheroids_df["AreaShape_EquivalentDiameter"]/1.49
spheroids_df_2["AreaShape_EquivalentDiameter"] = spheroids_df["AreaShape_EquivalentDiameter"]/1.49
spheroids_df_3["AreaShape_EquivalentDiameter"] = spheroids_df["AreaShape_EquivalentDiameter"]/3.02

spheroids_compact_df = spheroids_df[["ObjectNumber","AreaShape_Area","AreaShape_EquivalentDiameter",
    "AreaShape_FormFactor","AreaShape_MeanRadius","Intensity_MeanIntensity_Grayscale"]]

spheroids_compact_df_2 = spheroids_df_2[["ObjectNumber","AreaShape_Area","AreaShape_EquivalentDiameter",
    "AreaShape_FormFactor","AreaShape_MeanRadius","Intensity_MeanIntensity_Grayscale"]]

spheroids_compact_df_3 = spheroids_df_3[["ObjectNumber","AreaShape_Area","AreaShape_EquivalentDiameter",
    "AreaShape_FormFactor","AreaShape_MeanRadius","Intensity_MeanIntensity_Grayscale"]]


spheroids_compact_df["Type"] = "EDC 600-20"
spheroids_compact_df_3["Type"] = "Agarose"
spheroids_compact_df_2["Type"] = "EDC 300-20"


# print(spheroids_compact_df_2)

frames_df = [spheroids_compact_df,spheroids_compact_df_2,spheroids_compact_df_3]
ultimate_df = pd.concat(frames_df)

# print(ultimate_df)


# fig, ax =plt.subplots(1,2)
plt.subplots(figsize=(4, 4))

ax1 = sns.scatterplot(data=ultimate_df, x="AreaShape_EquivalentDiameter", y="AreaShape_FormFactor", hue = "Type")
# ax2 = sns.scatterplot(data=ultimate_df, x="AreaShape_EquivalentDiameter", y="Intensity_IntegratedIntensity_Grayscale", hue = "Type",ax=ax[1])
# ax1 = sns.kdeplot(data=ultimate_df, x="AreaShape_EquivalentDiameter", y="Intensity_IntegratedIntensity_Grayscale", hue = "Type", levels=5, linewidths=1)
# sns.swarmplot(data=ultimate_df, y="AreaShape_EquivalentDiameter", x="AreaShape_FormFactor", hue = "Type")
# sns.relplot(data=ultimate_df, y="AreaShape_EquivalentDiameter", x="AreaShape_FormFactor", hue = "Type")


plt.legend(fontsize=10)
ax1.set(xlabel='Equvalent diameter, μm', ylabel='Form factor')
ax1.set_aspect('auto')

# ax2.set(xlabel='Equvalent diameter, μm', ylabel='Integral intensity, A.U.')


plt.show()