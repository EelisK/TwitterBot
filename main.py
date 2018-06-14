#!./venv/bin/python3
from util import set_interval, update_memes
import sys


def main(n):
    """
    :param n: update the twitter account every n seconds
    """
    set_interval(update_memes, n)


if len(sys.argv) > 1:
    update_rate = int(sys.argv[1])
else:
    # Default is every hour
    update_rate = 6000

# At least 10 seconds update rate so that there will be
# enough time to finish the previous fetching and posting
update_rate = max(update_rate, 10)


main(update_rate)
