import os, zipfile

dir_name = "D:/oleic/arcade.oleic.co/allgamefiles/codecanyon-Uj6ffWHF-101-game-html5-game-bundle-construct-23/101GAMES/Games/collection2"

extension = '.zip'

# os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop throught items in dir
    if item.endswith(extension): # check for ".zip" externsion
        file_name = dir_name + "/" + item # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file