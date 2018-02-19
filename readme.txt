python crawl
Reference:
https://stackoverflow.com/questions/7746832/scraping-and-parsing-google-search-results-using-python

beautifulsoup4
pip3.5 install beautifulsoup4

# Requirement
# Create text file passing list of texts
# format: text
# file name: list.txt

1. main.py 
# Reads a google link passing text from file as parameter
# Create a json file with:
# title, url, text
# file name: data.json

2. break_url.py
# 1. Read json file data.json

# 2. create json file with:
# format: domain_id, domain
# file name: domains.json

# 3. create a second json file with:
# domain, text, url
# file name: urls_text.json

3. most_common_words.py
# 1. Read json file (break_url.py) - <text_id+domain_id>.json

# 2. Create json file with list of words to be ignored:
# file name: ignore.json

# 2. Retrieve most common words used on the site (url). 
# Ignore words from item 2

# 3. create json file with:
# url_id, dictionary of common words - format: "word: number of occurrences"
# file name: <"most_common_words_"+url_id>.json
