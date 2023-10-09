import sys
sys.path.append("./")


import os

def reset_folder(link_folder):
    listfie = os.listdir(link_folder)
    for filename in listfie:
        linkfile = link_folder + "/" + filename
        os.remove(linkfile)

