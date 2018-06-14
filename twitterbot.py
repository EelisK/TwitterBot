from secret_keys import consumer_key, consumer_secret, access_token, access_token_secret
import twitter


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


def post(post):
    api.PostUpdate(status="{}\n{}".format(post.title, post.url), media=post.url)
    print(post.url)
