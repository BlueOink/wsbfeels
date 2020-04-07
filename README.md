# wsbfeels

Outputs the percentage of people commenting "call" or "put" on r/wallstreetbets. 

Collects (most) positions commented and posted within 24 hours and saves it to a csv file to be parsed.

## Usage
 You gotta install praw and python and get reddit app auth stuff

 First run `python options.py`

 Then run `python create_post.py >> out.txt`
 
 This will create a file called out.txt that will be the exact text needed for the post on reddit. You can also parse it a different way by accessing positions.csv and dcomments.csv .
## Todo

- test if inverse wsb is profitable. Maybe even have a chart.

- scan submission titles

- improve accuracy

- get price of option at the time of creation, the see which plays were profitable and which one expired worthless

- detect sarcasm/stupidity

This is just for fun, not for profit. Just to collect and analyse data from r/wallstreetbets
