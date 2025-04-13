# Using Github API
# Eilis Donohue

# Import packages and file containing key
from github import Github
from config import config as cfg
import requests
import re

# Pass the token to the github api
apikey = cfg["lab5-token"]
g = Github(apikey)

# Get the repo
repo = g.get_repo("Eilis9/lab5")
print(repo)

# Get the url of the required file
fileInfo = repo.get_contents("ass4.txt")
url_of_file = fileInfo.download_url

# Get file contents
response = requests.get(url_of_file)
contents_of_file = response.text

# https://stackoverflow.com/questions/919056/case-insensitive-replace [7]
# Case insensitive replace of word
reg_exp = re.compile(re.escape('andrew'), re.IGNORECASE)
new_contents = reg_exp.sub('Eilis', contents_of_file)

# Write the new contents with Andrew replaced to the file
repo.update_file(fileInfo.path, "Replace 'Andrew'", new_contents, fileInfo.sha)

