"""
Tests for `utils` module.
"""
import os
import pytest
from naughty_string_validator.utils import FileUtils

class TestFileUtils(object):
    @classmethod
    def setup_class(cls):
        cls.file_utils = FileUtils()
        cls.dir = os.path.dirname(__file__)

    def test_read_file_with_invalid_path(self):
        invalid_path = "xy.json"
        with pytest.raises(IOError):
            response = self.file_utils.read_file(invalid_path)

    def test_read_file_with_valid_path(self):
        valid_path = "../naughty_string_validator/naughty_string_db/blns.json"
        response = self.file_utils.read_file(os.path.join(self.dir, valid_path))
        assert response is not None