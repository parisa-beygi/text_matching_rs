import codecs
import pickle
import gensim
import numpy as np

print ('Loading the model...')
model = gensim.models.KeyedVectors.load_word2vec_format('/home/parisa/projects/models/GoogleNews-vectors-negative300.bin', binary = True)
print ('Loaded the model!')
data_path = '/home/parisa/projects/txt_img/MatchPyramid-for-semantic-matching/data/amazon/'
train_file = codecs.open(data_path + 'amazon_train.txt', 'w', encoding='utf8')
user_text_file = codecs.open(data_path + 'amazon_user_text.txt', 'w', encoding='utf8')
word2vec_file = codecs.open(data_path + 'word2vec.txt', 'w', encoding='utf8')

train_file.write('label q1 q2\n')
user_text_file.write('qid words\n')
word_index = 0

def get_match(user_id, item_id, rating):
    train_file.write(str(rating) + ' ' + user_id + ' ' + item_id + '\n')


def get_profile_text(user_id, text_list):
    # user_text_file.write(user_id + ' ')
    for text in text_list:
        for word in text:
            word_vec = model[word]

            # get the word's embedding and save it to word2vec along with the word's id
            word2vec_file.write(word_index + ' ')
            np.savetxt(word2vec_file, word_vec, delimiter=' ')
            word2vec_file.write('\n')

            # append to the word id list of the text
            # user_text_file.write(word_index + ' ')









print ('Loading data...')

input = open('resources/data.pkl', 'rb')
user_dict = pickle.load(input)
item_dict = pickle.load(input)

print ('Loaded data!')

users = user_dict.get_dict()

print ('Started users...')
for user in users:
    for index in range(user.num_of_reviews()):
        review_text, rating, item_id = user.get_review_details(index)
        item = item_dict.get_profile(item_id)
        user_id = user.profile_id
        item_id = item.profile_id
        get_match(user_id, item_id, rating)

        get_profile_text(user_id, user.text_list)
        # get_profile_text(item.text_list)

    break



