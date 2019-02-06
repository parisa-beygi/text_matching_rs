import codecs

import pandas as pd

from src.text_match import get_profile_text


def create_normal_file(in_header, header, in_file, out_file, sep=None, usecols=[], wv_file=None):
    sum = 0
    out_file.write(header)
    for line in in_file:
        contents = line.strip().split(sep)
        if len(contents) != 0 and in_header not in contents:
            # print (sum, contents[0], contents[1])
            if wv_file is not None:
                get_profile_text(contents[0], contents[1], out_file, wv_file)

            else:
                for c in usecols:
                    out_file.write(contents[c] + ' ')
                out_file.write('\n')
            sum +=1

    print (sum)






if __name__== '__main__':
    in_path = '/home/parisa/projects/datasets/text matching/MSR Paraphrase Corpus/'
    in_train_path = in_path + 'msr_paraphrase_train.txt'
    in_test_path = in_path + 'msr_paraphrase_test.txt'
    in_data_path = in_path + 'msr_paraphrase_data.txt'

    out_path = '/home/parisa/projects/txt_img/MatchPyramid-for-semantic-matching/data/msrp/'
    out_train_path = out_path + 'msrp_train.txt'
    out_test_path = out_path + 'msrp_test.txt'
    out_data_path = out_path + 'msrp_data.txt'


    out_wv_path = out_path + 'word2vec.txt'

    # file = pd.read_csv(path, sep='	', dtype=str, usecols=[0,1,2])
    # file = file.dropna()
    # # sent1id, sent2id = file['#1 ID'], file['#2 ID']
    # sent1id = file['Sentence ID']
    #
    # sum = 0
    # # for id1, id2 in zip(sent1id, sent2id):
    # #     print (str(sum) + ' ' + id1, id2)
    # #     sum += 1
    # for id in sent1id:
    #     print (str(sum) + ' ' + id)
    #     sum += 1
    #
    # # print (len(sent1id), len(sent2id))
    # print (len(sent1id))
    # print (sum)
    in_train_file= codecs.open(in_train_path,'r', encoding='utf8')
    out_train_file = codecs.open(out_train_path,'w', encoding='utf8')

    in_test_file= codecs.open(in_test_path,'r', encoding='utf8')
    out_test_file = codecs.open(out_test_path,'w', encoding='utf8')

    in_data_file= codecs.open(in_data_path,'r', encoding='utf8')
    out_data_file = codecs.open(out_data_path,'w', encoding='utf8')


    out_wv_file = codecs.open(out_wv_path,'w', encoding='utf8')


    t_header = 'label q1 q2\n'
    in_header = 'Quality'
    create_normal_file(in_header, t_header, in_train_file, out_train_file, usecols=[0,1,2])
    create_normal_file(in_header, t_header, in_test_file, out_test_file, usecols=[0,1,2])


    d_header = 'qid\twords\n'
    in_header = 'Sentence ID'
    create_normal_file(in_header, d_header, in_data_file, out_data_file, sep='\t', usecols=[0,1], wv_file=out_wv_file)


    data = pd.read_csv(in_data_path, sep='\t', dtype=str)
    print (len(data))
