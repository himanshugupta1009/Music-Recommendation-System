import pandas as pd
import sys
import matplotlib.pylab as plt
import operator
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import csv

BY_USER_PATH = './Dataset/byUser.csv'
KAGGLE_SONGS_PATH = './Dataset/kaggle_songs.txt'
FREQ_MAP_PATH = './Dataset/freq_map.csv'
uid_songid_triplets_file_location = './Dataset/kaggle_visible_evaluation_triplets.txt'


byUserFile = open(BY_USER_PATH)
songsList = []
userIdList = []

for line in byUserFile:
    songsList.append(line.strip().split('\t')[1].strip().split(','))
    userIdList.append(line.strip().split('\t')[0])
songsList = songsList[1:]
userIdList = userIdList[1:]
byUserFile.close()

kaggleSongsFile = open(KAGGLE_SONGS_PATH)
songIdList = []
for line in kaggleSongsFile:
    songIdList.append(line.split(" ")[0])
kaggleSongsFile.close()

# print(uid_songid_file_data)
# print(userList)
# print(songIdList)

##              songid1 songid2 songid3
## userid1
## userid2
## userid3

freq = []
for x in range(len(songsList)):
    line = [0 for i in range(len(songIdList))]
    for i in range(len(songsList[x])):
        for j in range(len(songIdList)):
            if songsList[x][i] == songIdList[j]:
                line[j] += 1
    freq.append(line)
    print(100 * x / len(songsList))

with open(FREQ_MAP_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(freq)





#https://qiita.com/hik0107/items/96c483afd6fb2f077985