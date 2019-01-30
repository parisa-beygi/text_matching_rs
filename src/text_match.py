import codecs
import pickle

data_path = '/home/parisa/projects/txt_img/MatchPyramid-for-semantic-matching/data/amazon/'
train_file = codecs.open(data_path + 'amazon_train.txt', 'w', encoding='utf8')
train_file.write('label q1 q2\n')


def get_match(user_id, item_id, rating):
    train_file.write(str(rating) + ' ' + user_id + ' ' + item_id + '\n')





input = open('resources/data.pkl', 'rb')
user_dict = pickle.load(input)
item_dict = pickle.load(input)

users = user_dict.get_dict()

for user in users:
    for index in range(user.num_of_reviews()):
        review_text, rating, item_id = user.get_review_details(index)
        item = item_dict.get_profile(item_id)
        get_match(user.profile_id, item.profile_id, rating)

    break



