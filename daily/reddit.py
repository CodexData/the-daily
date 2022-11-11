import praw

import pandas as pd

# Reddit app API details
reddit = praw.Reddit(
    client_id="Your Client ID",
    client_secret="Your Client Secret",
    password="Your Password",
    user_agent="Your User Agemt",
    username="Your Username",
)

# Print USERNAME to test functionality
print(reddit.user.me())

posts = []
# change 'MachineLearning' to name of desired subreddit
ml_subreddit = reddit.subreddit('MachineLearning')

# ml_subreddit.hot(limit=10) scrapes the top 10 hottest posts from the chosen subreddit
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

# strangely i got append to work. Go Figure. The below creates and prints a DF, which can be transferred to a csv using the function whiich is hashed out
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)

# posts.to_csv("Posts")
