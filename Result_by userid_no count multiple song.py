import pandas as pd
#pd.options.mode.chained_assignment = None 
dataframe = pd.read_csv("kaggle_visible_evaluation_triplets.txt", delimiter="\s+")
dataframe.to_csv("NewProcessedDoc_check2.csv", encoding='utf-8', index = False)
df = pd.read_csv('NewProcessedDoc_check2.csv',names = ['userid', 'songid', 'playcount'])
df.sort_values(["userid"],axis=0, ascending=True, inplace=True)


User_count = 0
UserList = [df.userid[0]]
User_Select = [[df.songid[0]]]

for x in range (len(df)-1):
        if (df.userid[x] == df.userid[x+1]):
      #      for i in range(df.playcount[x+1]):
                User_Select.append([])
                User_Select[User_count].append(df.songid[x+1]) 
        else:
            UserList.append(df.userid[x+1])
            User_count = User_count+1
       #     for j in range(df.playcount[x+1]):
            User_Select.append([])
            User_Select[User_count].append(df.songid[x+1]) 

df1 = pd.DataFrame(list(zip(UserList, User_Select)), columns = ['userid', 'songid'])
df1.to_csv("Result_22.csv", encoding='utf-8', index = False)