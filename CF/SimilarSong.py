import operator
from pprint import pprint

from cf import MSD_util, MSD_rec
import copy


# Return similar songid list with descending order
def getSimilarity(songId, uniqeSongIds, pr):
	uniqSongId2Score = dict()

	for uSong in uniqeSongIds:
		try:
			score = pr.Match(songId, uSong)
			if score != 0:
				uniqSongId2Score[uSong] = score
		except:
			pass

	# delete the element whose score is 0
	deleteList = []
	for uSong in uniqSongId2Score.keys():
		if uniqSongId2Score[uSong] == 0:
			deleteList.append(uSong)
	for key in deleteList:
		del uniqSongId2Score[key]

	# Delete own element (songId's)
	try:
		del uniqSongId2Score[songId]
	except:
		pass

	# Sort by score with descending order
	sortedList = sorted(uniqSongId2Score.items(), key=operator.itemgetter(1))
	sortedList.reverse()

	# Extract songid
	songList = []
	for t in sortedList:
		songList.append(t[0])
	return songList




def main():


	# Prepare for match
	f_triplets_tr = "train_triplets.txt"
	s2u_tr = MSD_util.song_to_users(f_triplets_tr)
	_A = 0.15
	_Q = 3
	pr = MSD_rec.PredSI(s2u_tr, _A, _Q)



	uniqueSongId = []
	f = open('kaggle_songs.txt', 'r')
	line = f.readline()
	while line:
		uniqueSongId.append(line.split(" ")[0])
		line = f.readline()
	f.close()

	outputFile = open("similarity.txt", "w")

	count = 0
	total = len(uniqueSongId)
	for id in uniqueSongId:
		count += 1
		print(str(100*count/total) + "%")
		songIds = copy.deepcopy(uniqueSongId)
		output = getSimilarity(id, songIds, pr)
		if len(output) != 0:
			line = ', '.join(output)
			line = id + ", {" + line + "}"
			print(line)
			outputFile.write(line)
			outputFile.write("\n")
	outputFile.close()



if __name__=="__main__":
	main()





