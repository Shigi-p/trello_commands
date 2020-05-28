#!usr/bin/env python3
# _*_ coding: utf8 _*_

import os
import urllib.request
import json

if __name__ == "__main__":
    api_key = os.environ['TRELLO_API_KEY']
    token = os.environ['TRELLO_TOKEN']
    my_board = ""

    board_list_url = 'https://trello.com/1/members/toshikishigihara/boards?key=' + \
                     api_key + '&token=' + \
                     token + '&fields=name'

    try:
        with urllib.request.urlopen(board_list_url) as response:
            board_list = json.loads(response.read())

            for board in board_list:
                if board['name'] == "個人的なやつ":
                    my_board = board['id']

    except urllib.error.URLError as e:
        print(e.reason)

    board_url = 'https://trello.com/1/boards/' + \
                my_board + '/lists?key=' + \
                api_key + '&token=' + \
                token + '&fields=name'

    try:
        with urllib.request.urlopen(board_url) as response:
            body = json.loads(response.read())

            print(body)

    except urllib.error.URLError as e:
        print(e.reason)
