"""
Tests for `naughty_string_validator` module.
"""
import sys
import os
import pytest

from naughty_string_validator import *

class TestNaughty_string_validator(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_presence_of_db_files(self):
        assert len(os.listdir('naughty_string_validator/naughty_string_db')) == 2

    def test_function_names_of_naughty_string_validator(self):
        main_module = naughty_string_validator.__all__
        assert 'get_naughty_string_list' in main_module and 'get_emoji_list' in main_module and 'get_random_naughty_string' in main_module and 'get_random_emoji' in main_module

    def test_len_of_naughty_string_list(self):
        assert len(get_naughty_string_list()) > 0
    
    def test_type_of_naughty_string_list(self):
        assert type(get_naughty_string_list()) is list

    def test_len_of_emoji_list(self):
        assert len(get_emoji_list()) > 0

    def test_type_of_emoji_list(self):
        assert type(get_emoji_list()) is list

    def test_type_of_random_naughty_string(self):
        assert type(get_random_naughty_string()) is str

    def test_type_of_random_emoji(self):
        assert type(get_random_emoji()) is str

    @classmethod
    def teardown_class(cls):
        pass
