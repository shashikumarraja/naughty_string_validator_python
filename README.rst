==========================================================
naughty_string_validator
==========================================================

.. image:: https://img.shields.io/pypi/v/naughty-string-validator.svg
      :target: https://pypi.python.org/pypi/naughty-string-validator/

.. image:: https://img.shields.io/pypi/pyversions/naughty-string-validator.svg
      :target: https://pypi.python.org/pypi/naughty-string-validator/

.. image:: https://travis-ci.org/shashikumarraja/naughty_string_validator_python.svg?branch=master
    :target: https://travis-ci.org/shashikumarraja/naughty_string_validator_python

.. image:: https://codecov.io/gh/shashikumarraja/naughty_string_validator_python/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/shashikumarraja/naughty_string_validator_python

.. image:: https://pyup.io/repos/github/shashikumarraja/naughty_string_validator_python/shield.svg
     :target: https://pyup.io/repos/github/shashikumarraja/naughty_string_validator_python/
     :alt: Updates
     
.. image:: https://pepy.tech/badge/naughty-string-validator
     :target: https://pepy.tech/project/naughty-string-validator
       
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
     :target: https://opensource.org/licenses/MIT
     

A python library that returns `naughty strings` from an offline database of `Big List of Naughty Strings <https://github.com/minimaxir/big-list-of-naughty-strings>`_ and emojis. The db will be continuously growing with each release.

The Big List of Naughty Strings is an evolving list of strings which have a high probability of causing issues when used as user-input data.

This library can be inluded in the test automation framework for API, UI, or DB testing to validate them against naughty strings.


Installation
*************
  pip install naughty_string_validator

Usage
***********
.. code-block:: python

    from naughty_string_validator import *

* To get a random naughty string from the list

.. code-block:: python

    print(get_random_naughty_string())

    #output
    "<a href=\"\\xE2\\x80\\x88javascript…(1)\" id=\"fuzzelement1\">test</a>"
  

* To get entire naughty string list 

.. code-block:: python

    print(get_naughty_string_list())

    #output
    ["", "undefined", "undef", "null", "NULL", "(null)", "nil", …]

* To get a random emoji from the emoji list

.. code-block:: python

    print(get_random_emoji())

    #output
    "😃"

* To get a entire emoji list
  
.. code-block:: python

    print(get_emoji_list())

    #output
    ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "☺️", "😊", …]

Tests
***********
* To run tests

    py.test --cov=naughty_string_validator test/ --verbose




