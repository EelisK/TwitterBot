import threading
import datetime
import sys
import twitterbot
from database import Post, engine
from sqlalchemy.orm import sessionmaker
from reddit import reddit


Session = sessionmaker(bind=engine)


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def in_database(post, session=Session()):
    for p in session.query(Post).all():
        if p.id == post.id:
            return True
    return False


def update_memes():
    hours_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    new_posts = [
        post for post in reddit.subreddit('DeepFriedMemes').hot(limit=100)
        if datetime.datetime.utcfromtimestamp(post.created_utc) >= hours_ago
    ]
    session = Session()
    new_posts = list(filter(lambda post: all(map(lambda p: p.id != post.id, session.query(Post).all())), new_posts))
    if len(new_posts) > 0:
        top_post = new_posts[0]
        post = Post(id=top_post.id)
        session.add(post)
        session.commit()
        session.close()
        twitterbot.post(top_post)
    else:
        sys.stderr.write("No new posts")
