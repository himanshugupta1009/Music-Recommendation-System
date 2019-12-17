import pandas as pd
import csv

DATA_FILE = r"kaggle_visible_evaluation_triplets.txt"
BY_SONG_FILE = "bySong.csv"
BY_USER_FILE = "byUser.csv"
NUM_UNIQUE_SONG = 163206
NUM_UNIQUE_USER = 110000


def generateByUserCsv():
	# Generate byUser.csv
	# userid    song_id1,song_id2,song_id3,.....
	df = pd.read_csv(DATA_FILE, sep='\t', names=['userid', 'songid', 'playcount'])
	df.sort_values(by="userid", axis=0, ascending=True, inplace=True)
	df = df.reset_index()

	userIDList = []
	songIDList = []

	count = 0
	for i in range(len(df)):
		if not df.userid[i] in userIDList:
			currentUserId = df.userid[i]
			currentUserIdSongList = [df.songid[i]]
			userIDList.append(df.userid[i])
			count += 1

			for j in range(i + 1, len(df)):
				if currentUserId == df.userid[j]:
					currentUserIdSongList.append(df.songid[j])
				else:
					songIDList.append(",".join(currentUserIdSongList))
					print(str((100 * count) / NUM_UNIQUE_USER) + "%")
					break

	df1 = pd.DataFrame(list(zip(userIDList, songIDList)), columns=['userid', 'songid'])
	df1.to_csv(BY_USER_FILE, encoding='utf-8', sep='\t', index=False, quoting = csv.QUOTE_NONE, escapechar = ' ')

	print("Finish")


def generateBySongCsv():
	# Generate bySong.csv
	# songid    user_id1,user_id2,user_id3,......

	df = pd.read_csv(DATA_FILE, sep='\t', names=['userid', 'songid', 'playcount'])
	df.sort_values(by="songid", axis=0, ascending=True, inplace=True)
	df = df.reset_index()

	songIDList = []
	userIDList = []

	count = 0
	for i in range(len(df)):
		if not df.songid[i] in songIDList:
			currentSongId = df.songid[i]
			currentSongIdUserList = [df.userid[i]]
			songIDList.append(df.songid[i])
			count += 1

			for j in range(i + 1, len(df)):
				if currentSongId == df.songid[j]:
					currentSongIdUserList.append(df.userid[j])
				else:
					userIDList.append(",".join(currentSongIdUserList))
					print(str((100 * count) / NUM_UNIQUE_SONG) + "%")
					break

	df1 = pd.DataFrame(list(zip(songIDList, userIDList)), columns=['songid', 'userid'])
	df1.to_csv(BY_SONG_FILE, encoding='utf-8', sep='\t', index=False, quoting = csv.QUOTE_NONE, escapechar = ' ')

	print("Finish")

def main():
	selection = input("Select A or B (A: bySong.csv, B: byUser.csv): ")
	if selection.lower() == "a":
		generateBySongCsv()
	elif selection.lower() == "b":
		generateByUserCsv()
	else:
		print("invalid selection")
main()
