import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

data = pd.read_csv("Hotel_List.csv", encoding= 'unicode_escape')
print(data.head())

ratings = data["individual ratings"].value_counts()
numbers = ratings.index
quantity = ratings.values

custom_colors = ["Red", "yellow", 'Green', "blue", "black", "orange"]
plt.figure(figsize=(5, 5))
plt.pie(quantity, labels=numbers, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Hotel Reviews Ratings", fontsize=20)
plt.show()

data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["individual ratings"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["individual ratings"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["individual ratings"]]
data["Compound"] = [sentiments.polarity_scores(i)["comp"] for i in data["individual ratings"]]
print(data.head())

x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive 😊 ")
    elif (b>a) and (b>c):
        print("Negative 😠 ")
    else:
        print("Neutral 🙂 ")
sentiment_score(x, y, z)
