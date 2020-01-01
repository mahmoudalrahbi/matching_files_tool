#|##########################################################|##
# Matching files tool aims to help in finding files that    |##
# not have a corresponding file and delete it or copy       |##
# the files which have a corresponding file.                |##
#                                                           |##
# written by @mahmoudalrahbi                                |##
#|##########################################################|##


import argparse
import glob
import os
import shutil 
from tqdm import tqdm


#################################################################################

def check_corresponding_files(dir1, dir2, ext1, ext2):
#|##########################################################|##
#| check_corresponding_files()                              |##
#| check if each files in both direcories have corresponding|##
#| files in the other direcory and show the files with      |##
#| no corresponding file                                    |##
#|##########################################################|##
    c=0 #count files that does not have corresponding files
    no_matching_files_dir1 =[] # no matching file in fiest directory
    no_matching_files_dir2 =[] # no matching file in second directory 
 
    print("\n")
    pbar = tqdm(glob.glob(os.path.join(dir1, "*."+ext1)))# prepare progress bar
    for filename in pbar:
        f,_ = filename.split('.')
        lastName=os.path.basename(os.path.normpath(f))
        corespondingFiles = os.path.join(dir2, lastName + '.'+ext2)

        if not os.path.exists(corespondingFiles):
            #print(corespondingFiles + " not exist")
            no_matching_files_dir1.append(lastName + '.'+ext1)
            c+=1
        pbar.set_description(lastName+ '.'+ext1)#upade description for progress bar

    print("\n")
    pbar = tqdm(glob.glob(os.path.join(dir2, "*."+ext2)))# prepare progress bar
    for filename in pbar:
        f,_ = filename.split('.')
        lastName=os.path.basename(os.path.normpath(f))
        corespondingFiles = os.path.join(dir1, lastName + '.'+ext1)

        if not os.path.exists(corespondingFiles):
            #print(corespondingFiles + " not exist")
            no_matching_files_dir2.append(lastName + '.'+ext2)
            c+=1
        pbar.set_description(lastName+ '.'+ext2)#upade description for progress bar

    num = len(no_matching_files_dir1)
    if num > 0:   
        print("%d files without cressponding file in %s"%(num ,dir1))
        for file in no_matching_files_dir1:
            print(file)
        print("--------------------------------------------------------------")


    num = len(no_matching_files_dir2)
    if num > 0:
        print("%d files without cressponding file in %s"%(num,dir2))
        for file in no_matching_files_dir2:
            print(file)
        print("--------------------------------------------------------------")
    print("%d files does not have corresponding files"%c)
    print("--------------------------------------------------------------")
    


    #end of check_corresponding_files()
#################################################################################

#################################################################################

def delete_files(dir1, dir2, ext1, ext2):
#|##########################################################|##
#| delete_files()                                           |##
#| delete files in dir1 which does not have corresponding   |##
#| files  in dir2                                           |##
#|                                                          |##
#|##########################################################|##
    c=0 #count files that does not have corresponding files
    deleted_files=[]
    pbar = tqdm(glob.glob(os.path.join(dir1, "*."+ext1))) # prepare progress bar
    for filename in pbar: #loop through files
        f,_ = filename.split('.')
        lastName=os.path.basename(os.path.normpath(f))
        corespondingFiles = os.path.join(dir2, lastName + '.'+ext2)

        if not os.path.exists(corespondingFiles):
            #print(corespondingFiles + " not exist")
            c+=1
            os.remove(filename)
            #print(filename + " is deleted")
            deleted_files.append(lastName+ '.'+ext1)
        pbar.set_description(lastName+ '.'+ext1)#upade description for progress bar

    num = len(deleted_files)
    if num > 0:
        print("%d files are deleted from directory %s"%(num,dir1))
        for file in deleted_files:
            print(file)
        print("--------------------------------------------------------------")

    #end of delete_files()
#################################################################################

#################################################################################

def copy_files(dir1, dir2, ext1, ext2,distnation):
#|##########################################################|##
#| copy_files()                                             |##
#| copy files in dir1 which have  corresponding             |##
#| files  in dir2 (copy it into distnation directory)       |##
#|                                                          |##
#|##########################################################|##
    c=0
    pbar = tqdm(glob.glob(os.path.join(dir1, "*."+ext1))) # prepare progress bar
    for filename in pbar:
        f,_ = filename.split('.')
        lastName=os.path.basename(os.path.normpath(f))
        corespondingFiles = os.path.join(dir2, lastName + '.'+ext2)

        if os.path.exists(corespondingFiles):
            shutil.copy(filename,distnation)
            c+=1
            #print("%d -%s copy into %s"%(c,filename,distnation) )
        
        pbar.set_description(lastName+ '.'+ext1)#upade description for progress bar

    print("%d files are copied into %s from %s"%(c ,distnation,dir1))
    print("--------------------------------------------------------------")








#prepare argument come from command line
parser = argparse.ArgumentParser()
parser.add_argument("-dir1",help="set the first Directory")# first directory
parser.add_argument("-dir2",help="set the second Directory")# second directory
parser.add_argument("-ext1",help="set the first extintion")# extition of files in first directory
parser.add_argument("-ext2",help="set the second extintion")# extition of files in second directory

#accept one argument only of these
deleteArg = parser.add_mutually_exclusive_group()
#delete the files with no coressponding files in both directories
deleteArg.add_argument("-delete_both",help="delete files which does not have corresponding files from the both directories",action="store_true")
#delete the files with no coressponidng files from first directory only
deleteArg.add_argument("-delete_dir1",help="delete files which does not have corresponding files form the dir1",action="store_true")
#delete the files with no coressponidng files from second directory only
deleteArg.add_argument("-delete_dir2",help="delete files which does not have corresponding files form the dir2",action="store_true")


#accept one argument only of these
copyArg = parser.add_mutually_exclusive_group()
#copy the files which have coressponding files from both directory to the specfied directory
copyArg.add_argument("-copy_both",help="copy the fils which have corresponding files from both(dir1,dir2) to specfied directory")
#copy the files which have coressponding files from first directory only to the specfied directory
copyArg.add_argument("-copy_dir1",help="copy the fils which have corresponding files from (dir1) to specfied directory")
#copy the files which have coressponding files from both directory to the specfied directory
copyArg.add_argument("-copy_dir2",help="copy the fils which have corresponding files from (dir2) to specfied directory")


args = parser.parse_args() #get the passed arguments


if not args.dir1 or not args.dir2 or not args.ext1 or not args.ext2: #check the existing of required arguments
    parser.error("you have to file the required fields [dir1][dir2][ext1][ext2]")

dir1 = args.dir1 
dir2 = args.dir2
ext1 = args.ext1
ext2 = args.ext2


deleteDir = None
if args.delete_both:
    deleteDir = "both"
elif args.delete_dir1:
    deleteDir = "dir1"
elif args.delete_dir2:
    deleteDir = "dir2"



copyDir = None
if args.copy_both:
    copyDir = "both"
elif args.copy_dir1:
    copyDir = "dir1"
elif args.copy_dir2:
    copyDir = "dir2"

#check the exsting of corresponding files
if deleteDir == None and copyDir == None:
    check_corresponding_files(dir1, dir2, ext1, ext2)
    #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg


#logic for deleting files
if deleteDir =="dir1":
    ans = input("Are you sore do you want to delete some files from %s (Y/N)? "%dir1)
    if ans =="Y" or ans== "y": 
        delete_files(dir1, dir2, ext1, ext2)
    #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -delete_dir1
elif deleteDir =="dir2":
    ans = input("Are you sore do you want to delete some files from %s (Y/N)? "%dir2)
    if ans =="Y" or ans== "y": 
        delete_files(dir2, dir1, ext2, ext1)
        #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg  -delete_dir2
elif deleteDir == "both":
    ans = input("Are you sore do you want to delete some files from %s and %s(Y/N)? "%(dir1 ,dir2))
    if ans =="Y" or ans== "y": 
        delete_files(dir1, dir2, ext1, ext2)
        delete_files(dir2, dir1, ext2, ext1)
        #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -delete_both



#login for copying files

if copyDir =="dir1":
    if os.path.exists(args.copy_dir1):
        copy_files(dir1, dir2, ext1, ext2,args.copy_dir1)
    else:
        print("%s directory not exist"%args.copy_dir1)
    #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -copy_dir1 d3
elif copyDir =="dir2":
    if os.path.exists(args.copy_dir2):
        copy_files(dir2, dir1, ext2, ext1,args.copy_dir2)
    else:
        print("%s directory not exist"%args.copy_dir2)
        #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -copy_dir2 d3
elif copyDir == "both":
    if os.path.exists(args.copy_both):
        copy_files(dir1, dir2, ext1, ext2,args.copy_both)
        copy_files(dir2, dir1, ext2, ext1,args.copy_both)
    else:
        print("%s directory not exist"%args.copy_both)
        #python main.py -dir1 d1 -ext1 xml -dir2 d2 -ext2 jpg -copy_both d3
#delete_files(deleteDir)
#copy_files(copyDir)
