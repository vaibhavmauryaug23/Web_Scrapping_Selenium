from xml.etree.ElementTree import Comment
import nltk
import ssl
from pandas import *
import pandas
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download([
"names",
"stopwords",
"state_union",
"twitter_samples",
"movie_reviews",
"averaged_perceptron_tagger",
"vader_lexicon","punkt"])

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

hotel_data = read_csv("Hotel_List.csv")
comment_list = hotel_data["Hotel Comments"].to_list()
polarity_list = []
for i in comment_list:
    polarity_list.append(sia.polarity_scores(i)["compound"])

df = pandas.DataFrame()
df["Individual Comment Ratings"] = hotel_data["individual ratings"]
df["Polarity Score"] = polarity_list

p = df["Individual Comment Ratings"]
q=df["Polarity Score"]

plt.scatter(p, q) 
plt.title('A plot to show the correlation between Individual Comment Ratings and Polarity Score')
plt.xlabel("Individual Comment Ratings")
plt.ylabel("Polarity Score")
plt.plot(np.unique(p), np.poly1d(np.polyfit(p, q, 1))(np.unique(p)), color='Red')
plt.show()

ctr=0
l=[]

#Mean for each hotel
hotel_polarity_score = []

while polarity_list!=[]:
    l=polarity_list[:100]
    hotel_polarity_score.append(st.mean(l))
    polarity_list=polarity_list[100:]
#print(hotel_polarity_score)

l=[]
x=hotel_data["Overall Ratings "].to_list()
while ctr<2000:
    l.append(x[ctr])
    ctr+=100

x=l
y=hotel_polarity_score

hps = pandas.DataFrame()
hps["Overall Ratings"] = x
hps["Hotel_Polarity_Score"] = y

x = hps["Overall Ratings"]
y=hps["Hotel_Polarity_Score"]



plt.scatter(x, y) 
plt.title('A plot to show the correlation between Overall Ratings and Aggregate Polarity Score of each hotel')
plt.xlabel("Overall Ratings")
plt.ylabel("Hotel_Polarity_Score")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='Red')
plt.show()