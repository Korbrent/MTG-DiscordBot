# MTG-DiscordBot
Discord Bot for Magic the Gathering nerds everywhere to rejoice. 

All development is facilitated through the Github Project or the development Discord channels. 

# Requirements

- Python (Obviously)
- **Python Libraries**:
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/) - Used to read in the `.env` file
- **TBD Python Libs**:
  - [`Scrython`](https://github.com/NandaScott/Scrython) - Python library for accessing the Scryfall API
  - [`Pyrchidekt`](https://github.com/linkian209/pyrchidekt) - Python library for accessing the Archidekt API

# Setup Guide

## Configuring your Virtual Environment

First, let's create a virtual environment so we don't install the plugins to your global Python installation and risk version c onflicts.

1. Create a new venv `python -m venv venv`
2. Activate the venv `./venv/Scripts/activate`

## Installing the necessary plugins
1. Install the necessary plugins with pip. `pip install -r requirements.txt --upgrade`
2. Congrats dude. You did it.