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

<h3>Start posting</h3>

<p>Run the script. You can provide an interval as 
an additional parameter. This will be the interval your bot uses to update your twitter account.
Interval is given in seconds, the default being 1800 (30 minutes).</p>

```sh
python3 main.py [interval]
```
