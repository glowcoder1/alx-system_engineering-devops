#!/usr/bin/python3
""" count_words function """
from requests import get


def count_words(subreddit, word_list, count=[], after=None):
    """
   queries the Reddit API, parses the title of all hot articles,
   and prints a sorted count of given keywords
    """
    headers = {'User-Agent': 'Custom'}

    word_list = [word.lower() for word in word_list]

    if bool(count) is False:
        for word in word_list:
            count.append(0)

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        req = get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            for child in req.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            count[i] += 1
                    i += 1

            if req.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            count, req.json()['data']['after'])
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
        req = get(url, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            for child in req.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            count[i] += 1
                    i += 1
            if req.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            count, req.json()['data']['after'])
            else:
                dict = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if count[i] != 0:
                        dict[word_list[i]] = (
                            count[i] * word_list.count(word_list[i]))

                for key, value in sorted(dict.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))
