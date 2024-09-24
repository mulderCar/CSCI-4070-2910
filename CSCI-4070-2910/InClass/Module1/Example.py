# cmd --> 'python --version' to test if you have python

# if you don't have a package, use pip
# cmd --> 'pip install pandas' to install packages you don't have
import pandas as pd

# df = Data Frame
# Holds our data (think spreadsheet)
df = pd.read_csv('Data/AllPokemon.csv')

print(df[800:])