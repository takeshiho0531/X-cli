import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    bearer_token=os.environ["BEARER_TOKEN"],
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_KEY_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)

client.create_tweet(
    text="I'm tweeting from the command line. Isn't that special?"
)  # noqa
