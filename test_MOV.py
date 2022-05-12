import datetime
from time import *
import time 
from pymediainfo import MediaInfo

def MOV(file_path,file):

    media_info = MediaInfo.parse(file_path)

    c=0
    err=[]

    for track in media_info.general_tracks: # ce qui concerne le media en general

        if track.format == "MPEG-4":
            #print ("format" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else:
            #print ("format" , track.track_type , track.stream_identifier , track.format , "different de MPEG-4")
            error=("format " + track.track_type + " "  + str(track.stream_identifier) + " " + track.format + " " + "different de MPEG-4")
            #print ("X")
            err.append(error)

        if track.tim == "00:00:00:00":
            #print ("TIM" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else:
            #print ("TIM" , track.track_type , track.stream_identifier , track.tim , "different de 00:00:00:00")
            error=("TIM " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.tim) + " " + "different de 00:00:00:00")
            #print ("X")
            err.append(error)

        if track.format_profile == "QuickTime":
            #print ("format profile" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else:
            #print ("format profile" , track.track_type , track.stream_identifier , track.format_profile , "different de QuickTime")
            error=("format profile " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.format_profile) + " " + "different de QuickTime")
            #print ("X")
            err.append(error)

    for track in media_info.video_tracks: # pour le stream vidéo

        if track.format == "ProRes":
            #print ("format" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("format" , track.track_type , track.stream_identifier , track.format , "different de ProRes")
            error=("format " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.format) + " " + "different de ProRes")
            #print ("X")
            err.append(error)
                    
        if track.format_profile == "422 HQ":
            #print ("format profile" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("format profile" , track.track_type , track.stream_identifier , track.format_profile , "different de 422 HQ")
            error=("format profile " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.format_profile) + " " + "different de 422 HQ")
            #print ("X")
            err.append(error)
                    
        if track.bit_rate >= 147200000 and track.bit_rate <= 220800000  :
            #print ("bit rate" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("bit rate " , track.track_type , track.stream_identifier , track.bit_rate , "different de 184000000")
            error=("bit rate " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.bit_rate) + " " + "different de 184000000")
            #print ("X")
            err.append(error)
                    
        if track.width == 1920:
            #print ("width" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("width" , track.track_type , track.stream_identifier , track.width , "different de 1920")
            error=("width " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.width) + " " + "different de 1920")
            #print ("X")
            err.append(error)
                    
        if track.height == 1080:
            #print ("height" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("height" , track.track_type , track.stream_identifier , track.height , "different de 1080")
            error=("height " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.height) + " " + "different de 1080")
            #print ("X")
            err.append(error)
                    
        if track.frame_rate == "25.000":
            #print ("frame rate" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("frame rate" , track.track_type , track.stream_identifier , track.frame_rate , "different de 25.000")
            error=("frame rate " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.frame_rate) + " " + "different de 25.000")
            #print ("X")
            err.append(error)
                        
        if track.scan_type == "Interlaced":
            #print ("scan type" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("scan type" , track.track_type , track.stream_identifier , track.scan_type , "different de Interlaced")
            error=("scan type " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.scan_type) + " " + "different de Interlaced")
            #print ("X")
            err.append(error)
                        
        if track.scan_order == "TFF":
            #print ("scan order" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("scan order" , track.track_type , track.stream_identifier , track.scan_order , "different de TFF")
            error=("scan order " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.scan_order) + " " + "different de TFF")
            #print ("X")
            err.append(error)

        if track.bits__pixel_frame >= "1" :
            #print ("Bit-(Pixel*Frame)" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else:
            #print ("Bit-(Pixel*Frame)" , track.track_type , track.stream_identifier , track.bits__pixel_frame , "< 1")
            error=("Bit-(Pixel*Frame) " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.bits__pixel_frame) + " " + "< 1")
            #print ("X")
            err.append(error)

    for track in media_info.audio_tracks: # pour tous les streams audios existants
        if (track.format) == "PCM":
            #print ("format" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else:
            #print ("format" , track.track_type , track.stream_identifier , track.format , "different de PCM")
            error=("format " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.format) + " " + "different de PCM")
            #print ("X")
            err.append(error)

        if(track.sampling_rate) == 48000 :
            #print ("sampling rate" , track.track_type , track.stream_identifier)
            #print ("ok")
            c=c+1
        else :
            #print ("sampling rate" , track.track_type , track.stream_identifier , track.sampling_rate , "different de 48000")
            error=("sampling rate " + track.track_type + " "  + str(track.stream_identifier) + " " + str(track.sampling_rate) + " " + "different de 48000")
            #print ("X")
            err.append(error)

    # print ("\n")

    now = datetime.datetime.now()
    # print ("Rapport au" , now.strftime("%Y-%m-%d %H:%M:%S"))


    # print (file)
    # print (track.duration)
    for track in media_info.general_tracks:
        naudio = track.count_of_audio_streams

    # print(err)

    naudio=int(naudio)
    if c < 12+(naudio*2):
        e=12+(naudio*2)-c
        # print (e , "erreur(s)")

        with open("logs.txt",mode='a',encoding = 'utf-8')as f:
            f.write("\n")
            f.write("----------")
            f.write("\n")
            f.write("Rapport au " + now.strftime("%Y-%m-%d %H:%M:%S\n"))
            f.write(str(file) + "\n")
            f.write("Duration: " + str(track.other_duration[4]) + "\n")
            f.write(str(e) + "erreur(s)\n")
            f.write("\n".join(err))
            f.write("\n")
            f.write("----------\n")
            f.close
        return 'false'

    else:
        # print ("fichier sans erreur")
        with open("logs.txt",mode='a',encoding = 'utf-8')as f:
            f.write("\n")
            f.write("----------")
            f.write("\n")
            f.write("Rapport au " + now.strftime("%Y-%m-%d %H:%M:%S\n"))
            f.write(str(file) + "\n")
            f.write("Duration: " + str(track.other_duration[4]) + "\n")
            f.write("fichier sans erreur\n")
            f.write("----------\n")
            f.close
        # print ("\n")
        return 'true'