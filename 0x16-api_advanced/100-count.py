#!/usr/bin/python3
''' Get hot posts '''
import pprint
import re
import requests

url = 'http://reddit.com/r/{}/hot.json'


def count_words(subreddit, word_list, hot_list=[], after=None):
    ''' Get hot posts '''
    header = {'User-agent': 'tabbykatz-app3'}
    parameters_ = {'limit': 100}
    if isinstance(after, str):
        if after != "DONE":
            parameters_['after'] = after
        else:
            return print_it(word_list, hot_list)

    response = requests.get(url.format(subreddit),
                            headers=header, params=parameters_)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_it(word_list, hot_list):
    ''' print'''
    lst = {}
    for word in word_list:
        lst[word] = 0
    for title in hot_list:
        for word in word_list:
            lst[word] = lst[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))
    lst = {k: v for k, v in lst.items() if v > 0}
    unsorted_words = sorted(list(lst.keys()))
    for word in sorted(unsorted_words, reverse=True, key=lambda k: lst[k]):
        print("{}: {}".format(word, lst[word]))
