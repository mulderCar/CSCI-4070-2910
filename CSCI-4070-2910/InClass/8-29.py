# run 'pip install pandas' in terminal to install pandas
import pandas as pd

# df = Data Frame
# A data frame is a 2D data structure with columns that can be of different data types like a spreadsheet or SQL table

df = pd.read_csv('./AllPokemon.csv')

print(df[800:]) # print from 800th row to the end

print(df.Name) # print all the names of the pokemon