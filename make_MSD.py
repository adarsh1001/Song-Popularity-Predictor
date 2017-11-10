import sys
import os
import numpy as np
import hdf5_getters

Features = ['artist_hotttnesss', 'sample_rate', 'artist_familiarity', 'bars_conf_mean', 'bars_conf_var', 'beats_conf_mean', 'beats_conf_var', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'key', 'key_conf', 'loudness', 'mode', 'mode_conf', 'sections_conf_mean', 'sections_conf_var', 'segments_conf_mean', 'segments_conf_var', 'segments_loudness_max_mean', 'segments_loudness_max_var', 'segments_loudness_max_time_mean', 'segments_loudness_max_time_var', 'segments_pitches_mean', 'segments_pitches_var', 'segments_timbre_mean', 'segments_timbre_var', 'start_of_fade_out', 'tatums_conf_mean', 'tatums_conf_var', 'tempo', 'time_sign', 'time_sign_conf', 'year', 'song_hotttnesss']

def lablify():
    f=open('MSD_DATASET.txt', 'a')
    outstring=''
    for i in Features:
        outstring+=i
        outstring+=' '
    outstring+='\n'
    f.write(outstring)
    f.close()


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
                    feat.append(hdf5_getters.get_artist_hotttnesss(h5))
                    feat.append(hdf5_getters.get_analysis_sample_rate(h5))
                    feat.append(hdf5_getters.get_artist_familiarity(h5))

                    feat.append(hdf5_getters.get_artist_terms(h5))
                    feat.append(hdf5_getters.get_artist_terms_freq(h5))
                    feat.append(hdf5_getters.get_artist_terms_weight(h5))
                    feat.append(hdf5_getters.get_bars_confidence(h5))
                    feat.append(hdf5_getters.get_beats_confidence(h5))
                    feat.append(hdf5_getters.get_danceability(h5))
                    feat.append(hdf5_getters.get_duration(h5))
                    feat.append(hdf5_getters.get_end_of_fade_in(h5))
                    feat.append(hdf5_getters.get_energy(h5))
                    feat.append(hdf5_getters.get_key(h5))
                    feat.append(hdf5_getters.get_key_confidence(h5))
                    feat.append(hdf5_getters.get_loudness(h5))
                    feat.append(hdf5_getters.get_mode(h5))
                    feat.append(hdf5_getters.get_mode_confidence(h5))
                    feat.append(hdf5_getters.get_sections_confidence(h5))
                    feat.append(hdf5_getters.get_segments_confidence(h5))
                    feat.append(hdf5_getters.get_segments_loudness_max(h5))
                    feat.append(hdf5_getters.get_segments_loudness_max_time(h5))
                    feat.append(hdf5_getters.get_segments_pitches(h5))
                    feat.append(hdf5_getters.get_segments_timbre(h5))
                    feat.append(hdf5_getters.get_song_hotttnesss(h5))
                    feat.append(hdf5_getters.get_start_of_fade_out(h5))
                    feat.append(hdf5_getters.get_tatums_confidence(h5))
                    feat.append(hdf5_getters.get_tempo(h5))
                    feat.append(hdf5_getters.get_time_signature(h5))
                    feat.append(hdf5_getters.get_time_signature_confidence(h5))
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
