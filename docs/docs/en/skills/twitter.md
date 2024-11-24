# Twitter Skill

The Twitter skill provides functionality for interacting with the Twitter (X) API. It allows you to make tweets, create polls, reply to tweets, and post tweets with images.

## Methods

### make_tweet

Makes a simple text tweet.

**Parameters:**
- `content` (str): The content of the tweet to be made

**Returns:** String confirming tweet was submitted

### make_tweet_with_image

Makes a tweet containing both text and an image.

**Parameters:**
- `content` (str): The content of the tweet to be made
- `image_url` (str): URL of the image to include in the tweet

**Returns:** String confirming tweet was submitted

### make_poll

Creates a Twitter poll.

**Parameters:**
- `content` (str): The content/question for the poll
- `duration_minutes` (int): How long the poll should run for in minutes
- `options` (list[str]): List of poll options for users to vote on

**Returns:** String confirming poll was created

### reply_to_tweet

Replies to an existing tweet.

**Parameters:**
- `tweet_id` (int): The ID of the tweet to reply to
- `content` (str): The content of the reply tweet

**Returns:** String confirming reply was submitted with the tweet ID
