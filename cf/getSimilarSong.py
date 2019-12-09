from cf import MSD_util, MSD_rec
from pprint import pprint
import operator


# Return similar songid list with descending order
def similarity(songId):
	f_triplets_tr = "train_triplets.txt"

	s2u_tr = MSD_util.song_to_users(f_triplets_tr)
	_A = 0.15
	_Q = 3
	pr = MSD_rec.PredSI(s2u_tr, _A, _Q)

	uniqSongId2Score = dict()

	f = open('kaggle_songs.txt', 'r')
	line = f.readline()
	while line:
		uniqSongId2Score[line.split(" ")[0]] = 0
		line = f.readline()
	f.close()

	for uSong in uniqSongId2Score.keys():
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
	del uniqSongId2Score[songId]

	# Sort by score with descending order
	sortedList = sorted(uniqSongId2Score.items(),  key=operator.itemgetter(1))
	sortedList.reverse()

	# Extract songid
	songList = []
	for t in sortedList:
		songList.append(t[0])
	return songList


output = similarity("SOIJTCX12A6D4F8247")

pprint(output)



