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
	
	[f, s, w] = am.dirWavFeatureExtractionNoAveraging('../%s/' % song_dir);
	#np.savetxt('all_squashed.csv', f, delimiter=',');
	#np.savetxt('all_filenames.csv', w, delimiter=',', fmt='%s');
	#np.savetxt('all_indices.csv', s, delimiter=',');
	'''
	w = np.genfromtxt('all_filenames.csv', dtype='string', delimiter=',');
	f = np.genfromtxt('all_squashed.csv', delimiter=',');
	'''	
	#for i in range(0, len(w)):
	#	w[i] = w[i].replace('../latest_songs/', '');	
	X = [];
	y = [];
	for i in range(0, len(f)/30):
		print "Song %d" % i
		f_new = [];
		f_here = f[i*30:(i+1)*30];
		for k in f_here:
			f_new.append(-1 * sum(k)/len(k));
		
		for ii, item in enumerate(f_new):
			f_new[ii] = f_new[ii] / max(f_new);
		
		playcount = get_playcount(w[i].replace('../%s/' % song_dir, ''));
		if playcount != -1:
			y.append(get_playcount_bin(playcount));
			
			for ind, j in enumerate(f_new):
				'''
				if j <= 0.1:
					f_new[ind] = 1;
				elif j > 0.1 and j <=0.2:
					f_new[ind] = 2;
				elif j > 0.2 and j<=0.225:
					f_new[ind] = 3;
				elif j > 0.225 and j<=0.250:
					f_new[ind] = 4;
				elif j > 0.250 and j <= 0.275:
					f_new[ind] = 5;
				elif j > 0.275 and j<=0.3:
					f_new[ind] = 6;
				elif j > 0.3 and j<=0.325:
					f_new[ind] = 7;
				elif j>0.325 and j<=0.35:
					f_new[ind] = 8;
				elif j>0.35 and j <=0.375:
					f_new[ind] = 9;
				elif j>0.375 and j<=0.4:
					f_new[ind] = 10;
				elif j>0.4 and j<=0.5:
					f_new[ind] = 11;
				elif j>0.5 and j<=0.6:
					f_new[ind] = 12;
				elif j>0.6 and j<=0.7:
					f_new[ind] = 13;
				elif j>0.7 and j<=0.8:
					f_new[ind] = 14;
				elif j>0.8 and j<=0.9:
					f_new[ind] = 15;
				elif j>0.9:
					f_new[ind] = 16;
					'''

				if j <= 0.1:
					f_new[ind] = 1;
				elif j > 0.1 and j<=0.2:
					f_new[ind] = 2;
				elif j > 0.2 and j<=0.3:
					f_new[ind] = 3;
				elif j > 0.3 and j<=0.4:
					f_new[ind] = 4;
				elif j > 0.4 and j<=0.5:
					f_new[ind] = 5;
				elif j > 0.5 and j<=0.6:
					f_new[ind] = 6;
				elif j > 0.6 and j<=0.7:
					f_new[ind] = 7;
				elif j > 0.7 and j<=0.8:
					f_new[ind] = 8;
				elif j > 0.8 and j<=0.9:
					f_new[ind] = 9;
				elif j > 0.9:
					f_new[ind] = 10;

			X.append(f_new);
	
	np.savetxt('test_features.csv', X, delimiter=',');
	np.savetxt('test_labels.csv', y, delimiter=',');
