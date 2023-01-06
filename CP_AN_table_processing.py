import pandas as pd

# cells_path = "./PhD_scripts/Data examples/CP_AN_table_processing/Cells.csv"
cells_path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_AN_table_processing/Cells.csv"
apoptosis_path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_AN_table_processing/Apoptotic_Cells.csv"
necrosis_path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_AN_table_processing/Necrotic_Cells.csv"
an_path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_AN_table_processing/Necrotic_Apoptotic_Cells.csv"

cells_df = pd.read_csv(cells_path)
apoptosis_df = pd.read_csv(apoptosis_path )
necrosis_df = pd.read_csv(necrosis_path)
an_df = pd.read_csv(an_path)
# columns_names_arr = cells_df.columns.values


image_names = pd.unique(cells_df.loc[:,"FileName_Original"]) #Extract unique names of images

for name in image_names:
    cells_df_current = cells_df.loc[cells_df["FileName_Original"] == name] #Extract all rows with same image name
    apoptosis_df_current = apoptosis_df.loc[apoptosis_df["FileName_Original"] == name]
    necrosis_df_current = necrosis_df.loc[necrosis_df["FileName_Original"] == name]
    an_df_current = an_df.loc[an_df["FileName_Original"] == name]

    cells_number = cells_df_current.shape[0] #Count number of rows with same image name
    apoptosis_number = apoptosis_df_current.shape[0]
    necrosis_number = necrosis_df_current.shape[0]
    an_df_number = an_df_current.shape[0]

    print(cells_number,apoptosis_number,necrosis_number,an_df_number)

