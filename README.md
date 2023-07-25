https://www.youtube.com/watch?v=s8XjEuplx_U&t=1s

To install packages
  pip install requests
It might error the first time, so try again
It will get the requests package from pypi (the python package index)
To check if it installed, go into python by typing this in the command line
  python
Then 
  import requests
It should just be blank, not ModuleNotFoundError
You can now exit with
  exit()

At the bottom it will say update pip, but when you try to update, it will say 
  ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'c:\\python311\\lib\\site-packages\\pip-22.3.1.dist-info\\entry_points.txt'      
  Consider using the `--user` option or check the permissions.

Next install beautiful soup 4 with
  pip install beautifulsoup4
check with
  import bs4

Another way to check packages
  pip list
But this won't show smptlib, email.mime, datetime so would have to manually check that out with import

A better way would be requirements.txt, then
  pip install -r requirements.txt

===========================================================
to run the programs, type the name of the file in the command line

For the ted_talk_downloader, have to supply a ted talk url as an argument.
  ted_talk_downloader https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection

==========================================================
Installed different types of jupyter so not sure which one is necessary. Installed the vs code extension, jupyter-lab, and jupyter.
To launch jupyter
  jupyter-lab

Installing dependencies for PDF table extraction was messy. Had to install 
  pip install opencv-python
and
  https://ghostscript.com/releases/gsdnld.html
and 
  https://platform.activestate.com/ActiveState/ActiveTcl-8.6
and
  pip install camelot-py 
as explained in 
  https://camelot-py.readthedocs.io/en/master/user/install-deps.html
other pdf libraries
  tabula, pdfplumber,pdftable, pdf-table-extract, but camelot the best. It outputs panda dataframe

seaborn is for data visualization


====================================================================================
# Build Tools to Automate Stuff in Python

6 Amazing Python Projects for Python beginners to build Tools 

Python Libraries that you'd end up using in these projects

* PIL (Pillow)
* requests
* BeautifulSoup
* camelot
* re
* PDFminer 
* gensim (Summarizer) 


Note: Google has changed the way less secure apps are handeld. It's critical for the Email Automation project in the course. I'm exploring possible alternatives for that. 

