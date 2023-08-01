# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "main" ]
  

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        pip install selenium
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
    - name: Test with pytest
      run: |
        python new.py
