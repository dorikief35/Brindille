from distutils import errors
from fileinput import filename
import shutil
import os
import time
import datetime
import pathlib
from pymediainfo import MediaInfo
import test_MOV
import test_MXF
import csv

# Save paths in a csv file
def savePath(watchfolder, xdcam, prores, refuse):
    pathlist = [watchfolder, xdcam, prores, refuse]
    with open("paths.csv",'w')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pathlist)

# Message for files that can't be moved
def cantMove(file, destinationPath):
    now = datetime.datetime.now()
    with open("logs.txt",mode='a',encoding = 'utf-8')as f:
                f.write("\n")
                f.write("----------")
                f.write("\n")
                f.write("Rapport au " + now.strftime("%Y-%m-%d %H:%M:%S\n"))
                f.write(str(file) + "\n")
                f.write("File already exists in destination folder:\n")
                f.write(str(destinationPath) + "\n")
                f.write("\n")
                f.write("----------\n")
                f.close

# Main function
def principale(watchfolder, xdcam, prores, refuse):

    # Save paths in a csv file
    savePath(watchfolder, xdcam, prores, refuse)
    
    # List of files in watchfolder
    files = os.listdir(watchfolder)

    # File formats list 
    xdcam_format=['.mxf']
    prores_format=['.mov']

    # Set the current time
    now = datetime.datetime.now()

    # Test files in watchfolder
    for file in files:
        file_path= watchfolder + '/' + file
        #print(file_path)
        file_ext=pathlib.Path(file).suffix
        # print(file)
        # print(file_ext)
        # print(file_path)

        # Test if file is a XDCAM file
        if file_ext in xdcam_format:
            state_xdcam = test_MXF.MXF(file_path,file)

            if state_xdcam =='true':
                
                # Move the file to the xdcam folder
                try:
                    shutil.move(file_path,xdcam) 
                    # print("OK XDCAM")
                except:
                    cantMove(file, xdcam)

            else :
                
                # Move the file to the refuse folder
                try:
                    shutil.move(file_path,refuse)
                    # print("XDCAM not OK")
                except: 
                    # print("XDCAM already exists")
                    cantMove(file, refuse) 
        
        # Test if file is a ProRes file
        elif file_ext in prores_format:
            state_prores = test_MOV.MOV(file_path,file)

            if state_prores == 'true':
                
                # Move the file to the prores folder
                try:
                    shutil.move(file_path,prores) 
                    # print("OK PRORES")
                except:
                    # print("PRORES already exists")
                    cantMove(file,prores)

            else :
                
                # Move the file to the refuse folder
                try:
                    shutil.move(file_path,refuse) 
                    # print("PRORES not OK")
                except:
                    # print("PRORES already exists")
                    cantMove(file,refuse)

        # Extension not in the list 
        else:
            with open("logs.txt",mode='a',encoding = 'utf-8')as f:
                f.write("\n")
                f.write("----------")
                f.write("\n")
                f.write("Rapport au " + now.strftime("%Y-%m-%d %H:%M:%S\n"))
                f.write(str(file) + "\n")
                f.write("Extension non conforme")
                f.write("\n")
                f.write("----------\n")
                f.close

            # Move the file to the refuse folder
            try:
                shutil.move(file_path,refuse)
                # print("Non conforme")
            except:
                # print("Already exists in refuse folder")
                cantMove(file,refuse)




        