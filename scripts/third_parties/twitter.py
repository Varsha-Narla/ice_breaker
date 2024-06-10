import os 
from dotenv import load_dotenv
import tweepy 
import requests
import tweepy.client 

load_dotenv()

twitter_client=tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
)


def scrape_user_tweets(username, num_tweets=5, mock: bool=False):
    """ scrapes user's original tweets and returns them as a dictionary
    """
    tweet_list=[]
    if mock:
        EDEN_TWITTER_GIST="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        tweets=requests.get(EDEN_TWITTER_GIST, timeout=5).json()

        for tweet in tweets:
            tweet_dict={}
            tweet_dict["text"]=tweet["text"]
            tweet_dict["url"]=f"https://twitter.com/{username}/status{tweet['id']}"
            tweet_list.append(tweet_dict)


    else:
        user_id=twitter_client.get_user(username=username).data.id
        tweets=twitter_client.get_user_tweets(
            id=user_id,max_results=num_tweets, exclude=["retweets", "replies"]
        )

        for tweet in tweets:
            tweet_dict={}
            tweet_dict["text"]=tweet["text"]
            tweet_dict["url"]=f"https://twitter.com/{username}/status{tweet['id']}"
            tweet_list.append(tweet_dict)


if __name__=="__main__":
    tweets=scrape_user_tweets(username="EdenEmarco177", mock=True)
    print(tweets)