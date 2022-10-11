"""
Tests for `naughty_string_validator` module.
"""
from __future__ import unicode_literals

import sys
import os
import pytest
from builtins import str
from naughty_string_validator import *

class TestNaughty(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_presence_of_db_files(self):
        assert len(os.listdir('naughty_string_validator/naughty_string_db')) == 2
        
    def test_len_of_naughty_string_list(self):
        assert len(get_naughty_string_list()) > 0
    
    def test_type_of_naughty_string_list(self):
        assert isinstance(get_naughty_string_list(), list)

    def test_len_of_emoji_list(self):
        assert len(get_emoji_list()) > 0

    def test_type_of_emoji_list(self):
        assert isinstance(get_emoji_list(), list)

    def test_type_of_random_naughty_string(self):
        assert isinstance(get_random_naughty_string(), str)

    def test_type_of_random_emoji(self):
        assert isinstance(get_random_emoji(), str)

    @classmethod
    def teardown_class(cls):
        pass
