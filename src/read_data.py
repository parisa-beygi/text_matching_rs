import codecs
import gzip
import pickle
import time
from src.profile import ProfileDictionary


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)


def read(path):
    mygen = parse(path)

    user_dict = ProfileDictionary()
    item_dict = ProfileDictionary()

    j = 0
    for i in mygen:
        print(i)
        j += 1

        out_file.write(str(i) + '\n')

        user_id = i['reviewerID']
        rev = i['reviewText']
        item_id = i['asin']
        rating = i['overall']

        user = user_dict.get_profile(user_id)
        user.update(rev, item_id, rating)

        item = item_dict.get_profile(item_id)
        item.update(rev, user_id, rating)

        #TODO: should be removed
        if j > 3:
            return user_dict, item_dict


    return user_dict, item_dict

if __name__== '__main__':
    out_file= codecs.open('output/data_file.txt','w', encoding='utf8')
    path = '/home/parisa/projects/datasets/recommender/Amazon/reviews_Books_5.json.gz'
    start = time.time()

    user_dict, item_dict = read(path)

    # TODO: should be changed to data.pkl
    with open("resources/incomplete_data.pkl", "wb") as structured_data:
        pickle.dump(user_dict, structured_data)
        pickle.dump(item_dict, structured_data)

    end = time.time()
    print (str((end - start)))
    print ('salaaam\n')
