import pandas as pd

def number_type_from_imagename(image_name):
    i = 0
    for symbol in image_name:
        if symbol.isdigit():
            i = i+1
        if symbol.isalpha():
            break
    image_number = int(image_name[0:i])
    image_type = image_name[i:12+i]

    return image_number,image_type

def mean_and_stdev_by_type(dataframe,image_type):
    current_df = dataframe.loc[dataframe["Image type"] == image_type]
    cells = current_df["N Cells"].mean()
    cells_stdev = current_df["N Cells"].std()
    apoptotic = current_df["N Apoptotic"].mean()
    apoptotic_stdev = current_df["N Apoptotic"].std()
    necrotic = current_df["N Necrotic"].mean()
    necrotic_stdev = current_df["N Necrotic"].std()
    na = current_df["N NA"].mean()
    na_stdev = current_df["N NA"].std()

    data = pd.DataFrame({'Cells':[cells], 'Apoptotic':[apoptotic],'Necrotic':[necrotic], 'NA':[na], 'Cells std':[cells_stdev], 
        'Apoptotic std':[apoptotic_stdev], 'Necrotic std':[necrotic_stdev], 'NA std':[na_stdev]})

    data_round = data.round(0)

    return data_round

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

result_df = pd.DataFrame({'Image number':[], 'Image name':[], 'Image type':[], 'N Cells':[], 'N Apoptotic':[], 'N Necrotic':[], 'N NA':[]})

for name in image_names:
    cells_df_current = cells_df.loc[cells_df["FileName_Original"] == name] #Extract all rows with same image name
    apoptosis_df_current = apoptosis_df.loc[apoptosis_df["FileName_Original"] == name]
    necrosis_df_current = necrosis_df.loc[necrosis_df["FileName_Original"] == name]
    an_df_current = an_df.loc[an_df["FileName_Original"] == name]

    cells_number = cells_df_current.shape[0] #Count number of rows with same image name
    apoptosis_number = apoptosis_df_current.shape[0]
    necrosis_number = necrosis_df_current.shape[0]
    an_df_number = an_df_current.shape[0]

    #Extract original image number from image name
    image_number,image_type = number_type_from_imagename(name)

    #Create df with current data 
    result_current =  pd.DataFrame({'Image number':[image_number], 'Image name':[name],'Image type':[image_type], 'N Cells':[cells_number], 'N Apoptotic':[apoptosis_number], 
        'N Necrotic':[necrosis_number], 'N NA':[an_df_number]})

    #Append current data to result df
    # result_df = result_df.append(result_current)
    result_df = pd.concat([result_current, result_df])

result_df = result_df.sort_values(by=['Image name'])
result_sorted_df = result_df.sort_values(by=['Image number'])

data = mean_and_stdev_by_type(result_sorted_df,'ApNec 300-20')
print(data)



