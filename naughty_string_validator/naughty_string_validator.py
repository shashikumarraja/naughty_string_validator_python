import json
import random
import sys
import os

__all__ = ['get_naughty_string_list', 'get_emoji_list', 'get_random_naughty_string', 'get_random_emoji']

this_directory = os.path.dirname(__file__)

with open( os.path.join(this_directory, 'naughty_string_db/blns.json'), 'r') as f:
    naughty_string_list = json.loads(f.read())
    
with open( os.path.join(this_directory, 'naughty_string_db/emoji.json'), 'r') as f:
    emoji_list =json.loads(f.read())

def get_naughty_string_list():
    """ Get entire naughty string list """
    return naughty_string_list

def get_random_naughty_string():
    """ Get a random naughty string """
    return (random.choice(naughty_string_list)).encode('utf-8').decode('utf-8')

def get_emoji_list():
    """ Get entire emoji list """
    return list(map(lambda x: x.get('emoji'), emoji_list))

def get_random_emoji():
    """ Get a random emoji """
    return (random.choice(get_emoji_list())).encode('utf-8').decode('utf-8')
