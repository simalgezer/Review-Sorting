#Importing libraries & preparing data
import numpy as np
import pandas as pd
import math
import scipy.stats as st

pd.set_option ('display.max_columns', None)
pd.set_option ('display.width', None)
pd.set_option ('display.expand_frame_repr', False)
pd.set_option ('display.float_format', lambda x: '%.5f' % x)

df_ = pd.read_csv("/kaggle/input/amazon-review/amazon_review.csv")
df = df_.copy()

#Creating a time-weighted average & comparing it with existing avg-rating
import matplotlib.pyplot as plt

df["day_diff"].hist(bins=20)
plt.show()

a = df["day_diff"].quantile(0.25)
b = df["day_diff"].quantile(0.50)
c = df["day_diff"].quantile(0.75)

df["day_diff"].mean()

time_weighted_avg = df.loc[df["day_diff"] <= a, "overall"].mean() * 40 / 100 + \
df.loc[(df["day_diff"] > a) & (df["day_diff"] <= b), "overall"].mean() * 30 / 100 + \
df.loc[(df["day_diff"] > b) & (df["day_diff"] <= c), "overall"].mean() * 20 / 100 + \
df.loc[(df["day_diff"] > c), "overall"].mean() * 10 / 100

avg_rating = df.overall.mean(). #4.587589013224822
((time_weighted_avg-avg_rating)/avg_rating)*100 #0.8834266717838546

#Preparing data for wilson lower bound method
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]
df = df[["reviewerName", "overall", "summary", "helpful_yes", "helpful_no", "total_vote", "reviewTime"]]
df.head()

#Applying wilson lower bound
# score_pos_neg_diff
df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)

# score_average_rating
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)

# wilson_lower_bound
df["wilson_lower_bound"] = df.apply (lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

df.head()
df.loc[df["helpful_yes"] > 5]

#Sorting reviews according to score_average_rating
df.sort_values("score_average_rating", ascending=False).head(20)

#Sorting reviews according to wilson_lower_bound
df.sort_values("wilson_lower_bound", ascending=False).head(20)
