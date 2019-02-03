import codecs
import pickle
import re
from collections import Counter

import gensim
import numpy as np

print ('Loading the model...')
model = gensim.models.KeyedVectors.load_word2vec_format('/home/parisa/projects/models/GoogleNews-vectors-negative300.bin', binary = True)
print ('Loaded the model!')
data_path = '/home/parisa/projects/txt_img/MatchPyramid-for-semantic-matching/data/amazon/'
train_file = codecs.open(data_path + 'amazon_train.txt', 'w', encoding='utf8')
user_text_file = codecs.open(data_path + 'amazon_user_text.txt', 'w', encoding='utf8')
item_text_file = codecs.open(data_path + 'amazon_item_text.txt', 'w', encoding='utf8')
word2vec_file = codecs.open(data_path + 'word2vec.txt', 'w', encoding='utf8')
test_wv_file = codecs.open(data_path + 'test_wv.txt', 'w', encoding='utf8')

train_file.write('label q1 q2\n')
user_text_file.write('qid words\n')
word_index = 0

regex = re.compile('[,\.!?]')

vocab = {}

dict = Counter()


def save_profile_word(word, profile_file):
    profile_file.write(str(vocab[word]) + '(' + word + ')' + ' ')


def process_word_embedding(file, word):
    if file is not None:
        global word_index
        word_vec = model[word]
        if word not in vocab:
            vocab[word] = word_index
            word_index += 1
            file.write(str(vocab[word]) + ' ')
            for e in word_vec:
                file.write(str(e) + ' ')
            file.write('\n')


def get_match(user_id, item_id, rating):
    train_file.write(str(rating) + ' ' + user_id + ' ' + item_id + '\n')


def get_profile_text(profile_id, text_list, profile_file, wv_file = None):
    # user_text_file.write(user_id + ' ')
    print (profile_id)
    print (len(text_list))
    # for text in text_list:
    all_text = ' '.join(text_list)
    all_text = regex.sub(' ', all_text)
    words = all_text.strip().split()
    words = [w.lower() for w in words]

    dict.update(words)

    profile_file.write(profile_id + ' ')
    for word in words:
        if word in model.wv.vocab:
            process_word_embedding(wv_file, word)
            save_profile_word(word, profile_file)

    profile_file.write('\n')


# def process_profile_text(profile_id, text_list):
#     for text in text_list:
#         text = regex.sub(' ', text)
#         words = text.strip().split()
#
#         for word in words:
#             save_profile_word(word)
#     user_text_file.write('\n')








print ('Loading data...')

input = open('resources/incomplete_data.pkl', 'rb')
user_dict = pickle.load(input)
item_dict = pickle.load(input)

print ('Loaded data!')

users = user_dict.get_dict()

print ('Started users...')
for user in users:
    for index in range(user.num_of_reviews()):
        review_text, rating, item_id = user.get_review_details(index)
        # item = item_dict.get_profile(item_id)
        user_id = user.profile_id
        # item_id = item.profile_id
        get_match(user_id, item_id, rating)

        get_profile_text(user_id, user.text_list, user_text_file, wv_file = word2vec_file)
        # get_profile_text(item.text_list)

    # break

items = item_dict.get_dict()

for item in items:
    get_profile_text(item.profile_id, item.text_list, item_text_file)


sum = 0

for w, count in dict.most_common():
    print (w + ' ' + str(count))
    if w in model.wv.vocab:
        sum +=1

print ('vocab size:\n')
print (sum)

print ('____________')