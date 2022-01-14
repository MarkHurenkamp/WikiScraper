Wikipedia scraper
============================

Basic demonstration of how to scrape tables from Wikipedia (and most other websites) using Selenium.


## How to use:
in `main.py`,  edit the following line to the URL of the wikipedia page you'd like to scrape:

> WEBSITE = "https://en.wikipedia.org/wiki/SQL"<br>

Then execute `main.py` and any table from the given page will be exported in a separate csv. 

## Example:

The English wikipedia page for [SQL](https://en.wikipedia.org/wiki/SQL) has two tables at the time of writing:

*Table1:*
![image](https://user-images.githubusercontent.com/90369156/149567652-6c0116d4-7fdc-4927-8d39-00755a1fbdd7.png)

*Table2:*
![image](https://user-images.githubusercontent.com/90369156/149567948-406cd160-b670-4e60-8c31-e2e68bc58f90.png)

After running main.py, you get the following outputs:

![image](https://user-images.githubusercontent.com/90369156/149568408-074ba4c7-acc0-43f6-88fc-97f7e228e729.png)



## Requirements:
- Firefox (tested with 95.0.2, 64bit)
- geckodriver - v0.30.0 (2021-09-16) is included, latest version can be downloaded from [Mozilla's github account](https://github.com/mozilla/geckodriver/)
- [requirements.txt](requirements.txt) - install with `pip install -r "requirements.txt"`
