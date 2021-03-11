"""
1. creat a google bot in google ahat room and get the webhook like next line
https://chat.googleapis.com/v1/spaces/AAAAKsw_d5E/messages?key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2. save webhook to credential
"""

from json import dumps

from httplib2 import Http

import read_yaml as ryaml

credential = "/Users/huangyiling/Github/credential/google_bot.yaml"

def main(message):
    """Hangouts Chat incoming webhook quickstart."""
    url = ryaml.read_yaml(credential)['test_bot']['webhook']
    bot_message = {'text' : message}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)


if __name__ == '__main__':
    main('OOOOOOOO')
