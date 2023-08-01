trigger:
- main

pool:
  vmImage: ubuntu-latest
strategy:
  matrix:
    Python27:
      python.version: '3.0'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- script: |
    python -m pip install --upgrade pip
    pip install selenium
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |
    pip install pytest pytest-azurepipelines
    python new.py
  displayName: 'pytest'