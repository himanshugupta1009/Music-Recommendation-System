
import pandas as pd
#pd.options.mode.chained_assignment = None 
dataframe = pd.read_csv("kaggle_visible_evaluation_triplets.txt", delimiter="\s+")
dataframe.to_csv("NewProcessedDoc_check2.csv", encoding='utf-8', index = False)
df = pd.read_csv('NewProcessedDoc_check2.csv',names = ['userid', 'songid', 'playcount'])
df = df[['songid', 'userid','playcount']]
df = df.sort_values('songid', ascending = True)
df = df.reset_index(drop=True)

Song_count = 0
User_Select = [df.songid[0]]
UserList = [[df.userid[0]]]

for x in range (len(df)-1):
        if (df.songid[x] == df.songid[x+1]):
            for i in range(df.playcount[x+1]):
                UserList.append([])
                UserList[Song_count].append(df.userid[x+1]) 
        else:
            User_Select.append(df.songid[x+1])
            Song_count = Song_count+1
            for j in range(df.playcount[x+1]):
                UserList.append([])
                UserList[Song_count].append(df.userid[x+1]) 

df1 = pd.DataFrame(list(zip(User_Select,UserList)), columns = ['songid','userid'])
df1.to_csv("Result_by songid_count multiple song.csv", encoding='utf-8', index = False)
