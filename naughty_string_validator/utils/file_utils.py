import json
import io


class FileUtils:

    def __init__(self):
        pass

    def read_file(self, path):
        try:
            with io.open(path, 'r', encoding='utf8') as f:
                content = json.loads(f.read())
            return content
        except IOError as e:
            raise e
