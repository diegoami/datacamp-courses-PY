# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets_2.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda txt: txt.startswith('RT'), tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
