# Web Services and Applications - Assignments
Module: Web Services and Applications  
Course: ATU HDip in Computing in Data Analytics  
Lecturer: Andrew Beatty <br>
Student: Eilis Donohue (G00006088)


## Content   

The weekly assignment for the Web Services and Applications module. These were as follows:

**assignment2-carddraw.ipynb** <br>
Look at the the page Deck of Cards API    https://deckofcardsapi.com/
This is an API that simulates dealing a deck of cards
Write a program that "deals" (prints out) 5 cards

From there you need to print the value and the suit of each card.

save the file as assignment2-carddraw.py (or as a notebook)

Last few marks:
Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

**assignment03-cso.py** <br>
Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

Upload this program to the same repository you used for the first assignment
Save this assignment as "assignment03-cso.py"
I don't need you to reformat or analyse the data in any way
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators.

**assignment04-github.py** <br>
Write a program in python that will read a file from a repository, 

The program should then replace all the instances of the text "Andrew" with your name. 

The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

I do not need to see your keys.


## Repository Contents

- assignment2-carddraw.ipynb <br>
- assignment03-cso.py <br>
- assignment04-github.py <br>
- cso.json (json file created from the CSO API) <br>
- config.py (hidden file for access to a private github repository used in assignment04) <br>


## Requirements  

A full list of all packages and versions are given in the [requirements.txt](requirements.txt) file. 

## Using the Repository

The notebooks can be run in two ways:

  1. On your local machine using [Visual Studio Code](https://code.visualstudio.com/) and [Anaconda](https://www.anaconda.com/download).
  2. Instantly online using [Github Codespaces](https://github.com/features/codespaces).


### Option 1: Run Locally (VS Code + Anaconda)

  1. Clone the repository to your local machine: <br>
  ```git clone https://github.com/Eilis9/WSAA-coursework.git```
  ```cd WSAA-coursework```
  2. Set up a virtual environment using Anaconda: <br>
  ```conda create -n wsaa_assignment python=3.9``` <br>
  ```conda activate wsaa_assignment``` <br>
  ``` pip install -r requirements.txt``` <br>
  3. Launch Visual Studio Code (VS Code) <br>
    - Open the repository folder in VS Code
    - Install the Python extension if prompted
    - Select the wsaa_assignment environment as the Python interpreter
  4. Run the Jupyter Notebooks (where relevant): <br>
    - Open the notebook file (assignment2-carddraw.ipynb) or python file in VS Code
    - Use the integrated Jupyter Notebook interface to run the cells or terminal in VS Code

### Option 2: Run using Github Codespaces

  1. Click on the green "Code" button and select "Open with Codespaces". <br>
  2. The repository will open in a Codespace in your browser.<br>
  3. Open the Jupyter Notebook or python file by clicking on the file name in the file list.<br>
 

## Prerequisites
- For local setup, ensure Anaconda or Miniconda is installed. See download link above.
- Familiarity with Jupyter Notebook is recommended but not essential.

## References

1. Geeksforgeeks.org (2024) response.json() - Python requests [Online] Available: https://www.geeksforgeeks.org/response-json-python-requests/
2. Stack Overflow (2002) How do I read image data from a URL in Python? [Online] Available:https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
3. Ipyplot https://github.com/karolzak/ipyplot
4. deckofcardsapi.com API Documentation [Online] Available: https://deckofcardsapi.com/
5. CSO (2025) [Online] Historic exchequer https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en
6. Geeksforgeeks.org - JSON dumps [Online] Available: # https://www.geeksforgeeks.org/json-dump-in-python/
7. Stack Overflow (2010) - Case insensitive replace [Online] Available: https://stackoverflow.com/questions/919056/case-insensitive-replace



## Notes
This repository was created by Eilis Donohue for the Web Services and Applications module as part of the Higher Diploma in Computing in Data Analytics at ATU. All content is original unless otherwise stated. Solutions and code snippets are based on the course material and personal research and the creator takes no responsibility for any errors or omissions.
In the event of any issues, please contact the repository owner. All feedback and comments are welcome.

