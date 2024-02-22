import requests
import yaml

import statistics

config = yaml.safe_load(open('config.yml'))
url = config['url']


def publish():
    body = statistics.stats

    res = requests.post(url, json=body)
    print(res.text)


def main():
    statistics.init_stats()
    publish()


if __name__ == '__main__':
    main()
