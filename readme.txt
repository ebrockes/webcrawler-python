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
# 3. List words that: 
# 3.1. probably will appear in web sites related
# 3.2. show that the specific site is not related
# format: text: list of words ok : list of words not ok
# file name: words.txt


1. main.py 
# Reads a google link passing text from file as parameter
# Create a json file with:
# url, titulo, text
# file name: data.json

2. break_url.py
# 2.1. Read json file data.json
# 2.2 create json file with:
# format: domain_id, domain
# file name: domains.json
# 2.3. create a second json file with: (TODO)
# text -> list of domain
# domain -> list of (url, title)
# file name: urls.json
# 2.4. erase data.json

TODO 3. words.py
# 3.1. Read json file urls.json
# 3.2. Read file with words to be considered
# 3.3. Evaluate occurrences of specific word on url:
# 3.4. Create json file with:
# url, list of word and number of ocurrences
# file name: words.json

TODO 4. find_identification.py
#TODO names, phone numbers, emails on the web sites

TODO 5. dashboard
#TODO - web application


