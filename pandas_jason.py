import requests
import pandas as pd
import matplotlib.pyplot as plt

url_users = "https://jsonplaceholder.typicode.com/users"
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments"

response_users = requests.get(url_users)
response_posts = requests.get(url_posts)
response_comments = requests.get(url_comments)

# print(response_users)

if response_users.status_code == 200 and response_posts.status_code == 200 and response_comments.status_code == 200:
    data_users = response_users.json()
    data_posts = response_posts.json()
    data_comments = response_comments.json()
else:
    raise Exception("Nie udalo sie pobrac danych")

# tworzenie dataframe
df_users = pd.DataFrame(data_users)
df_posts = pd.DataFrame(data_posts)
df_comments = pd.DataFrame(data_comments)

# print(df_users.to_string())

# print(df_posts.to_string()) # sprawdzamy co mamy w dataframe

posts_per_user = df_posts.groupby('userId')['id'].count()
# posts_per_user.rename(columns={'id': 'posts_count'}, inplace=True)
print(posts_per_user)