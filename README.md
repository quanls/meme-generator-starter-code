# Meme Generator
Generating a memes by stacking quotes over images.

## Overview and Modules
The project driving executors are:
- The Quote Engine that collects quotes from multiple file types and return quote details as a Quote Object.
- The Meme Engine that takes a random Quote objects and stacks its details on an image.
- The user can provide his own custom meme image and quote and a meme will be created via a CLI (command line interface) or a web service app.

## Setup
To set up the project we need the following:
1. Clone the repo on your local machine by running the command:
```
git clone git@github.com:quanls/meme-generator-starter-code.git
```

2. Install the xpdf tool on your system by [downloading](https://www.xpdfreader.com/download.html) the proper version for it and adding the path for the proper bin file to your system environment varibles. This is to collect quotes from PDF files.

3. Create a new python environment for the project by running one of the following commands on your terminal.
```
python -m venv .memeenv
```

If the command result told that you need to install python venv, please follow the instruction from the command then re-run the command again

4. Activate your environment by running one of the following commands in your terminal.
```
.memeenv/bin/activate
```

5. Install the required packages by running the following command:
```
pip install -r requirements.txt
```


## Terminal Examples
Once all the setup is done, please make sure that you are in `src` folder, then you can run the follwing example in your terminal
```
python meme.py
```
and it will generate a random meme for you.

You can also generate your custom meme but you need to understand how to do it in the terminal first. You can run
```
python meme.py -h
```
and it will handle your needs.

You can start the server by calling the below command in terminal window
```
python app.py
```
