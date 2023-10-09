from service.service_controll.tool.tool_mapping import mapping
from tkinter import filedialog

hello = mapping(6,11)

def convert_mode(mode,x,y):
    x = float(x)*0.1
    y = float(y)*0.1
    return x,y

def convert_milling_to_cnc(x,y):
    dao_x = 165 
    dao_y = 255
    x_hole_tb = 165+10
    y_hole_tb = 255-10
    x_cnc = x - dao_x + x_hole_tb + 75
    y_cnc = y + dao_y - y_hole_tb + 30
    x_cnc = round(x_cnc,2)
    y_cnc = round(y_cnc,2)
    return x_cnc,y_cnc

def update_mapping():
    f_list = open("service/service_controll/data/data_cnc/list_leveling.txt")
    var = []
    for data in f_list:
        data = data.split("\n")[0]
        x = float(data.split(",")[0])
        y = float(data.split(",")[1])
        z = float(data.split(",")[2])
        var.append([x,y,z])
    hello.input_list(var)
    hello.update_listcheck()

def convert_file(link_file,mode_file):
    z_lv_mapping = int(open("service/service_controll/data/data_cnc/value_lv_mapping.txt").readline().split("\n")[0])
    z_lv_current = int(open("service/service_controll/data/data_cnc/value_lv_current.txt").readline().split("\n")[0])
    f = open(link_file)
    filename = "service/service_controll/data/data_runfile/" + str(link_file).split("/")[-1]
    f_file = open(filename,'w')
    type_temp = 0
    count = 0
    for data in f:
        data = data.split("\n")[0]
        cm = data.split(",")[0]
        if(cm !="change"):
            x = float(data.split(",")[1])
            y = float(data.split(",")[2])
            x,y = convert_mode(mode_file,x,y)
            x_cnc,y_cnc = convert_milling_to_cnc(x,y)
            z = z_lv_mapping - hello.check_full(x_cnc,y_cnc) + z_lv_current
            z = int(z+5)#int(round(z/10)*10)+10
            line = cm + "," + str(x_cnc) + "," + str(y_cnc) + "," + str(z) + "\n"

            if(cm == "move"):
                f_file.write("move_ready,0,0,0\n")
                line = "move_xy_cnc"+ "," + str(x_cnc) + "," + str(y_cnc) + ",32\n"
                f_file.write(line)
                f_file.write("settime,100,0,0\n")
                f_file.write("move_z_blu,"+ str(z) +",0,0\n")
                f_file.write("settime,200,0,0\n")
            elif(cm == "bit"):
                line = "xyz" + "," + str(z) + "," + str(x_cnc) + "," + str(y_cnc)  + ",\n"
                f_file.write(line)

            elif(cm == "movedrill"):
                f_file.write("move_ready,0,0,0\n")
                line = "move_xy_cnc"+ "," + str(x_cnc) + "," + str(y_cnc) + "32\n"
                f_file.write(line)
                f_file.write("move_hole,0,0,0\n")
                f_file.write("move_ready,0,0,0\n")
            else:
                None
        else:
            type = int(data.split(",")[1][-1])
            if(count != 0):
                f_file.write("open," + str(type_temp) +"\n")
                f_file.write("block," + str(type)+"\n")
            else:
                f_file.write("block," + str(type)+"\n")
            count = count + 1
            type_temp = type

            
    if(count !=0):
        f_file.write("open," + str(type_temp) +"\n")

    f.close()
    f_file.close()



