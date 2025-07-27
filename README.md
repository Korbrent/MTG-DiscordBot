<a id="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Last Commit][last-commit-shield]][last-commit-url]
[![Coverage][coverage-badge]][coverage-url]
![Interrogate][interrogate-shield]
[![Contributors][contributors-shield]][contributors-url]
[![Unlicense License][license-shield]][license-url]
![Size][repo-size-shield]

<br />
<div align="center">
  <a href="https://github.com/Korbrent/MTG-DiscordBot">
    <!-- TODO <img src="https://some.image.site/cool_logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">MTG Discord Bot</h3>

  <p align="center">
    A small Discord bot providing utilities for the popular TCG Magic The Gathering.
    <br />
    <a href="https://korbrent.github.io/MTG-DiscordBot/"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup-guide">Setup Guide</a></li>
      </ul>
    </li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

# About the Project
Discord Bot for Magic the Gathering nerds everywhere to rejoice.

All development is facilitated through the Github Project or the development Discord channels.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Getting Started

## Prerequisites

- Python (Obviously)
- *tbd*
  -  [Scrython](https://github.com/NandaScott/Scrython) - Python library for accessing the Scryfall API
  -  [Pyrchidekt](https://github.com/linkian209/pyrchidekt) - Python library for accessing the Archidekt API

## Setup Guide

### Prerequisites

This project requires `dos2unix` for some pre-commit hooks.
```sh
sudo apt install -y dos2unix
```

### Configuring your Virtual Environment

First, let's create a virtual environment so we don't install the plugins to your global Python installation and risk version conflicts.

1. Create a new venv
```sh
python -m venv venv
```
2. Activate the venv
```sh
source venv/bin/activate
```

### Installing the necessary plugins
1. Install the necessary modules with poetry
```sh
poetry install
```
2. Congrats dude. You did it.

### Setting up pre-commit hooks
1. Run the pre-commit-hooks installer
```sh
pre-commit install --install-hooks
```
2. Build the package to generate additional data used by the pre-commit hooks.
```sh
python3 -m build
```
3. (Optional) Test the installation
```sh
poetry run pre-commit run --all-files
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Built With

* [Black][black-url]
* [Conventional-pre-commit][cpc-url]
* [Coverage][coverage-url]
* [Coverage-badge][coverage-badge-url]
* [Flake8][flake8-url]
* [Handsdown][hd-url]
* [Interactions.py][dci-url]
* [Interrogate][int-url]
* [Isort][isort-url]
* [MkDocs][mkdocs-url]
* [MyPy][mypy-url]
* [Pre-commit-hooks][pch-url]
* [Pydocstyle][pds-url]
* [Pyrchidekt][pyrchidekt-url]
* [Pyroma][pyroma-url]
* [PyTest][pytest-url]
* [Scrython][scrython-url]
* [Xenon][xenon-url]

# License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contact
Korbin Shelley - [@Kor](https://discord.com/users/189871577783861258) - kortheshells@gmail.com
Brenton Candelaria - [@HyPerNT](https://discord.com/users/198554971954872320) - brentoncandelaria@gmail.com
Richard Duran - [@MoodyPDuck](https://discord.com/users/337704272697229313) - richduran13@gmail.com

Project Link: [https://github.com/Korbrent/MTG-DiscordBot](https://github.com/Korbrent/MTG-DiscordBot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[last-commit-shield]: https://img.shields.io/github/last-commit/Korbrent/MTG-DiscordBot
[last-commit-url]: https://github.com/Korbrent/MTG-DiscordBot/commits/main/
[contributors-shield]: https://img.shields.io/github/contributors/KorBrent/MTG-DiscordBot
[contributors-url]: https://github.com/Korbrent/MTG-DiscordBot/graphs/contributors
[license-shield]: https://img.shields.io/github/license/Korbrent/MTG-DiscordBot
[license-url]: https://github.com/Korbrent/MTG-DiscordBot/blob/main/LICENSE
[interrogate-shield]: ./badges/interrogate.svg
[repo-size-shield]: https://img.shields.io/github/languages/code-size/Korbrent/MTG-DiscordBot

<!-- Links to packages in the repo -->
[pytest-url]: https://docs.pytest.org/en/stable/
[black-url]: https://github.com/psf/black
[pch-url]: https://github.com/pre-commit/pre-commit-hooks
[flake8-url]: https://flake8.pycqa.org/en/latest/
[mypy-url]: https://mypy-lang.org
[xenon-url]: https://pypi.org/project/xenon/
[pyroma-url]: https://pypi.org/project/pyroma/
[int-url]: https://interrogate.readthedocs.io/en/latest/
[pds-url]: https://www.pydocstyle.org/en/stable/
[hd-url]: https://github.com/vemel/handsdown
[coverage-url]: https://coverage.readthedocs.io/en/7.9.1/
[coverage-badge-url]: https://pypi.org/project/coverage-badge/
[coverage-badge]: badges/coverage.svg
[mkdocs-url]: https://www.mkdocs.org
[dci-url]: https://github.com/interactions-py
[pyrchidekt-url]: https://github.com/linkian209/pyrchidekt
[scrython-url]: https://github.com/NandaScott/Scrython
[cpc-url]: https://github.com/compilerla/conventional-pre-commit
[isort-url]: https://pycqa.github.io/isort/
