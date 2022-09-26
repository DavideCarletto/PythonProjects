import pandas as pd

def series():

    # A pandas series is like a column in a table. It is a one-dimensional array holding data of any type.

    ds = [5,10,15,20,25]
    series = pd.Series(ds, index=["one","two","three","four","five"])

    print(f"Series from dataSet: \n{series}\n")

    ds2 = {"one": 5,"two": 10, "three": 15, "four": 20, "five": 25}
    series2 = pd.Series(ds2, index=["one", "four"])

    print(f"Series from dict (picked only two elements): \n{series2}\n")


def dataFrames():

    # A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
    # Series is like a column, a DataFrame is the whole table.

    ds =  {
        "Mesi":["Gennaio","Agosto","Dicembre"],
        "Giorni": [31,31,31],
        "Festivita":["Capdoanno","Ferragosto","Natale"]
    }

    df = pd.DataFrame(ds, index=["Mese1", "Mese2", "Mese3"])

    print(df.loc[["Mese1","Mese3"]])

def read_files():

    df = pd.read_csv("../Pandas/pokemon.csv", sep=",", index_col=0) # Index col = 0 means that indices on columns are not automatically generated
    print(f"Data frame from csv: \n{df}\n") # If u want to display all rows, use the toString method

    df2 = pd.read_json("../Pandas/pokemon.json")
    print(f"Data frame from json:\n {df2}")

    print(f"Maximun rows: {pd.options.display.max_rows}")
    #same thing with excel files

def select_data():

    df = pd.read_csv("../Pandas/pokemon.csv", index_col=1) # In this case, index_col is the column number 1 (the name of the pokemon)
    print(f"Data selected with slicing: \n{df[10:20]}")

    print(f"Data selected with head function: \n{df.head(10)}")
    print(f"Data selected with tail function: \n{df.tail(10)}")
    print(f"Data selected with specific columns: \n{df[['HP', 'Attack']][10:15]}\n") # Could be used head and tail methods as well
    print(f"Data selected with loc method: \n{df.loc['Bulbasaur':'Squirtle',['HP','Attack']]}\n") # The last one is included
    print(f"Data selected with iloc method: \n{df.iloc[0:10,[4,5]]}\n") # The last one is not included

def iterate_dataFrame():

    # The iteration creates a copy of the dataframe, so do not modify data with iteration!

    df = pd.read_csv("../Pandas/pokemon.csv").head(3)

    print("Iterate dataFrame with iteritems: \n")

    for key in df.iteritems():
        print(key)

    print()

    print("Iterate dataFrame with iterrrows: \n")

    for index,row in df.iterrows():
        print(index,row)

    print()

    print("Iterate dataFrame with itertuples: \n")

    for row in df.itertuples():
        print(row)

def sort_dataFrame():

    df = pd.read_csv("../Pandas/pokemon.csv")
    sdf = df.sort_index(ascending=False)

    print(f"Data frame sorted by indices in descending order: \n{sdf.head(6)}")
    print()

    sdf2 = df.sort_values(by=["Total","HP"], ascending=[True, False])

    print(f"Data frame sorted by total and hp values: \n{sdf2[['Name','Total', 'HP']].head(6)}")

def modify_dataFrame():

    df = pd.read_csv("../Pandas/pokemon.csv")

    # Add columns with 4 methods

    #df[["Wii","Switch","Gameboy"]] = ["2nd","7th","1st"]
    #df.insert(13,"Wii","2nd")
    #df.loc[:, "Wii"] = "2nd"
    df = df.assign(Wii = "2nd")

    print(f"Added columns: \n{df.head(5)}\n")


    # Delete columns with 3 methods

    #df.drop("Legendary", inplace=True, axis=1) # Axis = 1 means columns, axis = 0 means row, inplace = true means u want to remove from the specific dataframe
    #del df["Legendary"]
    colPop = df.pop("Legendary")

    print(f"Removed Legendary column: \n{df.head(5)}\n")
    print(f"List of columns removed: \n{colPop.head(5)}\n")

    # Reverse columns

    columns = df.columns.tolist()
    columns.reverse()

    print(f"Data frame with columns reversed: \n{df[columns].head(5)}\n")

def save_to_file():

    df = pd.read_csv("Pandas/pokemon.csv", sep=",")
    df2 = df[["Name","Attack","Speed"]]
    df3 = df[["Name","Attack"]]
    df4 = df[["Name","Speed"]]

    #df2.to_csv("Pandas/mini_pokemon.csv", index=False) # Index = False means that indices won't be in csv file

    # If u want to create a zip file, follow this method:

    #compressed_options = dict(method = "zip", archive_name = "Pandas/nuovi_pokemon.csv")
    #df2.to_csv("Pandas/nuovi_pokemon.zip", index = False, compression = compressed_options)

    # Save to excel file with one sheet

    #df2.to_excel("Pandas/nuovi_pokemon2.xlsx", index=False, sheet_name="Pokemon stats")

    # Save to excel file with multiple sheets

    with pd.ExcelWriter("../Pandas/nuovi_pokemon2.xlsx") as writer:
        df2.to_excel(writer, sheet_name="Pokemon stats", index=False)
        df3.to_excel(writer, sheet_name="Pokemon attacks", index=False)
        df4.to_excel(writer, sheet_name="Pokemon speeds", index=False)

    # Append a sheet to excel file

    df5 = df[["Name","Type 1"]]

    with pd.ExcelWriter("Pandas/nuovi_pokemon2.xlsx", mode="a") as writer:
        df5.to_excel(writer,sheet_name="Pokemon type 1", index=False)

def filter_dataFrame():

    df = pd.read_csv("../Pandas/pokemon.csv")


    print(f" DataFrame filtered:\n {df[(df['Total']>500) & (df['HP']>150)]}\n")
    print(f" DataFrame filtered with loc: \n {df.loc[(df['Name'].str.contains('saur')),['Name','Total','HP']]}\n")
    print(f" DataFrame filtered with query: \n {df.query('Total > 750 and Speed > 50')}\n")

def modify_data():

    df = pd.read_csv("Pandas/pokemon.csv")

    df.loc[(df['Name'].str.contains('saur')), 'Type 1'] = 'newType'
    print(f" Single columns modified: \n\n {df.head(10)}\n")


    df.loc[(df['Name'].str.contains('saur') & (df['Speed']>45)), ['Type 1','Type 2']] = ['newType1', 'newType2']
    print(f" Multiple columns modified: \n\n {df.head(10)}")

def clean_data():

    df = pd.read_csv("../Pandas/calories.csv")

    print(f" Dataframe without all data been cleaned:\n\n {df}\n")

    #df.dropna(inplace=True)  if you want to drop all the NaN values from the dataframe
    df["Calories"].fillna(df["Calories"].mean(), inplace=True) # .mean() is the average
    df["Date"].fillna("2020/12/22",inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])

    for index in df.index:
        if df.loc[index, 'Duration'] >60:
            df.loc[index, 'Duration'] = 60

    print(f" Dataframe with all data been cleaned:\n\n {df}\n")

def main():

    #series()
    #dataFrames()
    #read_files()
    #select_data()
    #iterate_dataFrame()
    #sort_dataFrame()
    #modify_dataFrame()
    #save_to_file()
    #filter_dataFrame()
    #modify_data()
    clean_data()

if __name__ == "__main__":

    # Pandas is a Python library used for working with data sets.
    # It has functions for analyzing, cleaning, exploring, and manipulating data.

    main()
