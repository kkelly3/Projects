# -*- coding: utf-8 -*-
"""
Kaitlin Kelly
This is the ViewData.py script.
It will get data from the raspberry pi based on the ip address and plot it if requested.
"""

sensor_data=[]
def validData(time:str=None,pot=None,sonic=None):
    """
    This function will make sure that all the data from the file is valid

    Parameters
    ----------
    time : str, optional
        make sure time is there
    pot : TYPE, optional
        make sure pot can be a float
    sonic : TYPE, optional
        make sure sonic can be a float

    Returns
    -------
    bool
        if line is valid or not.

    """
    if pot==None or time==None or sonic==None:
        return False
    try:
        angle=float(pot)
        dist=float(sonic)
        try:
            dateName(time)
        except:
            return False
        return True
    except:
        return False

def dateName(dt_str):
    """
    This function gets the datestring and returns it in a new format 

    Parameters
    ----------
    dt_str : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    date_sorted=[]
    string_sort=''
    i=0
    j=0
    while i<len(dt_str):
        if dt_str[i]=='_' or dt_str[i]=='/' or dt_str[i]==':' or dt_str[i]=='.':
            j=j+1
            date_sorted.append(string_sort)
            string_sort=''
        else:
            string_sort=string_sort+dt_str[i]
        i=i+1
    date_sorted.append(string_sort)
    months=['January','February','March','April','May','June','July','August','September','October','November','December']
    month=int(date_sorted[0])
    day=int(date_sorted[1])
    year=int(date_sorted[2])
    hours=int(date_sorted[3])
    
    minutes=int(date_sorted[4])
    sec=int(date_sorted[5])
    hours=int(date_sorted[6])
    
    date_send=""
    
    date_send=months[month+1]+", "+str(day)+", "+str(year)
    return date_send
    
    
def changeDate(date_string):
    """
    This function will get the date from the string give and return a datetime type

    """
    import datetime
    valid=False
    try:   

        i=0
        j=0
        date_sorted=[]
        string_sort=''
        while i<len(date_string):
            if date_string[i]=='_' or date_string[i]=='/' or date_string[i]==':' or date_string[i]=='.':
                j=j+1
                date_sorted.append(string_sort)
                string_sort=''
            else:
                string_sort=string_sort+date_string[i]
            i=i+1
        date_sorted.append(string_sort)

        month=int(date_sorted[0])
        day=int(date_sorted[1])
        year=int(date_sorted[2])
        hour=int(date_sorted[3])
        
        minute=int(date_sorted[4])
        second=int(date_sorted[5])
        
        microsecond=int(date_sorted[6])*1000
        #print(month,day,year)
        date=datetime.datetime(year,month,day,hour,minute,second,microsecond)
        #print(date)
            
        return date

    except:
        valid=False
    
    if valid==True:
        return valid,date
    else:
        return valid,''
    
def plot_data(data,fname):
    """
    This function will plot percentage (based on angles) against time and distance against time.

    Returns
    -------
    None.

    """
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import os
    import numpy as np
    import datetime as datetime
    date_list=[]
    angles=[] #percentages based on angle
    distances=[]
    temp=[]
    
    size=os.stat(fname).st_size
    try:
        how_big=int(size)
    except:
        print("File not found")
        return
    try:
        if len(data)==0:
            print("File Empty")
            return
    except:
        print("File Empty")
        return
    how_long=round(10*how_big/1000000,2)
    print("It may take: {} minutes before the graph is finished plotting.".format(how_long))
    #get data
    for i in data:
        if i[0]['Time']!=None and i[0]['Time']!='':
            date_list.append(i[0]['Time'])
            if i[1]['Potentiometer']!=None and i[1]['Potentiometer']!='':
                angles.append(float(i[1]['Potentiometer']))
            if i[2]['Distance']!=None and i[2]['Distance']!='':
                distances.append(float(i[2]['Distance']))
    
    date_fmt=None
    new_dt_list=[]
    #dt_str=[]
    #print(date_list)
    for i in range(0,len(date_list)):
        date_fmt=changeDate(date_list[i])
        new_dt_list.append(date_fmt)
        #times=datetime.datetime.strptime(date_list[i],"%m/%d/%Y_%H:%M:%S.%f")[:-3]
        #dt_str.append(times)
    #dt_str=np.array(new_dt_list,dtype='datetime64[ms]')
    
    time_started=dateName(date_list[0])
    #time_started=datetime.datetime.strptime(str(new_dt_list[0]),"%Y-%m-%d %H:%M:%S.%f")
    tm_st="Date Ran: "+str(time_started)
    #print(tm_st)
    print("Plotting is now started.")
    plt.subplot(211)
    plt.title(tm_st)
    #datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')

    
    plt.plot(new_dt_list,angles,label="Potentiometer ",color='paleturquoise',)

    #plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=120))
    #plt.xlabel('Month, Day, Year, Hour:Minute:Seconds.Milliseconds')
    plt.ylabel('Percentage (%)')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S.%f'))
    plt.xlabel('Time (Hour:Minute:Seconds.Milliseconds)')
    temp=sorted(angles)
    plt.ylim(bottom=temp[0]-1,top=temp[len(temp)-1]+1)
    plt.xlim(left=new_dt_list[0],right=new_dt_list[len(new_dt_list)-1])
    plt.xticks(rotation=45)
    plt.legend(loc=2)
    plt.subplot(212)
    #plt.title("Distance")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S.%f'))
    plt.plot(new_dt_list,distances,label="Ultrasonic Sensor ",color='paleturquoise',)
    plt.xlabel('Time (Hour:Minute:Seconds.Milliseconds)')
    plt.ylabel('Distance (cm)')
    plt.xlim(left=new_dt_list[0],right=new_dt_list[len(new_dt_list)-1])
    plt.xticks(rotation=45)
    plt.legend(loc=2)
    plt.tight_layout()
    fig=plt.gcf() #save plt img
    
    print("Plotting is now complete.")
    plt.show()
    img=input("Would you like to save this file (y/n)?")
    if img=='y' or img=='Y':
        import re
        named=re.search("(.+)(.csv|.txt)",fname)
        try:
            img_name=named.group(1)+".png"
            fig.savefig(img_name) #save plt img with file name+.png
        except:
            print("Graphs could not be saved.")
    elif img=='n' or img=='N':
        print("You have chosen not to save these graphs.")
    else:
        print("You chose neither y nor n. The graphs were not saved.")
    
def importFile(text_op:str=None):
    """
    This will allow user to import new csv or text file <FileToImport> in correct format
    
    Returns
    -------
    None.

    """
    import re
    import csv
    import platform
    #print(text_op)
    file_csv=''
    file_txt=''

    #get system type to type local path
    os_sys=platform.system()
    if os_sys=="Windows":
        local_path="\\"
    else:
        local_path="/"
        
    #find filename
    file_txt=re.search('(\w+.txt)', text_op)
    file_csv=re.search('(\w+.csv)', text_op)
    
    new_data=[]
    valid=False
    
    if file_txt!=None:
        #print('.txt')
        filename='DataFiles'+local_path+file_txt.group(1)
    elif file_csv!=None:
        #print('.csv')
        filename='DataFiles'+local_path+file_csv.group(1)
    else:
        filename=''
    #print(filename)
    valid = False
    #get data in filenames if possible
    try:
        #print("at import w/ filename: ",filename)
        if '.txt' in filename:
            with open(filename,'r',newline='') as f:
                #data=f.read()
                
                f.seek(0)
                reader = csv.DictReader(f)
                for row in reader:                
                    new_data.append([row['Time'],row['Potentiometer'],row['Distance']])
            #print(new_rec)

        if '.csv' in filename:
            #print("It is csv")
            
            with open(filename,'r',newline='') as csvfile:
                #read pointer
                csvfile.seek(0)
                reader = csv.DictReader(csvfile)

                for row in reader:
                    new_data.append([row['Time'],row['Potentiometer'],row['Distance']])
            #print(new_rec)
            
        #it was able to read file
        valid=True
            
    except:
        print("File {} was not found".format(filename))
        valid=False
    categories=['Time','Potentiometer','Distance']
    
    if valid==True:
        for i in range(0,len(new_data)):
            for j in range(0,len(categories)-1):
                if new_data[i][j]=='':
                    new_data[i][j]=None
            
            valid=validData(new_data[i][0],new_data[i][1],new_data[i][2])
            #print(new_rec[i])
            
            if valid==False:
                #print(valid)
                print("Time: {} appears to contain invalid data".format(new_data[i]))
                break
    
    
    record_appended=False
    s_data=[]
    #print(valid,len(new_rec))
    repeat_found=False
    if valid==True: 
        #print("It is valid")
        for i in range(0,len(new_data)):
            s_data.append([{categories[0]:new_data[i][0]},{categories[1]:new_data[i][1]},{categories[2]:new_data[i][2]}])
            #print(location)
        global sensor_data
        sensor_data=s_data.copy()
    else:
        print("It seems your file contains invalid data. Please try again with valid data.")
        print("Data should be date time, float, float")
        return -1

    return filename
 
def getFolder(ip_addr:str="",file_loc:str="/home/pi/Documents/",file=False):
    """
    If the file does not already exist or if it is a folder, this function will get it from the raspberry pi.

    Parameters
    ----------
    ip_addr : str, optional
        DESCRIPTION. The default is "".
    file_loc : str, optional
        DESCRIPTION. The default is "/home/pi/Documents/".
    file : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    import os
    import platform
    import sys
    
    path="ssh pi@"+ip_addr+" exit"
    try:
        #print("Here")
        check=os.system(str(path))
        #print("After")
        #print(check)
        if check!=0: #invalid ip address
            print("Please check ip address")
            #sys.exit()
            return 0
            #exit()
        #os.system("$exit")
    except OSError as err:
        print("Error:",err)
    except:
        #print("error")
        sys.exit("Could not connect")
    
    #get system type to type local path
    os_sys=platform.system()
    if os_sys=="Windows":
        local_path=" .\\DataFiles"
    else:
        local_path=" ./DataFiles"
        
    isFolder=os.path.isfile("DataFiles")
    if isFolder==False:
        os.system("mkdir DataFiles")


    #path name needed to get the pi data
    if file==True:
        path="scp pi@"+ip_addr+":"+file_loc+local_path
    else:
        path="scp -r pi@"+ip_addr+":"+file_loc+local_path
    #print(path)
    
    #check file
    try:
        print("Transfer has Started")
        check=os.system(str(path))
        #os.system("scp pi@raspberrypi:/home/pi/Documents/ECE592_651/Finals_proj/22_July_2021_22_44_1627008255_727.csv ./")
        if check==1:
            print("File not found")
            #sys.exit("File or folder was not found")
            return -1
    except OSError as err:
        print("Error:",err)
        return -1
    except:
        print("Could not find the file or folder given.")
        return -1
    # except SCPException as e:
    #     print("File may not exist, ",e)
        
    
    print("Transfer Complete")
def fileExist(text_op:str=None):
    """
    This will check if a csv or text file already exists in the DataFiles folder.
    
    Returns
    -------
    True means that the file does exist, False means that the file does not exist.

    """
    import re
    import csv
    import platform
    #print(text_op)
    file_csv=''
    file_txt=''

    #get system type to type local path
    os_sys=platform.system()
    if os_sys=="Windows":
        local_path="\\"
    else:
        local_path="/"
        
    #find filename
    file_txt=re.search('(\w+.txt)', text_op)
    file_csv=re.search('(\w+.csv)', text_op)
    
    if file_txt!=None:
        #print('.txt')
        f_hold=file_txt.group(1)
        filename='DataFiles'+local_path+file_txt.group(1)
    elif file_csv!=None:
        #print('.csv')
        f_hold=file_csv.group(1)
        filename='DataFiles'+local_path+file_csv.group(1)
    else:
        filename=''

    existing=0
    #get data in filenames if possible
    try:
        #print("at import w/ filename: ",filename)
        if '.txt' in filename:
            with open(filename,'r',newline='') as txtfile:
                print("File {} already exists".format(f_hold))
                existing=1
                
        if '.csv' in filename:
            #print("It is csv")
            
            with open(filename,'r',newline='') as csvfile:
                print("File {} already exists".format(f_hold))
                existing=1
            
    except:
        #print("File {} was not found".format(filename))
        existing=0
    return existing
    
        
def parse(args):
    """
    This function will make sure that the arguments given are all valid. Once determining that they are in a valid format, it will go through the arguments. If the ip address is valid or not, if the input number is valid(0/1),if it is a folder or a file that needs to be retrieved, if a file already exists or not, import the file if not, then plot data assuming it is valid.

    """
    import sys
    import re
    
    #print(len(args))
    #order: ip_addr,plot 0/1,filename path
    has_fname=False #if it has a filename or not
    
    #Check formatting 
    if len(args)<2 or len(args)>3:
        print("Invalid format detected")
        sys.exit(0)
    else:
        if len(args)==2:
            ip_addr=args[0]
            tran_plot=args[1]
            #filepath=None
        elif len(args)==3:
            ip_addr=args[0]
            tran_plot=args[1]
            filepath=args[2]
            count=re.findall('[.]',filepath)
            if len(count)>1:
                print("When giving a filename, please have format: /file_location/filename.file_extention")
                sys.exit(0)
            elif len(count)==1:

                #find filename
                file_txt=re.search('(\w+).txt', filepath)
                file_csv=re.search('(\w+).csv', filepath)

                if file_txt!=None and file_txt!="":
                    has_fname=True
                elif file_csv!=None and file_csv!="":
                    has_fname=True
                else:
                    print("ERROR: Invalid file extention. File extention must be .csv or .txt")
                    sys.exit(0)
            else: #no extention
                has_fname=False
    
        else:
            print("Invalid format detected")
    
    
    #is ip address valid?
    try:
        ip_check=re.search("(\d+[.]\d+[.]\d+[.]\d+)",ip_addr)
        ip_hold=ip_addr.replace(ip_check.group(1),'')
        if ip_hold.strip()!='':
            print("Invalid IP address given.")
            sys.exit(0)
    except:
        print("IP address is invalid. IP address should be similar to: 192.168.1.101")
    
    #is the input number value valid
    try:
        plotting=int(tran_plot)
        if plotting!=0 and plotting!=1:
            print("Number must be a 1 or 0 to determine if a file will be plotted(1) or not(0)")
            print("Format: <ip_addr> <num_0_or_1> <file_path>")
            return 0
        
    except:
        print("Please include a 1 or 0 to determine if a file will be plotted(1) or not(0)")
        print("Format: <ip_addr> <num_0_or_1> <file_path>")
        sys.exit(0)
        
    #if it is supposed to plot, does it have a filename?
    if plotting==1 and has_fname==False:
        print("ERROR: Filename needed. When giving a filename, please have format:")
        print("/file_location/filename.file_extention")
        print("*NOTE: File extentions can be .txt or .csv")
        sys.exit(0)
        
    check_folder=0
    if len(args)==2:
        check_folder=getFolder(ip_addr=ip_addr,file=False)
    else:
        existing=fileExist(filepath)
        if existing==0:
            #file doesn't exist yet
            #if there are only 2 arguments use the default
            check_folder=getFolder(ip_addr, filepath,has_fname)
            
    if check_folder==-1:
        return 0
    if plotting==1:
        
        fname=importFile(filepath)
        if fname!=-1:
            global sensor_data
            plot_data(sensor_data,fname)



def main():
    """
    Calls parse and gives it the arguments.
    """
    import sys
    inputs=sys.argv
    inputs=inputs[1:len(inputs)]
    #print(inputs)

    parse(inputs)
if __name__ == "__main__":
    main()
    