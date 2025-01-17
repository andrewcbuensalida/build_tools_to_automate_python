import requests #getting content of the TED Talk page

from bs4 import BeautifulSoup #web scraping

import re #Regular Expression pattern matching

# from urllib.request import urlretrieve #downloading mp4

import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

#url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"

#url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml") # had to install lxml with pip for this to work

result = None

for val in soup.findAll("script"):
    if re.search("talkpage",str(val)) is not None: # take out .init from talkpage.init because ted.com changed their html
        result = str(val)

if result is None:
    raise Exception("Could not find script tag containing the mp4")

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group()

if result_mp4 is None:
    raise Exception("Could not find mp4 in the script tag")

print("This is result_mp4", result_mp4)

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..... " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ..... " + file_name)


r = requests.get(mp4_url)

with open(file_name,'wb') as f:
  f.write(r.content)

# Alternate method
#urlretrieve(mp4_url,file_name)

print("Download Process finished")

