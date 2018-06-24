import threading
import datetime
import sys
import os
import twitterbot.twitterbot as bot
from twitterbot.database import Post, engine
from sqlalchemy.orm import sessionmaker
from urllib import request
from twitterbot.reddit import reddit


Session = sessionmaker(bind=engine)


def set_interval(func, sec, sub):
    def func_wrapper():
        set_interval(func, sec, sub)
        func(sub)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def in_database(post, session=Session()):
    for p in session.query(Post).all():
        if p.id == post.id:
            return True
    return False


def update(subreddit):
    limit = {"l": 30}
    def inner():
        hours_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        # Top posts today
        new_posts = [
            post for post in reddit.subreddit(subreddit).hot(limit=limit["l"])
            if datetime.datetime.utcfromtimestamp(post.created_utc) >= hours_ago
        ]
        session = Session()
        # Select posts that are not in the database already
        new_posts = list(filter(lambda post: all(map(lambda p: p.id != post.id, session.query(Post).all())), new_posts))
        if len(new_posts) > 0:
            top_post = new_posts[0]
            post = Post(id=top_post.id)
            session.add(post)
            session.commit()
            session.close()
            bot.post(top_post)
        else:
            sys.stderr.write("No new posts\n")
            limit["l"] *= 2
            inner()
    inner()

def init_profile(sub):
    """
    Download the subreddits header icon
    and set it as profile pic.
    Then delete the picture.
    """
    icon_url = reddit.subreddit(sub).icon_img
    tmp_file = "tmp.{}".format(icon_url.split(".")[-1])
    request.urlretrieve(icon_url, tmp_file)
    bot.set_profile_pic(tmp_file)
    os.remove(tmp_file)
    print("Profile pic set to {}".format(icon_url))
