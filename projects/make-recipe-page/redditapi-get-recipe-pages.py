# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.
# -----------------------------------------------------------------------------
# Following along the basic steps with:
# https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/
# and
# https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
# and
# https://www.honchosearch.com/blog/seo/how-to-use-praw-and-crawl-reddit-for-subreddit-post-data/
# and
# https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

# Step 1: Bash "pip install praw" in a venv.

# Step 2: Fetch the login info (note will need to change '-' in redditapi-get-token.py to '_').
from redditapi_get_token import client_id, client_secret, username, password

# Step 3: Import praw.
import praw

# Step 4: Instantiate from the Reddit class as below:
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="MyBot/0.0.1", # From redditapi_get_token.py
    username=username,
    password=password,
)

# Step 5: Find submissions and each submission's title, url, author and text:

titles = []
urls = []
authors = []
text = []
for submission in reddit.subreddit("recipes").top(limit=50):
    # Check to make sure the submission has text:
    if submission.is_self:
        titles.append(submission.title)
        urls.append(submission.url)
        authors.append(submission.author)
        text.append(submission.selftext)

# Step 6: Write the necessary html code to input this data into a website.