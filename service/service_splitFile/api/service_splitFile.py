import sys
sys.path.append("./")

class sv_splitFile():
    def __init__(self) -> None:
        None

    def convert_info(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/1,info_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/1,info_ct.txt",'w')
        for data in f:
            if(data == "#PR_LINE_MILLING\n"): 
                break
            f_file.write(data)
        f_file.close()
        f.close()

    def convert_millingline(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/2,millingline_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/2,millingline_ct.txt",'w')
        i = 0
        for data in f:
            if(data == "#PR_FACE_MILLING\n"): 
                break

            if(i==1):
                f_file.write(data)

            if(i==0):
                if(data == "#PR_LINE_MILLING\n"):
                    i = 1
        f_file.close()
        f.close()        

    def convert_millingface(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/3,millingface_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/3,millingface_ct.txt",'w')
        i = 0
        for data in f:
            if(data == "#PR_FOOT_MILLING\n"): 
                break

            if(i==1):
                f_file.write(data)

            if(i==0):
                if(data == "#PR_FACE_MILLING\n"):
                    i = 1
        f_file.close()
        f.close()        

    def convert_millingfoot(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/4,millingfoot_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/4,millingfoot_ct.txt",'w')
        i = 0
        for data in f:
            if(data == "#PR_DRILL_HOLE\n"): 
                break

            if(i==1):
                f_file.write(data)

            if(i==0):
                if(data == "#PR_FOOT_MILLING\n"):
                    i = 1
        f_file.close()
        f.close()      

    def convert_drillhole(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/5,drillhole_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/5,drillhole_ct.txt",'w')
        i = 0
        for data in f:
            if(data == "#PR_LINE_CUTTING\n"): 
                break

            if(i==1):
                f_file.write(data)

            if(i==0):
                if(data == "#PR_DRILL_HOLE\n"):
                    i = 1
        f_file.close()
        f.close()     


    def convert_cuttingline(self,linkfile):
        f = open(linkfile,"r")
        open("service/service_splitFile/data/output/6,cuttingline_ct.txt",'a').close()
        f_file = open("service/service_splitFile/data/output/6,cuttingline_ct.txt",'w')
        i = 0
        for data in f:
            if(i==1):
                f_file.write(data)

            if(i==0):
                if(data == "#PR_LINE_CUTTING\n"):
                    i = 1
        f_file.close()
        f.close()   

    def convert_allFile(self,linkfile):
        self.convert_info(linkfile)
        self.convert_millingline(linkfile)
        self.convert_millingface(linkfile)
        self.convert_millingfoot(linkfile)
        self.convert_drillhole(linkfile)
        self.convert_cuttingline(linkfile)



