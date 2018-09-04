import json
import os
import random

SRC_DIRECTORY = os.path.dirname(__file__)


class NaughtyStringValidator(object):
    def __init__(self):
        with open(os.path.join(SRC_DIRECTORY, 'naughty_string_db/blns.json'), 'r') as f:
            self.naughty_string_list = json.loads(f.read())

        with open(os.path.join(SRC_DIRECTORY, 'naughty_string_db/emoji.json'), 'r') as f:
            self.emoji_list = json.loads(f.read())

    def get_naughty_string_list(self):
        """ Get entire naughty string list """
        return self.naughty_string_list

    def get_random_naughty_string(self):
        """ Get a random naughty string """
        return (random.choice(self.naughty_string_list)).encode('utf-8').decode('utf-8')

    def get_emoji_list(self):
        """ Get entire emoji list """
        return list(map(lambda x: x.get('emoji'), self.emoji_list))

    def get_random_emoji(self):
        """ Get a random emoji """
        return (random.choice(self.get_emoji_list())).encode('utf-8').decode('utf-8')
