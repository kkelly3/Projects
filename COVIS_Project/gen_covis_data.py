# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:37:56 2021

@author: klkel
"""


#person number-8 dig, default:largest+1
#record date: Month, dd, year (June, 05, 2020)
#age: float
#gender: unspecified,male,female
#vaccination status
#type: empty, pfizer,moderna,j&j
#1st vaccine date: month, dd, year
#2nd vaccine date: month, dd, year
#email string
#notes

#unique pno
#dates valid
#status has to b r,p, or f
#dates have to be after jan 2020 and can't b in future
#email needs format correct <username@domain name> domain name should be <string.string>
#create dict obj for vstat,gen,vtype, maintain dict obj so new types can b added
#vtype = vaccine[amount of shots, days btwn needed]
#dates given should be valid


#-no = num of randomppl generated in file with filename
#if no arg given, gen 100,000 rec default and save in new file covid vaccine data.csv

import numpy as np
VType={'Pfizer':[2,21],'Moderna':[2,28],'J&J':[1,0]}
Gen={'U':'Unspecified','M':'Male','F':'Female'}
VStatus={'R':'Registered but not Vaccinated','P':'Partially Vaccinated','F':'Fully Vaccinated'}

def makeCSV(num:int=100000,filename:str="covidVaccineData.csv"):
    import csv
    import random
    import datetime
    import string
    
    #print("num: {}, file: {}".format(num,filename))
    #rand gen for each record
    #all attributes pass checks in prev slide
    #have header w/attr keys listed on slide 3
    #try keep ratios of gender case, vac rate, partially and fully vac ppl same as real nc data
    #https://covid19.ncdhhs.gov/dashboard/vaccinations
    #as of 6/6/2021
    #fully vax = 36.6% nc
    #part vax=43.7%
    #https://covid19.ncdhhs.gov/dashboard/vaccinations
    start_date=datetime.date(2021,1,1)
    today=datetime.date.today()
    time_btwn_days=today-start_date
    
    #high peaks for 1/11-1/25(med),3/1-4/5 (highest),5/10/24 (low)
    #every other percentage is lower
    
    day_grouping=[list(np.arange(0,10)),list(np.arange(10,24)),list(np.arange(24,59)),list(np.arange(59,94)),list(np.arange(94,129)),list(np.arange(129,143)),list(np.arange(143,1+time_btwn_days.days))]
    
    #email domain names
    domain=['gmail.com','yahoo.com','aol.com','ncsu.org','rti.com','cat.net']

    letters = string.ascii_letters    #letters (a-z and A-Z) for email
    letters = letters+'_0123456789'

    
    #based on https://public.tableau.com/views/NCDHHS_COVID-19_Dashboard_Vaccinations/Demographics?%3AshowVizHome=no
    age_grouping=[list(np.arange(0,12)),list(np.arange(12,18)),list(np.arange(18,25)),list(np.arange(25,50)),list(np.arange(50,65)),list(np.arange(65,75)),list(np.arange(75,100))]
    
    #print(age_grouping[0])
    
    vac_stat={}
    global VStatus
    vac_stat=VStatus.copy()
    status=[]
    for i in vac_stat.keys():
        status.append(i)
    #print(status)
    vaccine_type={}
    global VType
    vaccine_type=VType.copy()
    vaccines=[]
    for i in vaccine_type.keys():
        vaccines.append(i)
    
    gender_op={}
    global Gen
    gender_op=Gen.copy()
    genders=[]
    for j in gender_op.keys():
        genders.append(j)
    
    k=0
    record=[]
    
    v_state=np.random.choice(status,num,p=[.21,.43,.36])
    #print(v_state)
    invalid=False
    while k<num:
        invalid=False
        #rand gen num
        
        vdt1=''
        vdt2=''
        vaccine=''
        
        #get rdt
        days_btwn1=random.randrange(time_btwn_days.days)
        
        rdt=start_date+datetime.timedelta(days=days_btwn1)        
        rdt_hold=rdt.strftime("%B, %d, %Y")
        Rdt=rdt_hold.replace('-', ', ')

        
        vaccine_state=v_state[k]


        #get age        
        if vaccine_state=='R':
            age_group=np.random.choice(len(age_grouping),1,[.14,.08,.09,.33,.19,.1,.07])            
            #age=np.random.choice(age_grouping[int(age_group)])
            length=len(age_grouping[int(age_group)])
            age_hold=random.uniform(float(age_grouping[int(age_group)][0]),float(age_grouping[int(age_group)][length-1]))
            age=round(age_hold,1)
            
        else:
            #just get rid of age group 1 for this
            age_group=int(np.random.choice(len(age_grouping)-1,1,[.03,.06,.31,.25,.21,.14]))
            #age=np.random.choice(age_grouping[int(age_group)+1])
            age_group=int(age_group)+1
            length=len(age_grouping[int(age_group)])
            age_hold=random.uniform(float(age_grouping[int(age_group)][1]),float(age_grouping[int(age_group)][length-1]))
            age=round(age_hold,1)
        if age<=0:
            invalid=True
            
        #get vaccine type
        if vaccine_state=='P':
            check_vac=False
            while check_vac==False:
                vac_type=random.randint(0,len(vaccines)-1)
                vaccine=vaccines[vac_type]
        
                amount=vaccine_type.get(vaccine)
                if amount[0]>1:
                    #Shots like J&J cannot be partial
                    check_vac=True
                else:
                    check_vac=False
        elif vaccine_state=='F':
            vac_type=random.randint(0,len(vaccines)-1)
            vaccine=vaccines[vac_type]
            amount=vaccine_type.get(vaccine)
        else:
            vaccine=''
        
        if vaccine_state!='R':

            #get vdt1
            #day_group=np.random.choice(len(day_grouping),1,[.001,.1,.024,.75,.024,.1,.001])
            day_group=np.random.choice(len(day_grouping),1,[.01,.1,.01,.8,.01,.1,.01])

            day_1_idea=np.random.choice(day_grouping[int(day_group)])
            
            day1=start_date+datetime.timedelta(days=int(day_1_idea))            
            vdt1_hold=day1.strftime("%B, %d, %Y")
            vdt1=vdt1_hold.replace('-', ', ')

            #get vdt2
            if amount[0]>1 and vaccine_state!='P':
                #need 2nd shot
                
                min_date=day1+datetime.timedelta(days=amount[1])
                if min_date<=today:
                    vdt2_hold=min_date.strftime("%B, %d, %Y")
                    vdt2=vdt2_hold.replace('-', ', ')
                else:
                    #date is in fututure
                    invalid=True
            else:
                vdt2=''
        
        if vaccine_state!='R':
            gen_type=np.random.choice(genders,1,[0,.49,.51])
        else:
            gen_type=np.random.choice(genders,1,[.01,.44,.55])
        gender=gen_type[0]
        #print(gender_s)
        
        
        #get pno
        pno_str=str(k)
        Pno=pno_str.zfill(8)
        
        
        #decide if they have an email
        email_yn=random.randint(0,1)
        if email_yn == 1:
            #what is the email
            email_un_len=random.randint(1,20)
            email=''
            for i in range(0,email_un_len):
                email=email+random.choice(letters)
            email=email+'@'
            email=email+domain[random.randint(0,len(domain)-1)]
                        
        else:
            email=''
        
        #is there a note
        note_size=random.randint(0,100)
        notes=''
        for i in range(0,note_size):
            notes=notes+random.choice(letters+' ')
        
        if invalid==False:
            record.append({'Pno':Pno,'Rdt':Rdt,'Age':age,'Gen':gender,'VStatus':vaccine_state,'VType':vaccine,'Vdt1':str(vdt1),'Vdt2':str(vdt2),'Email':email,'Notes':notes})
            k=k+1
            
    #print(record)
    
    fieldnames = ['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
       
        writer.writerows(record)
            
def main():
    import sys
    import re
    arguments=sys.argv
    text_op=''
    for i in str(arguments[1:len(arguments)]):
        if i=="'" or i=="," or i=="[" or i=="]":
            text_op=text_op
        else:
            text_op=text_op+i
    #print('text: ',text_op)
    try:
        m=re.findall('(--no)\s+(\d+)\s+(--fname)\s+(\w+.\w+)',text_op)
        numbers=re.findall('(--no)\s+(\d+)',text_op)
        files=re.findall('(--fname)\s+(\w+.\w+)',text_op)
        
        #print("m: ",m)
        empty_list=[]
        
        if text_op=='':
            #print("empty")
            makeCSV()
        elif m==None or m=='' or m==empty_list:
            #print("m empty")
            if numbers!=None and numbers!=empty_list and numbers!='':
                if len(numbers)==1:
                    in_data=re.search('(--no)\s+(\d+)',text_op)
                    if in_data!=None and in_data!='':
                        text_op=text_op.replace(in_data.group(0), '')
                        if text_op.strip()=='':
                            amount=int(in_data.group(2))
                            if amount>=0:
                                makeCSV(num=amount)
                            else:
                                print("Input number must be a positive integer")
                        else:
                           print("It seems that you are having trouble inputing the data.")
                           print("It seems like you wanted to type: python gen_covis_data.py --no <no_of_records>")
                           print("\t-This will use a default filename covidVaccineData.csv and use the positive integer number you give it")
                           print("If you were trying to input a file, please make sure it was of type txt or csv.")
                           print("If that is the case, please type: python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                    else:
                        print("It seems that you are having trouble inputing the data.")
                        print("It seems like you wanted to type: python gen_covis_data.py --no <no_of_records>")
                        print("\t-This will use a default filename covidVaccineData.csv and use the positive integer number you give it")
                else:
                    #print("Invalid")
                    print("It seems that you are having trouble inputing the data.")
                    print("It seems like you wanted to type: python gen_covis_data.py --no <no_of_records>")
                    print("\t-This will use a default filename covidVaccineData.csv and use the positive integer number you give it")
            elif files!=None and files!=empty_list and files!='':
                if len(files)==1:
                    in_data=re.search('(--fname)\s+((\w+.txt)|(\w+.csv))',text_op)
                    if in_data!=None and in_data!='':
                        text_op=text_op.replace(in_data.group(0), '')
                        if text_op.strip()=='':
                            name=in_data.group(2)
                            makeCSV(filename=name)
                        else:
                            print("It seems that you are having trouble inputing the data.")
                            print("It seems you wanted to type: python gen_covis_data.py --fname <file_name.file_type>")
                            print("\t-This will use a default of 100k records of the csv or txt file name you give it.")
                            print("If you were trying to input a number, please make sure it was a positive integer.")
                            print("If that is the case, please type: python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                            
                    else:
                        print("It seems that you are having trouble inputing the data.")
                        print("It seems you wanted to type: python gen_covis_data.py --fname <file_name.file_type>")
                        print("\t-This will use a default of 100k records of the csv or txt file name you give it.")
                        
                else:                    
                    print("It seems that you are having trouble inputing the data.")
                    print("It seems you wanted to type: python gen_covis_data.py --fname <file_name.file_type>")
                    print("\t-This will use a default of 100k records of the csv or txt file name you give it.")
            else:
                print("It seems that you are having trouble inputing the data.")
                print("When inputing into this script, please type: python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                print("Other alternatives are:")
                print("\tpython gen_covis_data.py")
                print("\t-This will use a default of 100k records of the filename covidVaccineData.csv")
                print("\tpython gen_covis_data.py --no <no_of_records>")
                print("\t-This will use a default filename covidVaccineData.csv and use the positive integer number you give it")
                print("\tpython gen_covis_data.py --fname <file_name.file_type>")
                print("\t-This will use a default of 100k records of the csv or txt file name you give it.")
                print("\tWhen you type:python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                print("\t-You will input the filename of txt or csv type and the number of records you want the file to have.")
        else:
            #print(m)
            if len(numbers)>1:
                #input amount more than once
                print("Invalid")
                print("Cannot have multiple --no <num_records>")
                print("Can only have one.")
            if len(files)>1:
                #input file name more than once
                print("Invalid")
                print("Cannot have multiple files listed, must be --fname <file_name.file_type>")
            
            if len(m)==1:
                #print("m")
                in_data=re.search('(--no)\s+(\d+)\s+(--fname)\s+(\w+.\w+)',text_op)
                text_op=text_op.replace(in_data.group(0),'')
                if text_op.strip()=='':
                    amount=int(in_data.group(2))
                    name=in_data.group(4)
                    
                    f_check=re.search('(\w+.txt)|(\w+.csv)',name)
                    if f_check!=None and f_check!='':
                    
                        #print(amount,name)
                        #print("here")
                        if amount>=0:
                            makeCSV(amount,name)
                        else:
                            print("Number must be a positive integer")
                    else:
                        print("Filename should be of type csv or txt.")
                else:
                    print("There can only be one file and record amount given in this script.")
                    print("When inputing into this script, please type: python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
            else:
                print("It seems that you are having trouble inputing the data.")
                print("When inputing into this script, please type: python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                print("Other alternatives are:")
                print("\tpython gen_covis_data.py")
                print("\t-This will use a default of 100k records of the filename covidVaccineData.csv")
                print("\tpython gen_covis_data.py --no <no_of_records>")
                print("\t-This will use a default filename covidVaccineData.csv and use the positive integer number you give it")
                print("\tpython gen_covis_data.py --fname <file_name.file_type>")
                print("\t-This will use a default of 100k records of the csv or txt file name you give it.")
                print("\tWhen you type:python gen_covis_data.py --no <no_of_records> --fname <file_name.filetype>")
                print("\t-You will input the filename of txt or csv type and the number of records you want the file to have.")
        
    except:
        print("Problem has occured. Please Check that file is not currently open and that you have properly specified the information necessary.")
        print("To specify the arguments, please type: --no <number> --fname <filename>")
        print("Filename can be a txt or a csv file.")
        print("Number must be a positive integer")
        #makeCSV()
        
if __name__=="__main__":
    main()
        