# 1: Using the videogames.csv file provided on D2L, read the file in using Pandas.
import pandas as pd

df = pd.read_csv("Assignments/Lab1/videogames.csv")

# 2: Write a function that will accept the dataframe and the name of a publisher that outputs all games from that publisher sorted in alphabetical order.
def games_by_publisher(df, publisher):
    return df[df["Publisher"] == publisher].sort_values(by="Name")

print(games_by_publisher(df, "Nintendo"))

# 3: Write a function that will accept the dataframe and output the amount of games per genre as a percentage (x.x% / 100%).
def games_by_genre(df):
    return (df["Genre"].value_counts(normalize=True) * 100).map("{:.2f}%".format)

print(games_by_genre(df))

# 4: Write a function that will accept the dataframe and the name of a platform that outputs the top 5 games for that platform based on global sales.
#   a. The output should include the number in ranking, the name of the game, and the number of copies sold.
#   b. The data in videogames.csv is in millions, and will need to be converted.
def top_games_by_platform(df, platform):
    return df[df["Platform"] == platform].sort_values(by="Global_Sales", ascending=False).head(5)[["Name", "Global_Sales"]]

print(top_games_by_platform(df, "Wii"))

# 5: Using the year, write a function that will create a line chart that shows total video game sales across time.
import matplotlib.pyplot as plt

def sales_by_year(df):
    return df.groupby("Year").sum()["Global_Sales"].plot()

sales_by_year(df)
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.title("Global Sales by Year")
plt.show()