# LinkedIn Learning Downloader

#### This is largely based on [Jatin Patel's work](https://github.com/J3Patel/linkedin-learning-video-downloader) with some minor changes and additions.


Asynchronous scraping tool to fetch LinkedIn's Learning Course Library. The script fetches an entire course along with its (if any) exercise files.

**Dependencies:**
- Python 3.6
- aiohttp
- lxml

#### Info

This script was written for educational usage only and should be used **ONLY** for personal purposes. **DO NOT SHARE THE VIDEOS.**

And make sure your LinkedIn account is **NOT** protected with 2FA.

#### Usage

Create a virtual environment with Python 3.

> pip install -r requirements.txt

Edit config.py file and substitue USERNAME and PASSWORD with your LinkedIn credentials.

In `COURSES = ['']` add a desired course slug name.  

```Course's slug can be obtained using its url
e.g:
COURSE URL: https://www.linkedin.com/learning/python-essential-training-2
->
SLUG: python-essential-training-2
```
Finally, run the script with:

> python3 linkedin_video_downloader.py

PS. Use responsibly.