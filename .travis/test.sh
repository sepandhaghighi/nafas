#!/bin/bash
  set -e
  set -x
  IS_IN_TRAVIS=false
  PYTHON_COMMAND=python
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
	PYTHON_COMMAND=python3
  fi
  $PYTHON_COMMAND -m pytest test --cov=nafas --cov-report=term
  $PYTHON_COMMAND otherfiles/version_check.py
  
  if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
  then
      IS_IN_TRAVIS=true
  fi

  if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      $PYTHON_COMMAND -m vulture nafas/ setup.py --min-confidence 65 --exclude=__init__.py --sort-by-size
      $PYTHON_COMMAND -m bandit -r nafas -s B311
      $PYTHON_COMMAND -m pydocstyle --match-dir=nafas -v
  fi

