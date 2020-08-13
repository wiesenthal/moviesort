import numpy as np
import matplotlib.pyplot as plt

rtFile = open('rtOut.txt', 'r')
imdbFile = open('imdbOut.txt', 'r')

rtDict = {}
for line in rtFile.readlines():
    title, rating = line.strip().split('= ')
    rtDict[title] = int(rating)
rtFile.close()

imdbDict = {}
for line in imdbFile.readlines():
    title, rating = line.strip().split('= ')
    imdbDict[title] = int(float(rating)*10)

imdbFile.close()

movies = rtDict.keys()
ratings = rtDict.values()

ratings2 = imdbDict.values()

plt.scatter(range(0, len(ratings)), ratings, color="red", label="rotten tomatoes")
plt.scatter(range(0, len(ratings2)), ratings2, label="imdb")

plt.show()
