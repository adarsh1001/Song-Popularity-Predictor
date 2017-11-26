import os, json
from pyAudioAnalysis import audioFeatureExtractionMod as am 

song_dir = 'temp';


def get_playcount_bin(playcount):

	if playcount >= 1000000:
		return 1;
	else if playcount < 1000000 and playcount >= 500000:
		return 2;
	else if playcount < 500000 and playcount >= 100000:
		return 3;
	else if playcount < 100000:
		return 4;


def get_playcount(name):
	l = os.listdir('../%s/' % song_dir);
	f = json.load(open('../downloaded_songs.json'));
	playcount = -1;

	for item in l:
		for key, value in f.iteritems():
			temp = key.split(' ')[0].strip().lower();
			temp2 = key.split(',')[0].strip().lower();
			temp3 = key.split('.')[0].strip().lower();

			if temp in item.lower() or temp2 in item.lower() or temp3 in item.lower():
				for i in value:
					t = i['song_name'].split(' ')[0].strip().lower();
					t1 = i['song_name'].split(',')[0].strip().lower();
					t2 = i['song_name'].split('.')[0].strip().lower();

					if t in item.lower() or t1 in item.lower() or t2 in item.lower():
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
			f_new.append(sum(k)/len(l));

		playcount = get_playcount(w[i]);
		f_new.append(get_playcount_bin(playcount));

		f_final.append(f_new);

