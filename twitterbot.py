from secret_keys import consumer_key, consumer_secret, access_token, access_token_secret
from time import strftime, gmtime
import twitter


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


def post(post):
    api.PostUpdate(status="{}\n{}".format(post.title,
                                          "reddit.com{}".format(post.permalink)),
                   media=post.url)
    print("{:30} {:30} {:30}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), post.title, post.url))


def set_profile_pic(url):
    api.UpdateImage(image=url)
