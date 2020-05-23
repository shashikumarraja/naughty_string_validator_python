import sys
import json
import requests
from backports.configparser import ConfigParser

base_test_pypi_url = "https://test.pypi.org/pypi/naughty-string-validator/json"

def get_latest_nsv_version_from_pypi():
    res = requests.get(base_test_pypi_url)
    body = json.loads(res.text)
    releases = body.get('releases', {})
    latest_release = max([key for key in releases])
    return latest_release

def get_current_version_to_deploy():
    data_file = '.bumpversion.cfg'
    config = ConfigParser()
    config.read(data_file)
    current_version = config['bumpversion']['current_version']
    return current_version
    
def deploy():
    deployed_version = get_latest_nsv_version_from_pypi()
    current_version = get_current_version_to_deploy()
    if current_version > deployed_version:
        print(True)
        sys.exit(0)
    print(False)
    sys.exit(1)

if __name__ == "__main__":
    deploy()