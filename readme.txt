python crawl
Reference:
https://stackoverflow.com/questions/7746832/scraping-and-parsing-google-search-results-using-python

beautifulsoup4
pip3.5 install beautifulsoup4

# Requirement
# 1. Create text file passing list of texts
# format: text
# file name: list.txt
# 2. Create text file passing list of words to be ignored
# format: word
# file name: ignore.txt
# 3. List video web sites to be ignored on word count
# format: domain
# file name: ignore_domain.txt


1. main.py 
# Reads a google link passing text from file as parameter
# Create a json file with:
# title, url, text
# file name: data.json

2. break_url.py
# 2.1. Read json file data.json
# 2.2 create json file with:
# format: domain_id, domain
# file name: domains.json
# 2.3. create a second json file with:
# domain, text, url
# file name: urls.json

3. most_common_words.py
# 3.1. Read json file urls.json
# 3.2. Read file with words to be ignored
# 3.3. Read file with sites do be ignored
# file name: ignore.json
# 3.3. Retrieve most common words used on the site (url). 
# Do not do this if in 3.3
# Ignore words from item 2
# 3.4. create json file with:
# domain, text, url, dictionary of words and occurrencies
# file name: words.json
