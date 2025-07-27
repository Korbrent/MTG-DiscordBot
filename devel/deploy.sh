#!/bin/bash

# Pull latest refs from main and build docs
git checkout main && git pull
handsdown --external `git config --get remote.origin.url` -o docsmd -n <PROJECT> --theme=material
python3 -m mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
