import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp
import seaborn as sb
import PyQt5

mp.use('Qt5Agg')

nateamdf = pd.read_csv("data/DataViz Project - NATeams.csv")  # Reads into the CSV files using ; as the delimter.
euteamdf = pd.read_csv("data/DataViz Project - EUTeams.csv")
totaldf = nateamdf.append(euteamdf)
print(totaldf)

plot = sb.scatterplot(data=totaldf, x='games', y='wins',hue='region')
plt.xlabel = "Games"
plt.ylabel = "Wins"
plt.title = "Games VS Wins"
plt.legend(["NA", "EU"], loc="upper right")


plt.show()
