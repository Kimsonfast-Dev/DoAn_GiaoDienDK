import sys
sys.path.append("./")


def create(name):
    link = "Font_app/tab_app/" + name + ".py"
    open(link,"a").close()

    f      = open("Font_app/tab_app/doc/code_blank.py","r")
    f_copy = open(link,"w")

    for data in f:
        f_copy.write(data)

    f.close()
    f_copy.close