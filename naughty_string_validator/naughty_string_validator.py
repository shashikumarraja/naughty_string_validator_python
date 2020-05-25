import random
import os
from .utils import FileUtils


class Naughty:

    def __init__(self):
        self.file_utils = FileUtils()
        self.dir = os.path.dirname(__file__)
        self.naughty_string_list = self.file_utils.read_file(
            os.path.join(self.dir, 'naughty_string_db/blns.json'))
        self.emoji_list = self.file_utils.read_file(
            os.path.join(self.dir, 'naughty_string_db/emoji.json'))

    def get_naughty_string_list(self):
        """ Get entire naughty string list """
        return self.naughty_string_list

    def get_random_naughty_string(self):
        """ Get a random naughty string """
        return random.choice(self.naughty_string_list)

    def get_emoji_list(self):
        """ Get entire emoji list """
        return [emoji.get('emoji', '') for emoji in self.emoji_list]

    def get_random_emoji(self):
        """ Get a random emoji """
        return random.choice(self.get_emoji_list())
