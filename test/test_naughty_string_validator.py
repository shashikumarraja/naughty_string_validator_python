"""
Tests for `naughty_string_validator` module.
"""
from __future__ import unicode_literals

import os
from builtins import str

from naughty_string_validator import NaughtyStringValidator, SRC_DIRECTORY


class TestNaughtyStringValidator(object):

    @classmethod
    def setup_class(cls):
        cls.string_validator = NaughtyStringValidator()
        pass

    def test_presence_of_db_files(self):
        assert len(os.listdir(os.path.join(SRC_DIRECTORY, 'naughty_string_db'))) == 2

    def test_function_names_of_naughty_string_validator(self):
        main_module = self.string_validator.__dir__()
        assert 'get_naughty_string_list' in main_module
        assert 'get_emoji_list' in main_module
        assert 'get_random_naughty_string' in main_module
        assert 'get_random_emoji' in main_module

    def test_len_of_naughty_string_list(self):
        assert len(self.string_validator.get_naughty_string_list()) > 0

    def test_type_of_naughty_string_list(self):
        assert type(self.string_validator.get_naughty_string_list()) is list

    def test_len_of_emoji_list(self):
        assert len(self.string_validator.get_emoji_list()) > 0

    def test_type_of_emoji_list(self):
        assert type(self.string_validator.get_emoji_list()) is list

    def test_type_of_random_naughty_string(self):
        assert isinstance(self.string_validator.get_random_naughty_string(), str)

    def test_type_of_random_emoji(self):
        assert isinstance(self.string_validator.get_random_emoji(), str)

    @classmethod
    def teardown_class(cls):
        pass
