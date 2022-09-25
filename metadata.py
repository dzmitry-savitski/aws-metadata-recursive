#!/usr/bin/env python3
import requests


def main():
    token = get_token()
    read_metadata('http://169.254.169.254/latest/meta-data/', token)


def read_metadata(path, token):
    response = requests.get(path, headers={'X-aws-ec2-metadata-token': token})

    if response.status_code == 200:
        print(path)
        print(response.text)
        print('-' * 100)
        for line in response.text.splitlines():
            read_metadata(path.rstrip('/') + '/' + line, token)


def get_token():
    response = requests.put('http://169.254.169.254/latest/api/token',
                            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'})
    return response.text


if __name__ == '__main__':
    main()
