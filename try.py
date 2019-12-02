import pandas as pd
import sys
import matplotlib.pylab as plt
import operator
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder


uid_songid_file_location = './Dataset/byUser.csv'
songid_uid_file_location = './Dataset/bySong.csv'
songid_mappings_file_location = './Dataset/kaggle_songs.txt'
uid_songid_triplets_file_location = './Dataset/kaggle_visible_evaluation_triplets.txt'


uid_songid_file = open(uid_songid_file_location)
uid_songid_file_data = []
for line in uid_songid_file:
    uid_songid_file_data.append(line.strip().split('\t')[1].strip().split(','))
uid_songid_file_data = uid_songid_file_data[1:]
uid_songid_file.close()


songid_mappings_file = open(songid_mappings_file_location)
songid_mappings = {}
for line in songid_mappings_file:
    #print(line)
    temp_var = line.strip().split()
    songid_mappings[temp_var[0]] = int(temp_var[1])

songid_mappings_file.close()


uid_songid_transaction_data = uid_songid_file_data[1:5000]
print(len(uid_songid_file_data))
transaction_encoder = TransactionEncoder()
transaction_encoder_nd_array = transaction_encoder.fit(uid_songid_transaction_data).transform(uid_songid_transaction_data)
df = pd.DataFrame(transaction_encoder_nd_array, columns=transaction_encoder.columns_)

apriori(df, min_support=0.0015)
print("finish")
