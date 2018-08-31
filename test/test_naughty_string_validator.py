"""
Tests for `naughty_string_validator` module.
"""
import pytest

from naughty_string_validator import get_naughty_string_list


class TestNaughty_string_validator(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        assert len(get_naughty_string_list()) > 0

    @classmethod
    def teardown_class(cls):
        pass
