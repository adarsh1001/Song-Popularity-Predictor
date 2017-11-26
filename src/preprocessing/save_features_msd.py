import os, json
import numpy as np 
from pyAudioAnalysis import audioFeatureExtractionMod as am 

song_dir = 'latest_songs_2';


def get_playcount_bin(playcount):

	if playcount >= 5000000:
		return 1;
	elif playcount < 5000000 and playcount >= 2500000:
		return 2;
	elif playcount < 2500000:
		return 3;


def get_playcount(name):
	f = json.load(open('../d_songs_new.json'));
	playcount = -1;

	for key, value in f.iteritems():
		temp = key.split(' ')[0].strip().lower();
		temp2 = key.split(',')[0].strip().lower();
		temp3 = key.split('.')[0].strip().lower();

		if temp in name.lower() or temp2 in name.lower() or temp3 in name.lower():
			for i in value:
				t = i['song_name'].split(' ')[0].strip().lower();
				t1 = i['song_name'].split(',')[0].strip().lower();
				t2 = i['song_name'].split('.')[0].strip().lower();

				if t in name.lower() or t1 in name.lower() or t2 in name.lower():
					playcount = int(i['playcount']);
					break;
			break;

	return playcount;



if __name__ == '__main__':
	
	f = np.genfromtxt('../dataset/MSD_DATASET_LSTM.txt', delimiter=',');

	X = [];
	y = f[:, -1];
	y -= 1;

	f = f[:, 0:len(f[0])-1];
	for i in range(0, len(f)):
		f_new = [];
		for ind, j in enumerate(f[i]):
			if j <= 0.1:
				f_new.append(1);
			elif j > 0.1 and j<=0.2:
				f_new.append(2);
			elif j > 0.2 and j<=0.3:
				f_new.append(3);
			elif j > 0.3 and j<=0.4:
				f_new.append(4);
			elif j > 0.4 and j<=0.5:
				f_new.append(5);
			elif j > 0.5 and j<=0.6:
				f_new.append(6);
			elif j > 0.6 and j<=0.7:
				f_new.append(7);
			elif j > 0.7 and j<=0.8:
				f_new.append(8);
			elif j > 0.8 and j<=0.9:
				f_new.append(9);
			elif j > 0.9:
				f_new.append(10);

		X.append(f_new);
	
	np.savetxt('msd_features.csv', X, delimiter=',');
	np.savetxt('msd_labels.csv', y, delimiter=',');
