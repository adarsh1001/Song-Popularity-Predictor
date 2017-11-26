import json, os
from rapidconnect import RapidConnect

rapid = RapidConnect("default-application_5a191a72e4b0d45349f766fe", "bc65de32-d2c1-4679-94d9-2683183f4521");


if __name__ == '__main__':

	downloaded = open('../latest_songs_2/downloaded_songs.json', 'w+');
	d_json = {};

	artists_json = rapid.call('LastFM', 'getTopArtistsChart', { 
		'apiKey': '9c57fb1f3de3132bda349ef57801988d' 
	})
	#artists_json = json.loads(artists);

	full_list = artists_json['artists']['artist'];

	for item in full_list:
		temp = [];
		artist_name = item['name'].encode('ascii', 'ignore');

		top_50_songs = rapid.call('LastFM', 'getTopArtistTracks', { 
			'apiKey': '9c57fb1f3de3132bda349ef57801988d',
			'artist': artist_name,
			'limit' : '5',
			'page' : '5'
		});

		all_tracks = top_50_songs['toptracks']['track'];

		print("Artist - %s" % artist_name);
		for item2 in all_tracks:
			temp_name = item2['name'].encode('ascii', 'ignore');
			print("--%s" % temp_name);
			temp_dict2 = {};

			temp_dict2['song_name'] = temp_name;
			temp_dict2['playcount'] = item2['playcount'];
			temp_dict2['listeners'] = item2['listeners'];

			if not os.path.isfile('../latest_songs_2/%s-%s.mp3' % (artist_name, temp_name)):
				os.system('youtube-song-downloader "%s-%s"' % (artist_name, temp_name));
			temp.append(temp_dict2);

		d_json[artist_name] = temp;

	json.dump(d_json, downloaded);

	#os.chdir('pyAudioAnalysis');
	#os.system('python audioAnalysis.py dirMp3toWav -i ../../latest_songs/ -r 44100 -c');
