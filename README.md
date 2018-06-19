# TwitterBot

<h3>Get started</h3>

<p>Set up your api keys in the projects root</p>

```python3
# secret_keys.py


# Copy your Reddit keys here
client_id = ''
client_secret = ''

# Copy your Twitter keys here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

<h3>Set up and activate your virtual environment</h3>

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

<h3>Initialize your bot</h3>

<p>Select the subreddit you want to retrieve posts from and initialize your bot account</p>

```sh
python3 main.py init <your-subreddit>
```

<h3>Start posting</h3>

<p>Run the script. As parameters you should provide the subreddit your bot posts from, and an additional interval parameter your bot uses between the posts. Interval is given in seconds, and it has a default value of 1800 (30 minutes).</p>

```sh
python3 main.py <subreddit> [<interval>]
```
