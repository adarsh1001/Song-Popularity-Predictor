import os, json
from pyAudioAnalysis import audioFeatureExtractionMod as am 

song_dir = 'temp';


def get_playcount_bin(playcount):

	if playcount >= 5000000:
		return 1;
	elif playcount < 5000000 and playcount >= 1000000:
		return 2;
	elif playcount < 1000000 and playcount >= 100000:
		return 3;
	elif playcount < 100000:
		return 4;


def get_playcount(name):
	f = json.load(open('../downloaded_songs.json'));
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

	f_final = [];
	for i in range(0, len(f)/30):
		f_new = [];
		f_here = f[i*30:(i+1)*30];
		for k in f_here:
			f_new.append(sum(k)/len(k));

		playcount = get_playcount(w[i]);
		print playcount
		f_new.append(get_playcount_bin(playcount));

		f_final.append(f_new);
	
	print len(f_final);
	print len(f_final[0]);

	for item in f_final:
		if item[-1] != 1:
			print item;
