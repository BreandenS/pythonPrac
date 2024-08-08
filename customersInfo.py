import pandas as pd


data = pd.read_csv("Infor.csv")


def main():

  
    total_rating = data["Rating"].sum()
    num_feedback = len(data)
    average_rating = total_rating / num_feedback
    print(calculateAverageRating(average_rating))

def calculateAverageRating(average_rating):
  
    return average_rating


average_ratings = data.groupby("Product")["Rating"].mean()
sorted_ratings = average_ratings.sort_values(ascending=False)
top_3_products = sorted_ratings.head(3)
print(top_3_products)


def calculateTop3products(top_3_products):
    return top_3_products


data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data["Month"] = data["Date"].dt.to_period("M")
data = data.dropna(subset=["Month"])
feedback_per_month = data.groupby("Month").size()

print((feedback_per_month))


def calculateFeedback(feedback_per_month):
    return feedback_per_month


main()
