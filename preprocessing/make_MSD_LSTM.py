import sys
import os
import numpy as np
import hdf5_getters
import math

def main():
    dataset_dir = sys.argv[1]
    feat =[]
    feat1=[]
    feat2=[]
    feat3=[]
    feat4=[]

    print "Forming Dataset..."
    listing1 = os.listdir(dataset_dir)
    for a in listing1:
        listing2 = os.listdir(dataset_dir+a+'/')
        for b in listing2:
            listing3 = os.listdir(dataset_dir+a+'/'+b+'/')
            for c in listing3:
                listing4 = os.listdir(dataset_dir+a+'/'+b+'/'+c+'/')
                for d in listing4:
                    h5 = hdf5_getters.open_h5_file_read(dataset_dir+a+'/'+b+'/'+c+'/'+d)
                    feat =[]
                    feat1=[]
                    feat2=[]
                    feat3=[]
                    feat4=[]

                    temp = hdf5_getters.get_artist_hotttnesss(h5)
                    if (math.isnan(temp) or temp==0.0):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_artist_familiarity(h5)
                    if (math.isnan(temp) or temp==0.0):
                        h5.close()
                        continue


                    temp = hdf5_getters.get_end_of_fade_in(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_key_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_loudness(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_mode_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_sections_confidence(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_segments_confidence(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_segments_loudness_max(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_segments_loudness_max_time(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_segments_pitches(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_segments_timbre(h5)
                    if temp.size == 0:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_start_of_fade_out(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue


                    temp = hdf5_getters.get_tempo(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_time_signature_confidence(h5)
                    if (math.isnan(temp)):
                        h5.close()
                        continue

                    temp = hdf5_getters.get_year(h5)
                    if temp == 0:
                        h5.close()
                        continue


                    temp = hdf5_getters.get_artist_terms(h5)
                    if temp.size == 0:
                        h5.close()
                        continue
                    temp_ = hdf5_getters.get_artist_terms_weight(h5)
                    if temp_.size == 0:
                        continue

                    temp = hdf5_getters.get_bars_confidence(h5)
                    sz = temp.size
                    if sz<50:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_beats_confidence(h5)
                    sz = temp.size
                    if sz <50:
                        h5.close()
                        continue
                    mm = np.mean(temp)
                    vv = np.var(temp)
                    if mm==0.0 and vv==0.0:
                    	h5.close()
                        continue

                    temp = hdf5_getters.get_segments_confidence(h5)
                    sz = temp.size
                    if sz <50:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_tatums_confidence(h5)
                    sz = temp.size
                    if sz <50:
                        h5.close()
                        continue

                    temp = hdf5_getters.get_song_hotttnesss(h5)
                    if (math.isnan(temp) or temp==0.0):
                        h5.close()
                        continue



                    temp = hdf5_getters.get_bars_confidence(h5)
                    sz = temp.size
                    sz1 = sz/50
                    i=1
                    j=0
                    while i<=50:
                        if i == 50:
                            sz2 =  sz
                        else:
                            sz2 = i*sz1
                        num=0.0
                        acc = 0
                        while j<sz2:
                            acc += temp[j]
                            j+=1
                            num+=1.0
                        mm = acc/num
                        feat1.append(mm)
                        i+=1


                    temp = hdf5_getters.get_beats_confidence(h5)
                    sz = temp.size
                    sz1 = sz/50
                    i=1
                    j=0
                    while i<=50:
                        if i == 50:
                            sz2 =  sz
                        else:
                            sz2 = i*sz1
                        num=0.0
                        acc = 0
                        while j<sz2:
                            acc += temp[j]
                            j+=1
                            num+=1.0
                        mm = acc/num
                        feat2.append(mm)
                        i+=1


                    temp = hdf5_getters.get_segments_confidence(h5)
                    sz = temp.size
                    sz1 = sz/50
                    i=1
                    j=0
                    while i<=50:
                        if i == 50:
                            sz2 =  sz
                        else:
                            sz2 = i*sz1
                        num=0.0
                        acc = 0
                        while j<sz2:
                            acc += temp[j]
                            j+=1
                            num+=1.0
                        mm = acc/num
                        feat3.append(mm)
                        i+=1


                    temp = hdf5_getters.get_tatums_confidence(h5)
                    sz = temp.size
                    sz1 = sz/50
                    i=1
                    j=0
                    while i<=50:
                        if i == 50:
                            sz2 =  sz
                        else:
                            sz2 = i*sz1
                        num=0.0
                        acc = 0
                        while j<sz2:
                            acc += temp[j]
                            j+=1
                            num+=1.0
                        mm = acc/num
                        feat4.append(mm)
                        i+=1


                    i=0
                    avg = 0.0
                    while i<50:
                        avg = (feat1[i] + feat2[i] + feat3[i] + feat4[i])/4.0
                        feat.append(avg)
                        i++



                    temp = hdf5_getters.get_song_hotttnesss(h5)
                    hott = 0
                    if temp >=0.75:
                        hott = 1
                    elif temp >=0.40 and temp <0.75:
                        hott = 2
                    else:
                        hott = 3
                    feat.append(hott)

                    h5.close()


                    count = 1
                    f=open('MSD_DATASET_LSTM.txt', 'a')
                    outstring=''
                    cnt = 0
                    feat_size = len(feat)
                    for i in feat:
                        cnt+=1
                        outstring+=str(i)
                        if (cnt!=feat_size):
                            outstring+=','
                    outstring+='\n'
                    f.write(outstring)
                    f.close()

main()
