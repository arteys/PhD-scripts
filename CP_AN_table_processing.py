import pandas

# cells_path = "./PhD_scripts/Data examples/CP_AN_table_processing/Cells.csv"
cells_path = "C:/Users/Modern/Desktop/Python/PhD-scripts/Data examples/CP_AN_table_processing/Cells.csv"

cells_df = pandas.read_csv(cells_path)
columns_names_arr = cells_df.columns.values

# print(columns_names_arr)
# print(cells_df.loc[:,"ObjectNumber"])

count = 0
for n in cells_df.loc[:,"ObjectNumber"]:
    if n>1:
        count = count + 1
    else:
        print(count)
