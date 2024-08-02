import pandas as pd


data = pd.read_csv("Infor.csv")


def calculateAverageRating(average_rating):

    print(f"Average Rating: {average_rating}")

    return average_rating


total_rating = data["Rating"].sum()
num_feedback = len(data)
average_rating = total_rating / num_feedback

calculateAverageRating(average_rating)

def calculateTop3products(top_3_products):
    
    print(top_3_products)
    
average_ratings = data.groupby("Product")["Rating"].mean()
sorted_ratings = average_ratings.sort_values(ascending=False)

top_3_products = sorted_ratings.head(3)

calculateTop3products(top_3_products)

def calculateFeedback(feedback_per_month):

 print(feedback_per_month)
 
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
data["Month"] = data["Date"].dt.to_period("M")
data = data.dropna(subset=["Month"])
feedback_per_month = data.groupby("Month").size()

calculateFeedback(feedback_per_month)
