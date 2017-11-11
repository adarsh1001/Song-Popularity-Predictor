import sys
import os
import numpy as np
import hdf5_getters
import math

Features = ['artist_hotttnesss', 'artist_familiarity', 'bars_conf_mean', 'bars_conf_var', 'beats_conf_mean', 'beats_conf_var', 'duration', 'end_of_fade_in', 'key', 'key_conf', 'loudness', 'mode', 'mode_conf', 'sections_conf_mean', 'sections_conf_var', 'segments_conf_mean', 'segments_conf_var', 'segments_loudness_max_mean', 'segments_loudness_max_var', 'segments_loudness_max_time_mean', 'segments_loudness_max_time_var', 'segments_pitches_mean', 'segments_pitches_var', 'segments_timbre_mean', 'segments_timbre_var', 'start_of_fade_out', 'tatums_conf_mean', 'tatums_conf_var', 'tempo', 'time_sign', 'time_sign_conf', 'year', 'song_hotttnesss']
Bag_Words={} #Complete BoW
Final_BoW={} #Pruned BoW
feat=[]


def Lablify():
    f=open('AMSD_DATASET.txt', 'a')
    outstring=''
    for i in Features:
        outstring+=i
        outstring+=','
    for i in Final_BoW:
        outstring+=i
        outstring+=','
    outstring+='\n'
    f.write(outstring)
    f.close()

def Create_BoW(arg):
    listing1 = os.listdir(arg)
    for a in listing1:
        listing2 = os.listdir(arg+a+'/')
        for b in listing2:
            listing3 = os.listdir(arg+a+'/'+b+'/')
            for c in listing3:
                listing4 = os.listdir(arg+a+'/'+b+'/'+c+'/')
                for d in listing4:
                    h5 = hdf5_getters.open_h5_file_read(arg+a+'/'+b+'/'+c+'/'+d)
                    art_t = hdf5_getters.get_artist_terms(h5)
                    for i in art_t:
                        Bag_Words[i]=1
                    h5.close()
    Bag_Words['UNK']=1

def Index_BoW(BoW):
    index=0
    for i in BoW:
		BoW[i]=index
		index+=1
    return index

def Frequency(l, arg):
    arr = np.zeros(l)
    listing1 = os.listdir(arg)
    for a in listing1:
        listing2 = os.listdir(arg+a+'/')
        for b in listing2:
            listing3 = os.listdir(arg+a+'/'+b+'/')
            for c in listing3:
                listing4 = os.listdir(arg+a+'/'+b+'/'+c+'/')
                for d in listing4:
                    h5 = hdf5_getters.open_h5_file_read(arg+a+'/'+b+'/'+c+'/'+d)
                    art_t = hdf5_getters.get_artist_terms(h5)
                    for i in art_t:
                        k = Bag_Words[i]
                        arr[k]+=1
                    h5.close()
    return arr

def Prune(count):
    #We take top 100 out of all BoW keywords
    for i in range(50):
        ind = np.argmax(count)
        for j in Bag_Words:
            if Bag_Words[j] == ind:
                Final_BoW[j] = 1
        count[ind]=-1
    ind = Index_BoW(Final_BoW)
    return(ind)


def MeanVar(temp):
    temp = np.asarray(temp, dtype=np.float64)
    feat.append(np.mean(temp))
    feat.append(np.var(temp))

def main():
    dataset_dir = sys.argv[1]
    global feat
    Create_BoW(dataset_dir)
    Size_BoW = Index_BoW(Bag_Words)
    count = Frequency(Size_BoW, dataset_dir)
    Size_BoW = Prune(count)
    Lablify()

    listing1 = os.listdir(dataset_dir)
    for a in listing1:
        listing2 = os.listdir(dataset_dir+a+'/')
        for b in listing2:
            listing3 = os.listdir(dataset_dir+a+'/'+b+'/')
            for c in listing3:
                listing4 = os.listdir(dataset_dir+a+'/'+b+'/'+c+'/')
                for d in listing4:
                    h5 = hdf5_getters.open_h5_file_read(dataset_dir+a+'/'+b+'/'+c+'/'+d)
                    feat = []
                    temp = hdf5_getters.get_artist_hotttnesss(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_artist_familiarity(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_bars_confidence(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_beats_confidence(h5)
                    MeanVar(temp)


                    feat.append(hdf5_getters.get_duration(h5))

                    temp = hdf5_getters.get_end_of_fade_in(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)


                    feat.append(hdf5_getters.get_key(h5))

                    temp = hdf5_getters.get_key_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_loudness(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    feat.append(hdf5_getters.get_mode(h5))

                    temp = hdf5_getters.get_mode_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_sections_confidence(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_segments_confidence(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_segments_loudness_max(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_segments_loudness_max_time(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_segments_pitches(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_segments_timbre(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_start_of_fade_out(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_tatums_confidence(h5)
                    MeanVar(temp)

                    temp = hdf5_getters.get_tempo(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    feat.append(hdf5_getters.get_time_signature(h5))

                    temp = hdf5_getters.get_time_signature_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_year(h5)
                    if temp == 0:
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_song_hotttnesss(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue
                    feat.append(temp)

                    temp = hdf5_getters.get_artist_terms(h5)
                    temp_ = hdf5_getters.get_artist_terms_weight(h5)
                    if temp_.size == 0:
                        continue
                    for j in Final_BoW:
                        if j in temp:
                            x = np.where(temp==j)
                            x = x[0][0]
                            feat.append(temp_[x])
                        else:
                            x = 0.0
                            feat.append(x)

                    h5.close()


                    count = 1
                    f=open('AMSD_DATASET.txt', 'a')
                    outstring=''
                    for i in feat:
                        outstring+=str(i)
                        outstring+=','
                    outstring+='\n'
                    f.write(outstring)
                    f.close()

main()
