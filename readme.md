Wikipedia scraper
============================

Basic demonstration of how to scrape tables from Wikipedia (and most other websites) using Selenium.


## How to use:
in `main.py`,  edit the following line to the URL of the wikipedia page you'd like to scrape:

> WEBSITE = "https://en.wikipedia.org/wiki/SQL"<br>

Then execute `main.py` and any table from the given page will be exported in a separate csv. 

## Requirements:
- Firefox (tested with 95.0.2, 64bit)
- geckodriver - v0.30.0 (2021-09-16) is included, latest version can be downloaded from [Mozilla's github account](https://github.com/mozilla/geckodriver/)
- [requirements.txt](requirements.txt) - install with `pip install -r "requirements.txt"`
