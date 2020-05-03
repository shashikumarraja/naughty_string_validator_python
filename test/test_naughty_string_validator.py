"""
Tests for `naughty_string_validator` module.
"""
from __future__ import unicode_literals

import sys
import os
import pytest
from builtins import str
import naughty_string_validator
from naughty_string_validator import *

class TestNaughty_string_validator(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_presence_of_db_files(self):
        assert len(os.listdir('naughty_string_validator/naughty_string_db')) == 2

    def test_function_names_of_naughty_string_validator(self):
        main_module = naughty_string_validator.__all__
        expected_list = ['get_naughty_string_list', 'get_emoji_list',
                         'get_random_naughty_string', 'get_random_emoji']
        assert all(x for x in expected_list for x in main_module)
        

    def test_len_of_naughty_string_list(self):
        assert len(get_naughty_string_list()) > 0
    
    def test_type_of_naughty_string_list(self):
        assert isinstance(get_naughty_string_list(), list)

    def test_len_of_emoji_list(self):
        assert len(get_emoji_list()) > 0

    def test_type_of_emoji_list(self):
        assert isinstance(get_emoji_list(), list)

    def test_type_of_random_naughty_string(self):
        assert isinstance(get_random_naughty_string(), str) == True

    def test_type_of_random_emoji(self):
        assert isinstance(get_random_emoji(), str) == True

    @classmethod
    def teardown_class(cls):
        pass
