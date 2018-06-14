import praw
from secret_keys import client_id, client_secret

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='DeepFriedMemeBot')
