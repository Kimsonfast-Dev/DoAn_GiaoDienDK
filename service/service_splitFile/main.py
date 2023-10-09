import sys
sys.path.append("./")


from service.service_splitFile.api.service_splitFile import sv_splitFile

main = sv_splitFile()
def convertFile(linkfile):
    main.convert_allFile(linkfile)