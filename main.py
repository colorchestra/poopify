#!/usr/bin/python3

from textblob import TextBlob
import random
from twython import Twython, TwythonError
from mastodon import Mastodon

#### Twitter
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


#### Mastodon
mastodon_email = ''
mastodon_pw = ''
mastodon_address = ''

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret', api_base_url = mastodon_address)
mastodon.log_in(mastodon_email, mastodon_pw, to_file = 'pytooter_usercred.secret')
mastodon = Mastodon(access_token = 'pytooter_usercred.secret', api_base_url = mastodon_address)

# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
words_to_replace_singular = []
words_to_replace_plural = []
input_file = ''
output_sentence = '' 


with open(input_file) as file:
    text = file.readlines()

def poopify():
    blob = TextBlob(str(text))
    random_sentence = str(random.choice(blob.sentences))
    sentence_blob = TextBlob(random_sentence)
    print(sentence_blob.tags)

    for i in sentence_blob.tags:
        if i[1] == "NN":
            words_to_replace_singular.append(i[0])

    for i in sentence_blob.tags:
        if i[1] == "NNS":
            words_to_replace_plural.append(i[0])

    for word in words_to_replace_singular:
        random_sentence = random_sentence.replace(word, "poop")

    for word in words_to_replace_plural:
        random_sentence = random_sentence.replace(word, "poops")
    
    return random_sentence

    
output_sentence = poopify()

while "poop" not in output_sentence or len(output_sentence) > 280:
    output_sentence = poopify()


print(output_sentence)
twitter.update_status(status=output_sentence)
mastodon.toot(output_sentence)
