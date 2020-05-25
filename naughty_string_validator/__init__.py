__author__ = 'Shashi Kumar Raja'
__email__ = 'shashiraja92@gmail.com'
__version__ = '0.1.7'

from .utils import FileUtils    # noqa: F401
from .naughty_string_validator import Naughty
naughty = Naughty()
get_naughty_string_list = naughty.get_naughty_string_list
get_emoji_list = naughty.get_emoji_list
get_random_naughty_string = naughty.get_random_naughty_string
get_random_emoji = naughty.get_random_emoji
