# masonry-api
Basic API using `instagrapi` and `flesk` packages in python.
It has one endpoint to get media from an user from Instagram and it will return an array of pictures.

# Requirements
Python 3.8.0

## Install
pip install -r requirements.txt

# How to use
Endpoint:
`http://127.0.0.1:5000/getInstagramMediaByUsername/<igUsername>/<qtyMedia>`

# How to run
local: `py masonry.py`
host linux: `gunicorn app:masonry`
