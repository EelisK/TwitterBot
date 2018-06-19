#!./venv/bin/python3
from util import set_interval, update, init_profile
import sys


subreddit = 'DeepFriedMemes'
update_rate = 1800


def start(n):
    """
    :param n: update the twitter account every n seconds
    """
    print("Posting from {} every {} {}".format(subreddit,
                                               int(update_rate / 60) if update_rate >= 60 else update_rate,
                                               "minutes" if update_rate >= 60 else "seconds"))
    set_interval(update, n, subreddit)


def main():
    global update_rate, subreddit
    if len(sys.argv) == 3 and sys.argv[1].lower() == "init":
        init_profile(sys.argv[2])
        return
    elif len(sys.argv) > 1:
        try:
            update_rate = int(sys.argv[1])
        except ValueError:
            subreddit = sys.argv[1]
            if len(sys.argv) > 2:
                update_rate = int(sys.argv[2])
    # At least 10 seconds update rate so that there will be
    # enough time to finish the previous fetching and posting
    update_rate = max(update_rate, 10)
    start(update_rate)


main()
