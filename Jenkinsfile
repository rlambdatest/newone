
image: python:3.10

pipelines:
  default:
    - parallel:
      - step:
          name: Test
          caches:
            - pip
          script:
            - if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
            - pip install selenium
      - step:
          name: Lint code
          script:
            # Enforce style consistency across Python projects https://flake8.pycqa.org
            - pip install selenium
            - python new.py
              
