import sys

from cf import MSD_util, MSD_rec
from cf.SimilarSong import getSimilarity

def main(argv):
	if len(argv) == 1:
		id = argv[0]
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

		outputFile = open(id + ".txt", "w")


		output = getSimilarity(id, uniqueSongId, pr)
		if len(output) != 0:
			line = ', '.join(output)
			line = id + ", {" + line + "}"
			print(line)
			outputFile.write(line)
			outputFile.write("\n")
		else:
			print("There are no similar songs")

		outputFile.close()
	else:
		print("Please user only ONE argument which is song id (EX: SOAAAFI12A6D4F9C66)")




if __name__=="__main__":
	main(sys.argv[1:])
