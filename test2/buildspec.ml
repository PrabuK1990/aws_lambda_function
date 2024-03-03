version: 0.2
phases:
  install:
    runtime-versions:
      python: 3.7
  build:
    commands:
      - pip install --upgrade awscli
      - python -m unittest discover tests
artifacts:
  files:
    - '**/*'