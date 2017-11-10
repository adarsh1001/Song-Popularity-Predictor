import sys
import os
import numpy as np
import hdf5_getters

from geopy.geocoders import Nominatim
import pycountry as pc

Features = ['analysis_sample_rate', 'artist_familiarity', 'artist_hotttnesss', 'artist_latitude', 'artist_location', 'artist_longitude', 'artist_mbid', 'artist_mbtags', 'artist_mbtags_count', 'artist_name', 'artist_playmeid', 'artist_terms', 'artist_terms_freq', 'artist_terms_weight', 'audio_md5', 'bars_confidence', 'bars_start', 'beats_confidence', 'beats_start', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'release', 'release_7digitalid', 'sections_confidence', 'sections_start', 'segments_confidence', 'segments_loudness_max', 'segments_loudness_max_time', 'segments_loudness_start', 'segments_pitches', 'segments_start', 'segments_timbre', 'similar_artists', 'song_hotttnesss', 'song_id', 'start_of_fade_out', 'tatums_confidence', 'tatums_start', 'tempo', 'time_signature', 'time_signature_confidence', 'title', 'track_id', 'track_7digitalid', 'year']

def lablify():
    f=open('MSD_DATASET.txt', 'a')
    outstring=''
    for i in Features:
        outstring+=i
        outstring+=' '
    outstring+='\n'
    f.write(outstring)
    f.close()

def populate_country_ids():
    c_ids = {};

    i = 0;
    for item in list(pc.countries):
        c_ids[str(item.alpha_2).lower()] = i;
        i += 1;

    return c_ids;

def get_country(lat, lon):
    geolocator = Nominatim()
    location = geolocator.reverse(str(lat) + ", " + str(lon));

    return str(location.raw['address']['country_code']).lower();


if __name__ == '__main___':
    dataset_dir = sys.argv[1]

    lablify()

    listing1 = os.listdir(dataset_dir)
    for a in listing1:
        listing2 = os.listdir(dataset_dir+a+'/')
        for b in listing2:
            listing3 = os.listdir(dataset_dir+a+'/'+b+'/')
            for c in listing3:
                listing4 = os.listdir(dataset_dir+a+'/'+b+'/'+c+'/')
                for d in listing4:
                    h5 = hdf5_getters.open_h5_file_read(dataset_dir+a+'/'+b+'/'+c+'/'+d)
                    feat=[]
                    feat.append(hdf5_getters.get_analysis_sample_rate(h5))
                    feat.append(hdf5_getters.get_artist_7digitalid(h5))
                    feat.append(hdf5_getters.get_artist_familiarity(h5))
                    feat.append(hdf5_getters.get_artist_hotttnesss(h5))
                    feat.append(hdf5_getters.get_artist_id(h5))
                    feat.append(hdf5_getters.get_artist_latitude(h5))
                    feat.append(hdf5_getters.get_artist_location(h5))
                    feat.append(hdf5_getters.get_artist_longitude(h5))
                    feat.append(hdf5_getters.get_artist_mbid(h5))
                    feat.append(hdf5_getters.get_artist_mbtags(h5))
                    feat.append(hdf5_getters.get_artist_mbtags_count(h5))
                    feat.append(hdf5_getters.get_artist_name(h5))
                    feat.append(hdf5_getters.get_artist_playmeid(h5))
                    feat.append(hdf5_getters.get_artist_terms(h5))
                    feat.append(hdf5_getters.get_artist_terms_freq(h5))
                    feat.append(hdf5_getters.get_artist_terms_weight(h5))
                    feat.append(hdf5_getters.get_audio_md5(h5))
                    feat.append(hdf5_getters.get_bars_confidence(h5))
                    feat.append(hdf5_getters.get_bars_start(h5))
                    feat.append(hdf5_getters.get_beats_confidence(h5))
                    feat.append(hdf5_getters.get_beats_start(h5))
                    feat.append(hdf5_getters.get_danceability(h5))
                    feat.append(hdf5_getters.get_duration(h5))
                    feat.append(hdf5_getters.get_end_of_fade_in(h5))
                    feat.append(hdf5_getters.get_energy(h5))
                    feat.append(hdf5_getters.get_key(h5))
                    feat.append(hdf5_getters.get_key_confidence(h5))
                    feat.append(hdf5_getters.get_loudness(h5))
                    feat.append(hdf5_getters.get_mode(h5))
                    feat.append(hdf5_getters.get_mode_confidence(h5))
                    feat.append(hdf5_getters.get_release(h5))
                    feat.append(hdf5_getters.get_release_7digitalid(h5))
                    feat.append(hdf5_getters.get_sections_confidence(h5))
                    feat.append(hdf5_getters.get_sections_start(h5))
                    feat.append(hdf5_getters.get_segments_confidence(h5))
                    feat.append(hdf5_getters.get_segments_loudness_max(h5))
                    feat.append(hdf5_getters.get_segments_loudness_max_time(h5))
                    feat.append(hdf5_getters.get_segments_loudness_start(h5))
                    feat.append(hdf5_getters.get_segments_pitches(h5))
                    feat.append(hdf5_getters.get_segments_start(h5))
                    feat.append(hdf5_getters.get_segments_timbre(h5))
                    feat.append(hdf5_getters.get_similar_artists(h5))
                    feat.append(hdf5_getters.get_song_hotttnesss(h5))
                    feat.append(hdf5_getters.get_song_id(h5))
                    feat.append(hdf5_getters.get_start_of_fade_out(h5))
                    feat.append(hdf5_getters.get_tatums_confidence(h5))
                    feat.append(hdf5_getters.get_tatums_start(h5))
                    feat.append(hdf5_getters.get_tempo(h5))
                    feat.append(hdf5_getters.get_time_signature(h5))
                    feat.append(hdf5_getters.get_time_signature_confidence(h5))
                    feat.append(hdf5_getters.get_title(h5))
                    feat.append(hdf5_getters.get_track_id(h5))
                    feat.append(hdf5_getters.get_track_7digitalid(h5))
                    feat.append(hdf5_getters.get_year(h5))
                    h5.close()

                    count = 1
                    f=open('MSD_DATASET.txt', 'a')
                    outstring=''
                    for i in feat:
                        outstring+=str(i)
                        outstring+=' '
                    outstring+='\n'
                    f.write(outstring)
                    f.close()
