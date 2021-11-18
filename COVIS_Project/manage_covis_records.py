# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:37:56 2021

@author: klkel
"""


VType={'Pfizer':[2,21],'Moderna':[2,28],'J&J':[1,0]}
Gen={'U':'Unspecified','M':'Male','F':'Female'}
VStatus={'R':'Registered but not Vaccinated','P':'Partially Vaccinated','F':'Fully Vaccinated'}
record=[]    

def needHelp(location=None):
    """
    This function will tell you how to use this script.

    """
    try:
        if location==None:
            #general help
            print("This is the COVID-19 Vaccination Information System Help Function")
            print("Options include:")
            print("Search for a record")
            print("Add a new Vaccination Record")
            print("Add or change dictionary attriibutes")
            print("Modify a person's data")
            print("Import a file (csv or txt file)")
            print("Attribute options are:")
            print("\t-m which cobines with the options above")
            print("\t-g which contains graph options")
            print("\t-f which sets the filename")
            print("\t-h which is this help location should you need to come directly back")
            print("\t-i which gives the average information")
            attr=input("If you would like to learn more about a certain attribute, please type the attribute:")
            if attr=='-f':
                location='fname'
            elif attr=='-g':
                location='graphs'
            elif attr=='-m':
                location='modes'
            elif attr=='-i':
                location='info'
            elif attr=='-h':
                print("You are already in help")
                print("Help can be reached by typing python manage_covis_records.py -h")
                print("To learn more about this program, please try going to help once again. Goodbye.")
            else:
                print("It seems you were not sure what to type.")
                print("You may want to go through help one more time.")
                print("Help can be reached by typing python manage_covis_records.py -h")
                print("Goodbye.")
                
        if location=='modes':
            #give info about -m
            print("It seems you would like to learn more about the -m attribute")
            print("Options include:")
            print("search")
            print("add")
            print("addA")
            print("change")
            print("import")
            mode_op=input("If you would like to learn more about an option, please type it here: ")
            modes=['add','addA','search','change','import']
            if mode_op in modes:
                location=mode_op
            else:
                print("Goodbye")
            
        if location=='info':
            #give info on -i
            print("It seems you need help to understand the -i attribute")
            print("If you type the command 'python manage_covis_records.py -i' you will get information printed out")
            print("This information will include:\tTotal doses administered")
            print("\tTotal number of people")
            print("\tTotal number of people")
            
            print("\tTotal number of people partially vaccinated")
            print("\tCurrent vaccination rate" )
            print("\tThe average age of fully vaccinated people")
            print("\tPercentage of Female and Male who are fully vaccinated")
            
        if location=='change':
            #info on change
            print("It seems you need help to understand the -m change attribute")
            print("If you type the command 'python manage_covis_records.py -m change' you will be able to change a record")
            print("First you will need to search for a record and then select which record you would like to change")
            print("You can only change 1 modifier (i.e.: Gen,Age,Rdt,Vdt1,Vdt2,VType,VStatus,Email,Notes)")
            print("Pno is not able to be modified")
            print("Vdt1 and Vdt2 are not able to be changed if a date already exists for that record")
            print("The values that the record is changed to must be able to pass validation checks.")
            print("Validation checks include: ")
            print("\tIf VStatus is 'R', VType,Vdt1,and Vdt2 do not have a value inside of them.")
            print("\tIf VStatus is 'P', Vdt2 does not have a value inside of it.")
            print("\tIf VStatus is 'F', Vdt2 must be a valid date after Vdt1 and must match how long it takes for that vaccine to need a second shot.")
            print("\t\tEx) if: VType='Moderna', Vdt1=April, 05, 2021 \n\t\tVdt2 must be May, 03, 2021")
            
        if location=='dates':
            print("It seems you need help to understand inputing dates")
            print("Format is: (Month, day, year)")
            print("ex) June, 05, 2021")
            
        if location=='graphs':
            print("It seems you need help to understand the graph attribute.")
            #print("You can decide which graph attribute you would like to edit by typing ")
            print("There are 3 different graph options to choose from: ")
            print("\t1) -g day")
            print("\t\t-This option will show you two graphs. One on the top and one on the bottom. The top graph will show you vaccinations/day for people partially and fully vaccinated. The bottom Graph will show the total vaccinations/day for the same set of people.")
            print("\t2) -g age")
            print("\t\t-This option will show you one graph that shows total number of people, partially and fully, vaccinated in specific age categories.")
            print("\t3) -g type")
            print("\t\t-This option will show you one graph that shows total number of people, partially and fully, vaccinated in specific age categories.")
            
        if location=='search':
            print("It seems you need help to understand the search mode option")
            print("Criteria options are: Pno,Rdt,Age,Gen,VStatus,VType,Vdt1,Vdt2,Email,Notes")
            print("When entering a search condition the format should be: Criteria:value")
            print("ex) Pno:5")
            print("If multiple criteria please use format: Criteria1:value1,Criteria2:value2")
            print("ex) VStatus:F,VType:Moderna,Vdt1:May, 01, 2021")
            print("Only one value per criteria option accepted")
            print("You cannot do: Pno:5,Pno:6")
    
        if location=='addA':
            print("It seems you do not understand the addA function.")
            print("This function will add or modify dictionary attributes")
            print("There are 2 dictionaries to choose from. Types you can choose from are VTYpe and VStatus.")
            print("For VType type: -m addA VType <vaccine_name> <no_shots> <no_days_btwn_shots>")
            print('Alternatively, for VStatus type: -m addA VStatus <status_keyword> "<status_value>"')
            
        if location=='add':
            print("It seems you did not understand the add function.")
            print("This function allows the user to add a specified amount of records")
            print("If unspecified it will default to 1 additional record")
            print("To call it please type: -m add")
            print("Alternatively, you can also type: -m add <no_records>")
            print("The record must contain valid data.")
            location='valid'
            
        if location=='import':
            print("It seems you did not understand the import function.")
            print("This function will import the specified file")
            print("Format for calling this function is: -m import <filename>.<filetype>")
            print("File type can be a csv or txt file.")
            print("If a record's already exists, it will ask if you wish to modify the record, type 'y' for yes and 'n' for no")
            print("Modified records will append the Notes but nothing else")
            print("Data imported must be valid")
            location='valid'
            
        if location=='valid':
            print("Valid data includes:")
            import datetime
            global VStatus, VType
            dt=datetime.date.today()
            dt_hold=dt.strftime("%B, %d, %Y")
            today=dt_hold.replace('-', ', ')
            print("-Dates between January, 01, 2020 and {}".format(today))
            print("-Dates must be in the format Month, dd, yyyy")
            keys=list(VStatus.keys())
            vac=list(VType.keys())
            print("-VStatus can be: ",keys)
            print("-Vaccine options are: ",vac)
            print("-Vaccine date 2 must be after whatever the time between vaccines are from vaccine date 1")
    except:
        print("\nGoodbye")

def searchMode(location=None):
    """
    This function searches the compiled record options and will show the results if there are matching records.

    Parameters
    ----------
    criteria : str, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    import re
    invalid = False
    criteria_options=['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    #   ask criteria, pno, if none exit w/ "help text about the program"
    #   if mult matches, all printed to screen, if >10 print warning
    #   user can always give mult search criteria
    m=[]
    try:
        criteria=input("Please enter a search criteria: ")
        
        s=re.finditer('(\w+):((\w&\w)|(\w+@\w+.\w+)|(\w+,\s\d\d,\s+\d\d\d\d)|(\d+.\d+)|(\w+)|(\d+))', criteria)
        
        if criteria=='':
            #No input
            needHelp("search")
        #VType:J&J,Email:a@gmail.com,Rdt:May, 10, 2021, Pno:number, Gen:letter,Age:15.2,Age:15
        
        q=re.finditer('(\w+):((\w&\w)|(\w+@\w+.\w+)|(\w+,\s\d\d,\s+\d\d\d\d)|(\d+.\d+)|(\w+)|(\d+))', criteria)
        size=0
        
        for i in q:
            size=size+1
        # print('size',size)
        # print("s: ",s)
        count=0
        for i in s:
            
            # print('in for loop')
            # print(i)
            # print("group: ",i.group(0))
            
            
            if 'Notes'==i.group(1) and count<size-1 and size>1:
                #print("more than one")
                notes_group=re.search('(Notes):(.+)((,\w+:)|(,\s+\w+:))',criteria)
            elif 'Notes'==i.group(1):
                #print('only one')
                notes_group=re.search('(Notes):(.+)',criteria)
            else:
                notes_group=''
                
            if notes_group!=None and notes_group!='':
                #print("Notes exist")
                
                full_note=notes_group.group(1)+':'+notes_group.group(2)
                #print("full notes are ",full_note)
                criteria=criteria.replace(full_note,'')
                #print(notes_group.group(1),notes_group.group(2))
                m.append(notes_group)
                notes_group=''
            else:
                #print('at else')
                m.append(i)
                criteria=criteria.replace(i.group(0),'')
            count=count+1
            #remove the valid text from the criteria
            
        # print('m: ',m)
        # print(criteria)
    except:
        criteria=None
        m=''
        invalid = True
        
    if criteria==None:
        #print("help text about the program")
        invalid=True
        
    all_criteria=[]
    #print('m: ',m)
    try:
        criteria=criteria.replace(',','')
    except:
        criteria=criteria
        
    if criteria.strip()!='':
        #criteria should be blank if all the variables were valid
        invalid=True
    else:
        #the criteria is blank so there was something for every listed item
        invalid=invalid
        
    try:
        for i in range(0,len(m)):            
            #check if they have the correct criterias
            if m[i].group(1) not in criteria_options:
                #incorrect criteria
                invalid=True
                break
            else:
                all_criteria.append(m[i])
    except:
        invalid = True


    search_met=[]
        
    if invalid == False:
        #the criteria and how the user input things should be correct.
        global record
        record_search=record.copy()
        found=0
        valid=False
        for i in record_search:
            #go through the records
            
            next_record=False
            for j in range(0,len(criteria_options)):
                #go through criteria options
                
                if len(all_criteria)==1:
                    #only one criteria given
                    if all_criteria[0].group(1)==criteria_options[j]:
                        #it found the criteria the user searched for
                        
                        if j==0:
                            #Pno
                            if int(all_criteria[0].group(2))==int(i[j].get(criteria_options[j])):
                                #is the pno = to the record?
                                #print(i)
                                valid=True
                            else:
                                valid=False
                                break
                        elif j==2:
                            #age
                            if float(all_criteria[0].group(2))==float(i[j].get(criteria_options[j])):
                                valid=True
                            else:
                                valid=False
                                break
                        elif j==9:
                            #notes
                            
                            if (all_criteria[0].group(2))==(i[j].get(criteria_options[j])):
                                valid=True
                            else:
                                valid=False
                                break
                        else:
                            #something other than pno
                            if all_criteria[0].group(2)==i[j].get(criteria_options[j]):
                                #print(i)
                                valid=True
                            else:
                                valid=False
                else:
                    #More than 1 criteria given
                    for k in range(0,len(all_criteria)):
                        if all_criteria[k].group(1)==criteria_options[j]:
                            #it found the criteria the user searched for
                            if j==0:
                                #pno
                                if int(all_criteria[k].group(2))==int(i[j].get(criteria_options[j])):
                                    #print(i)
                                    valid=True
                                else:
                                    valid=False
                                    break
                            elif j==2:
                                #age
                                if float(all_criteria[0].group(2))==float(i[j].get(criteria_options[j])):
                                    valid=True
                                else:
                                    valid=False
                                    break
                            elif j==9:
                                if (all_criteria[k].group(2))==(i[j].get(criteria_options[j])):
                                    valid=True
                                else:
                                    valid=False
                                    break
                            else:
                                #criteria isn't pno
                                if all_criteria[k].group(2)==i[j].get(criteria_options[j]):
                                    #print(i)
                                    valid=True
                                else:
                                    valid=False
                            if valid==False:
                                next_record=True
                                break
                    if next_record==True:
                        break
                            
            if valid==True:
                found=found+1
                valid=False
                
                #add record to the search output
                search_met.append(i)
                
                
        print("Found {} record(s)".format(found))
        

        if location=='Change':
            return search_met
        
        if found>=10:
            print_all=''
            x=''
            while print_all!='n':
                if x!='e':
                    print_all=input("More than 10 matching the criteria, print (y/n): ")
                if print_all=='y' and x!='e':
                    
                    #print("view 10 entries at a time")
                    
                    startnum=0
                    stopnum=10
                    for i in range(startnum,stopnum):
                            print(search_met[i])
                            print('\n')
                    
                    
                    while x != 'e':
                        
                        x=input("To continue hit Enter. To exit type e: ")
                        try:
                            #print(x)
                            if x=='e':
                                #exit
                                break
                            if x=='':
                                #continue
                                #print("10 new records")
                                startnum=startnum+10
                                
                                stopnum=startnum+10
                                if stopnum>=len(search_met):
                                    stopnum=len(search_met)
                                
                                for i in range(startnum,stopnum):
                                    print(search_met[i])
                                    print('\n')

                        except:
                            continue
                            #do nothing
                elif print_all=='n':
                    print("You have chosen not to see all the matching records.")
                    break
                elif x=='e':
                    #exit
                    break
        else:
            if found==0:
                print("No record matches your input")
            else:
                #print("print all records matching")
                if len(search_met)==1:
                    #only 1 search found
                    print(search_met[0])
                else:
                    #more than 1 search found
                    for i in range(0,len(search_met)):
                        print(search_met[i])
                        print('\n')
    else:
        needHelp('search')
        # print("ERROR: When entering a search condition the format should be: ")
        # print("Criteria options are: Pno,Rdt,Age,Gen,VStatus,VType,Vdt1,Vdt2,Email,Notes")
        # print("ex) Pno:5")
        # print("If multiple criteria please use format: ")
        # print("ex) VStatus:F,VType:Moderna,Vdt1:May, 01, 2021")
        # print("Only one value per criteria option accepted")
        # print("You cannot do: Pno:5,Pno:6")
        
        

def validDate(date_string):
    """
    This function will validate date format and if it is in the correct range.
    """
    import datetime
    
    try:   
        #s_date="June, 20, 2020"

        count=date_string.count(',')
        months=['January','February','March','April','May','June','July','August','September','October','November','December']
        if count==2:
            i=0
            j=0
            date_sorted=[]
            string_sort=''
            while i<len(date_string):
                if date_string[i]==',':
                    j=j+1
                    date_sorted.append(string_sort)
                    string_sort=''
                else:
                    string_sort=string_sort+date_string[i]
                i=i+1
            date_sorted.append(string_sort)
        else:
            return False,''
        #print(date_sorted)
        if date_sorted[0] in months:
            month=date_sorted[0]
            i=0
            j=0
            while i<len(months):
                if month==months[i]:
                    j=i+1
                    #print(months[i])
                    break
                i=i+1
            #print(j)
            day=int(date_sorted[1])
            year=int(date_sorted[2])
            #print(j,day,year)
            date=datetime.date(year,j,day)
            start_date=datetime.date(2020,1,1)
            today=datetime.date.today()
            if date>start_date and date<=today:
                valid=True
                
                return valid,date
            else:
                valid=False
                
                return valid,''
            #print(date)
        else:
            valid=False
    except:
        print("\nFormat is: (Month, day, year)")
        print("ex) June, 20, 2020")
        print("This is required. Please try again")
        valid=False
    
    if valid==True:
        return valid,date
    else:
        return valid,''
    

def validData(pno=None,rdt=None,age=None,gen=None,vstatus=None,vtype=None,vdt1=None,vdt2=None,email=None,notes=None):
    """
    This function will validate the data input.
    """
    import re
    global Gen,VType,VStatus
    
    #print(rdt)
    valid=False
    
    if pno!=None:
        try:
            #check pno
            num=int(pno)
            if num>=0:
                #print("pno pass")
                valid=True
        except:
            return False
    else:
        return False
    
    if rdt!=None:
        try:
            valid,dates=validDate(rdt)
            #print("valid? is ",valid,dates)
        except:
            return False
        
    if age!=None:
        try:
            #check age
            age_test=float(age)
            if age_test>0:
                valid=True
                #print("age: ",valid)
        except:
            return False
    if gen!=None and gen!='':
        try:
            gender_op=Gen.keys()
            # for i in range(0,len(Gen)-1):
            #     gender_op.appned(Gen.key())
            if gen in gender_op:
                valid=True
                #print("gen: ",valid)
            else:
                return False
        except:
            return False
        
    if vstatus!=None and vstatus!='':
        try:
            #check vstatus
            global VStatus
            vstat_op=VStatus.keys()
            if vstatus in vstat_op:
                valid = True
                #print("vstatus: ",valid)
            else:
                return False
        except:
            return False
    else:
        return False
    
    #check vtype
    if vtype!=None and vtype!='' and vstatus!='R':
         try:
            #print(vtype,vstatus)
            #filled if vstatus isn't R
            global VType
            vtype_op=VType.keys()
            if vtype in vtype_op:
                if vstatus=='P':
                    if VType[vtype][0]!=1:
                        valid = True
                    else:
                        return False
                #print("vtype: ",valid)
            else:
                return False
         except:
            return False
    elif (vtype==None or vtype=='') and vstatus=='R':
        #print(vtype,vstatus)
        valid=True
            #empty if vstatus is R
    else:
        return False


    #check vdt`
    if vdt1!=None and vdt1!='' and vstatus!='R':
        try:
            #filled if vstatus isn't R
            valid,dates=validDate(vdt1)
            #print("vdt1: ",valid)
        except:
            return False
    elif (vdt1==None or vdt1!='') and vstatus=='R':
        valid=True
        #empty if vstatus is R
    else:
        return False
    
    # print(vtype)
    # print("vtype: ",VType[vtype][1])
    
    
    #check vdt2
    if vstatus=='F':
        
        import datetime

        #print(VType[vtype][0])
        if (vdt2!=None and vdt2!='') and (VType[vtype][0]!=1):
            #Vdt2 needs to exist
            try:
                #given date
                valid,date2=validDate(vdt2)
                try:
                    #ideal date
                    day2_ideal=dates+datetime.timedelta(VType[vtype][1])
                except:
                    #print("vdt2 is invalid")
                    return False
                
                #more than one shot needed                
                if date2==day2_ideal:
                    valid=True
                else:
                    return False
                    #print("date2: ",valid)
            except:
                return False
        elif (vdt2==None or vdt2=='') and (VType[vtype][0]!=1):
            #date is in future so no shot 2, even though it needs it
            #print(vtype,vstatus)
            try:
                #ideal date
                day2_ideal=dates+datetime.timedelta(VType[vtype][1])
            except:
                #print("vdt2 is invalid")
                return False
            if day2_ideal>=datetime.date.today():
                return False
            else:
                return False
                
        elif (vdt2==None or vdt2=='') and VType[vtype][0]==1:
            #print(vdt2,VType[vtype][0])
            # only one shot is needed
            valid=True
            #print("vdt2 is valid")
        elif (vdt2==None or vdt2=='') and VType[vtype][0]!=1:
            return False
        else:
            #print("false")
            return False
        
    elif (vdt2==None or vdt2=='') and vstatus!='F':
        
        #print("vdt2 is valid")
        #only 1 shot needed so vdt2 shouldn't exist
        valid=True
    else:
        #print("vdt2 is else")
        return False
    
    #check email 
    if email!=None:
        try:
            
            m=re.search('([\w.]+)@([\w]+\.\w+)',email)
            if m!=None and m!='':
                valid=True
            else:
                return False
        except:
            return False
    
    #print("valid: ",valid)
    return valid


def addRecord(number=None):
    """
    This function will add records (default of 1) to the file. It will ask for attributes for everything except pno. That includes, Rdt,Age,Gen,VStatus,Vtype,Vdt1,Vdt2,Email,and notes

    Parameters
    ----------
    num_rec : int, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
   
    #   ask attributes except for pno
    #   validate format, give user warning and remind req format and give opp to enter same attr again
    #   can not specify a val for non req attributes/attributes w/defaults
    #   if incorrect, give another attempt to try
    #   new pno is largest no+1 (size+1)
    #   if vaid,add new record to file
    global record
    valid = False
    rdt_val=False
    age_val=False
    gen_val=False
    vstat_val=False
    vtype_val=False
    vdt1_val=False
    vdt2_val=False
    email_val=False
    
    try:
        num_rec=int(number)
        if num_rec<=0:
            print("The number given to add is not valid. The number must be a positive integer greater than 0.")
            valid=False
        else:
            valid=True
    except:

        
        if number==None or number=='':
            num_rec=1
            valid=True
            print("You did not add a number to this function, default to 1")
        else:
            valid=False
            # print("Please state a number when using this function")
            # print("Proper way to call add is by typing -m add <no>")
            # print("The number must be a positive integer greater than 0.")
            needHelp('add')
            return
            
    if num_rec>0 and valid==True:
        for i in range(0,num_rec):
            while rdt_val == False:
                Recdt=input("Record Date: ")
                rdt_val,date=validDate(Recdt)
                if rdt_val==False:
                    print("WARNING: This is required data")
                    print("\nFormat is: (Month, day, year)")
                    print("ex) June, 20, 2020")
                    print("Please try again")
                    
                
            while age_val == False:
                age_s=input("Input age: ")
                try:
                    age=float(age_s)
                    age_val=True
                except:
                    age_val=False
                    print('\nFormat is an float')
                    print('ex) 15.0 or 15')
                    print('This is required. Please Enter your age again')
        
            
            Gen=input("Input gender: ")
            try:
                if Gen=='U':
                    gen_val=True
                elif Gen=='M':
                    gen_val=True
                elif Gen=='F':
                    gen_val=True
                elif Gen=='' or Gen==None:
                    Gen='U' #take default
                    gen_val=True
                else:
                    gen_val=False
                    print("Gender can be U,M,F")
            except:
                print("Gender can be U,M,F")
                gen_val=False
            
            Vstatus_default='R'
            if gen_val==True:
                while vstat_val==False:
                    Vstatus=input("Input Vaccination Status: ")
                    try:
                        if Vstatus=='R':
                            vstat_val=True
                        elif Vstatus=='P':
                            vstat_val=True
                        elif Vstatus=='F':
                            vstat_val=True
                        else:
                            Vstatus=Vstatus_default
                            print('\nFormat is a letter')
                            print('ex) R, P, or F')
                            print('This is required. Please Enter your age again')
                            vstat_val=False
                    except:
                        print('\nFormat is a letter')
                        print('ex) R, P, or F')
                        print('This is required. Please Enter your Vaccination Status again')
                        vstat_val=False
            else:
                vstat_val=False
                    
            if Vstatus!='R' and gen_val==True:
                Vtype_in=input("Please enter vaccine type: ") 
                try:
                    global VType
                    vtypes=VType.keys()
                    
                    if (Vtype_in in vtypes) or( Vtype_in=='') or (Vtype_in==None):
                        vtype=Vtype_in
                        vtype_val=True
                    else:
                        vtype=''
                        vtype_val=False
                except:
                    vtype=''
                    vtype_val=True
                
                Vdt1=input("First Vaccine Date: ")
                vdt1_val,Vdt1_hold=validDate(Vdt1)
                if Vstatus=='F' and VType[vtype][0]!=1 and vdt1_val==True:
                    import datetime
                    #print(VType[vtype][1])
                    vdt2_ideal=Vdt1_hold+datetime.timedelta(days=VType[vtype][1])
                    while vdt2_val!=True:
                        Vdt2=input("Second Vaccine Date: ")
                        vdt2_val,Vdt2_hold=validDate(Vdt2)
                        
                        if vdt2_ideal==Vdt2_hold:
                            vdt2_val=True
                        else:
                            vdt2_val=False
                            
                        if vdt2_val==False:
                            print("WARNING: This is required data")
                            print("\nFormat is: (Month, day, year)")
                            print("ex) June, 20, 2020")
                            print("Please try again")
                elif Vstatus=='F' and VType[vtype][0]==1 and vdt1_val==True:
                    vdt2_val=True
                    
                    Vdt2=''
                else:
                    vdt2_val=False
                    Vdt2=''
            else:
                vtype_val=True
                vdt1_val=True
                vdt2_val=True
                vtype=''
                Vdt1=''
                Vdt2=''
                
            quick_check=rdt_val and age_val and gen_val and vstat_val and vtype_val and vdt1_val and vdt2_val 
            if quick_check==True:
                email_in=input("Input email: ")
            try:
                import re
                email=re.search(r'([\w.]+)@([\w]+\.\w+)',email_in)
                if email!='' and email!=None:
                    # print(email)
                    # print(email.group(0)) #a.b@gmail.com
                    email_val=True
                else:
                    if email=='' or email==None:
                        email=''
                        email_val=True
                    else:
                        email_val=False
            except:
                email=''
                email_val=False
            
            notes=''
            notes=input("Notes: ")
            
            check_val= rdt_val and age_val and gen_val and vstat_val and vtype_val and vdt1_val and vdt2_val and email_val and valid
            #print(rdt_val, age_val, gen_val, vstat_val, vtype_val, vdt1_val, vdt2_val, email_val, valid)
            
            check_hold=[rdt_val , age_val , gen_val , vstat_val , vtype_val , vdt1_val , vdt2_val , email_val , valid]
            #print(check_hold)
            if(check_val==True):
                # global record
                # pno=len(record)
                #print("Valid")
                
                pno_str=str(len(record))
                P_num=pno_str.zfill(8)
                new_rec=[{'Pno':P_num},{'Rdt':Recdt},{'Age':age},{'Gen':Gen},{'VStatus':Vstatus},{'VType':vtype},{'Vdt1':Vdt1},{'Vdt2':Vdt2},{'Email':email},{'Notes':notes}]
                print("You have made record:\n",new_rec)
                record.append(new_rec)
                
            
                rdt_val=False
                age_val=False
                gen_val=False
                vstat_val=False
                vtype_val=False
                vdt1_val=False
                vdt2_val=False
                email_val=False
            else:
                print("Invalid data provided")
                
    else:
        needHelp('add')
        
def addAkey(attributes):
    """
    

    Parameters
    ----------
    vtype : str, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    import re
    #add vaccine type
    #get name of vaccine
    #no of shots
    #no of days
    # if Vtype==None:
    #     print("retry")
    dictionaries=['VType','VStatus']
    update=[]
    #print(attributes)
    try:
        m=re.findall('(-m\s+addA)\s+(\w+)',str(attributes))
        #print("tried")
        # print(m)
        for i in m:
            #print(i[1])
            if i[1] not in dictionaries:
                valid=False
                break
            else:
                valid=True
                update=i[1]
        if m==None or m=='':
            print("It seems you did not understand how to call the function.")
            print("There are 2 dictionarys to choose from. Types you can choose from are VTYpe and VStatus.")
            print("For VType type: -m addA VType <vaccine_name> <no_shots> <no_days_btwn_shots>")
            print("Alternatively, for VStatus type: -m addA VStatus <status_keyword> <status_value>")
        if valid==True:
            # print("updates: ",update)
            if update==dictionaries[0]:
                # print("update vtype")
                s=re.search('(-m\s+addA\s+VType)\s+(\w+)\s+(\d+)\s+(\d+)',str(attributes))
                # print("s:",s)
                if s!=None and s!='':
                    vname=s.group(2)
                    try:
                        no_s=int(s.group(3)) #Number of shots needed 
                        no_d=int(s.group(4)) #Number of days needed between shots
                        new_vac={}
                        new_vac[vname]=[no_s,no_d]
                        global VType
                        VType[vname]=[no_s,no_d]
                        #print(new_vac)
                    except:
                        #print("Invalid")
                        print("When adding/modifiying the dictionary element VType, you must include the vaccine name, number of shots, and days between the shots in the command.")
                        print("An example of this is: -m addA VType <vaccine_name> <no_shots> <no_days_btwn_shots>")
                else:
                    needHelp("addA")

            elif update==dictionaries[1]:
                #print("update vstatus")
                s=re.search('(-m\s+addA\s+VStatus)\s+(\w+)\s+"(.+)"',str(attributes))
                #print('s: ',s)
                try:
                
                    keyword=s.group(2)
                    value=s.group(3)
                    # new_vstatus={}
                    # new_vstatus[keyword]=[value]
                    global VStatus
                    VStatus[keyword]=value
                    #print(new_vstatus)
                except:
                    print("When adding/modifiying the dictionary element VStatus, you must include the keyword and days between the shots in the command.")
                    print('An example of this is: -m addA VStatus <keyword> "<vlaue>')
            else:
                needHelp('addA')
        #valid=True
        # if valid==True:
        #     print("add to VType")
        #     global VType
        #     VType[vname]=[no_s,no_d]
        #     #print(vname,no_s,no_d)
        else:
            needHelp('addA')
    except:
        needHelp('addA')
        

        
        
def makeGraph(gtype):
    """
    This script will generate graphs based on the filename given. Graphs can be age, vaccine type, or age.


    """
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import re
    #make a graph
    #based on age, day, vaccine type
    
    global record
    global VType
    record_copy=record.copy()
    vtype_copy=VType.copy()
    #Order of criteria: ['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    
    # gtype_options=['day','age','type']

    try:
        if "day" in gtype:
            
            import datetime
            date_set=set() #days
            date_part_l=[]
            date_full_l=[]
            date_tot_part=[]
            date_tot_full=[]
    
            for i in record_copy:
                #get all dates
                if i[6]['Vdt1']!=None and i[6]['Vdt1']!='':
                #person had 1st shot
                    #person had 1st shot
                    date_set.add(i[6]['Vdt1'])
                    #date_part_l.append(i[6]['Vdt1'])
                if i[7]['Vdt2']!=None and i[7]['Vdt2']!='':
                    #person had 2nd shot
                    date_set.add(i[7]['Vdt2'])
                    #date_full_l.append(i[7]['Vdt2'])
            date_list=list(date_set) #list of dates
            #print("got to dates")
            tot_part=0
            tot_full=0
            verify=False
            new_date_list=[]
            
            #get datetime version of the dates so it can b sorted
            for i in range(0,len(date_list)):
                verify, new_date=validDate(date_list[i])
                new_date_list.append(new_date)
    
            new_date_list=sorted(new_date_list) #sorted list of dates
            new_date_list_s=[]
            dt_hold=''
            n_dt=''
            
            #turn back to string
            for i in range(0,len(new_date_list)):
                dt_hold=new_date_list[i].strftime("%B, %d, %Y")
                n_dt=dt_hold.replace('-', ', ') #date format
                new_date_list_s.append(n_dt)
                
                
            #print("changed to date type")
    
    
            date_index=0
            #collect date amounts
            for i in range(0,len(new_date_list_s)):
                date_part=0
                date_full=0
                
            
                for j in record_copy:
                    if j[6]['Vdt1']==new_date_list_s[i]:
                        #person had 1st shot
                        date_part+=1
                        
                        amount=vtype_copy.get(j[5]['VType'])
                        if amount[0]==1:
                            #only needed 1 shot to b full vax
                            date_full+=1
    
                    if j[7]['Vdt2']==new_date_list_s[i]:
                        #person had 2nd shot
                        date_full+=1
    
    
                #get amt of partial/fully vax shots for each day
                tot_part=tot_part+date_part
                tot_full=tot_full+date_full
    
                date_part_l.append(date_part)
                date_tot_part.append(tot_part)
    
                date_full_l.append(date_full)
                date_tot_full.append(tot_full)   
    
    
            plt.subplot(211)
            #plot shots/day for partially and fully vax
            plt.title("Per Day")
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B, %d, %Y'))
            bar=plt.bar(new_date_list,date_part_l,label="Partly Vaccinated",color='paleturquoise',)
            bar=plt.bar(new_date_list,date_full_l,label="Fully Vaccinated",color='salmon')
            # plt.gcf().autofmt_xdate()
    
            plt.legend(loc=2)
            
            plt.subplot(212)
            plt.title("Total")
            
            
            #plot total shots/day for partially and fully vax
            l1=plt.fill_between(new_date_list, date_tot_part,label="Partly Vaccinated",color='cyan',alpha=0.3)
            l1=plt.fill_between(new_date_list, date_tot_full,label="Fully Vaccinated",color='salmon',alpha=0.8)
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B, %d, %Y'))
            
            plt.gcf().autofmt_xdate()
    
            plt.legend(loc=2)
            # plt.tight_layout()
            plt.show()
            
            
            
        elif "age" in gtype:
            #import matplotlib.axes as axes
            
            
            x=["12-17","18-24","25-34","35-44","45-54","55-64","65-74","75-84",">85"] #age groups
            full_group=[0,0,0,0,0,0,0,0,0]
            part_group=[0,0,0,0,0,0,0,0,0]
            age=0
            for i in record_copy:
                try:
                    age=float(i[2]['Age'])
                    #print(age)
                except:
                    print("Data may be invalid")
                    needHelp('graphs')
                    return
                if i[4]['VStatus']=='F':
                    #person is fully vax, figure out age group and then add to it
                    if age>=12 and age<18:
                        full_group[0]=full_group[0]+1
                    if age>=18 and age<25:
                        full_group[1]=full_group[1]+1
                    if age>=25 and age<35:
                        #print("In range 25-34")
                        full_group[2]=full_group[2]+1
                    if age>=35 and age<45:
                        full_group[3]=full_group[3]+1
                    if age>=45 and age<55:
                        full_group[4]=full_group[4]+1
                    if age>=55 and age<65:
                        full_group[5]=full_group[5]+1
                    if age>=65 and age<75:
                        full_group[6]=full_group[6]+1
                    if age>=75 and age<85:
                        full_group[7]=full_group[7]+1
                    if age>=85:
                        full_group[8]=full_group[8]+1
                        
                if i[4]['VStatus']=='P':
                    #print(i[4]['VStatus'])
                    #person is partially vax, figure out age group and then add to it
                    if age>=12 and age<18:
                        part_group[0]=part_group[0]+1
                    if age>=18 and age<25:
                        part_group[1]=part_group[1]+1
                    if age>=25 and age<35:
                        #print("In range 25-34")
                        part_group[2]=part_group[2]+1
                    if age>=35 and age<45:
                        part_group[3]=part_group[3]+1
                    if age>=45 and age<55:
                        part_group[4]=part_group[4]+1
                    if age>=55 and age<65:
                        part_group[5]=part_group[5]+1
                    if age>=65 and age<75:
                        part_group[6]=part_group[6]+1
                    if age>=75 and age<85:
                        part_group[7]=part_group[7]+1
                    if age>=85:
                        part_group[8]=part_group[8]+1
            
            #print("dual bar graph tot num partially and fully vax ppl in age categories")
            #print(part_group)
            x_loc=np.arange(len(x))
            
            width=0.45/2 #width of bars
            
            #plot graphs
            fig,ax=plt.subplots()
            bars1=ax.bar(x_loc-width,part_group,width=.45,color="g",label="P",alpha=.3)
            bars2=ax.bar(x_loc+width,full_group,width=.45,color="g",label="F",alpha=.7)
            
            #figure out where numbers above bar graph go
            width1=[]
            for n in ax.patches:
                width1.append(n.get_width())
                
            #put numbers above bar graph for partially vax
            v_add=0
            for i,v in enumerate(part_group):            
                new_i=i-(width1[i]*15/16)
                #print(new_i)
                if v!=0:
                    v_add=v*(1/18)
                else:
                    v_add=.01
                new_v=v+v_add
                ax.text(new_i,new_v,str(v))
            
            #put numbers above bar graph for fully vax
            v_add=0
            for i,v in enumerate(full_group):            
                new_i=i+(width1[i]*3/16)
                #print(new_i)
                if v!=0:
                    v_add=v*(1/18)
                else:
                    v_add=.01
                new_v=v+v_add
                ax.text(new_i,new_v,str(v))
                
    
            ax.set_xticks(x_loc)
            ax.set_xticklabels(x)
            ax.legend()
            #fig.tight_layout()
            plt.show()
            
    
        elif "type" in gtype:
            #print("pie chart showing num doses/vtype")
            x=['J&J','Moderna','Pfizer']
            y_amt=[0,0,0]
            y_total=0
            for i in record_copy:
                vtype=i[5]['VType']
                if vtype==x[0]:
                    #it is J&J
                    y_amt[0]+=1
                elif vtype==x[1]:
                    #it is Moderna
                    y_amt[1]+=1
                elif vtype==x[2]:
                    #it is Pfizer
                    y_amt[2]+=1
                #otherwise it was a diff type
                if vtype!='' and vtype!=None:
                    y_total+=1
            try:
                if y_total!=0:
                    y=[y_amt[0]/y_total,y_amt[1]/y_total,y_amt[2]/y_total]
                else:
                    #100% empty
                    print("There seems to be no data. Therefore it is 100% Empty")
                    x=['Empty','']
                    y=[1,0]
                fig1,ax1=plt.subplots()
                ax1.pie(y,labels=x,autopct='%1.1f%%',shadow=True,startangle=90)
            except:
                print("It seems there was no data in your file.")
            #ax1.pie(y,labels=x,autopct='%1.1f%%',pctdistance=1.0,startangle=90)
            
        else:
            needHelp('graphs')
    except:
        needHelp('graphs')

def info():
    """
    This function will print the average information of the records.

    Returns
    -------
    None.

    """
    global record
    #Order of criteria: ['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    records_copy=record.copy()
    
    num_fully_vax=0 #num of ppl fully vaccinated
    num_part_vax=0  #num of ppl partially vaccinated
    num_doses1=0    #num of ppl who have had 1st shot
    num_doses2=0    #num of ppl who have had 2nd shot
    ages=0          #total of ages combined
    num_fem=0       #total  of females
    num_male=0      #total  of males
    
    
    for i in records_copy:
        
        
        if i[4]['VStatus']=='F':
            #person was fully vaccinated
            num_fully_vax+=1
            #add age to total ages of ppl fully vax
            ages+=float(i[2]['Age'])
            
        if i[4]['VStatus']=='P':
            #person was partially vaccinated
            num_part_vax+=1
            
        if i[6]['Vdt1']!=None:
            #person had 1st shot
            num_doses1+=1
        if i[7]['Vdt2']!=None:
            #person had 2nd shot
            num_doses2+=1
            
        
        if i[3]['Gen']=='M':
            #person is male
            num_male+=1
        if i[3]['Gen']=='F':
            #person is female
            num_fem+=1
    

    num_doses=num_doses1+num_doses2 #total number of doses
    num_reg=len(records_copy) #num of ppl registered
    
    try:
        vax_rate=(num_fully_vax+num_part_vax)/num_reg #vaccination rate
        vax_rate=round(vax_rate,2)
    except:
        vax_rate=0
        
    try:
        
        avg_age=round(ages/num_fully_vax,1) #average age of fully vax
    except:
        avg_age=0
    try:
        percentage_f=100*(num_fem/(num_fem+num_male)) 
        percentage_m=100*(num_male/(num_fem+num_male))
    
        percentage_f=round(percentage_f,2) #rounded percentage of females
        percentage_m=round(percentage_m,2) #rounded percentage of males
    except:
        percentage_f=0
        percentage_m=0
        
    #print out the values
    print('Number of total doses administered: ',num_doses)
    print('Total number of people fully vaccinated: ',num_fully_vax)
    print('Total number of people partially vaccinated: ',num_part_vax)
    print('Current vaccination rate: ',vax_rate) 
    print('Average age: ',avg_age)
    print('%Female: {} & %Male: {}'.format(percentage_f,percentage_m))
    

def change():
    """
    This function will modify a person's data.
    It will ask for the person search criteria
    print the person's data to the screen
    ask for attribute to be changed
    once you enter the attribute by it's key name, 
    display current value and ask for new value
    new value go through validation
    can't change pno
    can't change vdt1 or vdt2 if they aren't empty
    """
    criteria_options=['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    invalid=0
    print("You have selected Modify Data")    
    try:
        records=searchMode('Change').copy()
        if len(records)>1:
            print("More than one record found. Please specify which record you would like to edit.")
            index=0
            exit_continue=''
            while exit_continue!='e':
                hold=index
                end_index=hold+10
                if end_index>len(records):
                    end_index=len(records)
                for i in range(hold,end_index):
                    print("i: {}, record: {}".format(index,records[index]))
                    index=index+1
                exit_continue=input("Type e to exit once you have found your record or any other key to continue: ")
                
                if exit_continue=='e':
                    break
            chosen=input("Select the i that corresponds to your record or type e to exit: ")
            try:
                print("You have chosen record ",int(chosen))
                print(records[int(chosen)])
                #records=records[chosen]
            except:
                print("You did not choose a valid record number.")
                invalid=1
        elif len(records)==1:
            print("This is the record that you have selected: ")
            print(records)
        elif len(records)<1:
            print("No record Found. Please try again")
            invalid=1
            
        
    except:
        print("No record found to change")
        invalid=1

    if invalid==0:
        modify=input("What would you like to modify? ")
        if modify in  criteria_options:
            for i in range(0,len(criteria_options)):
                #go through what can be modified
                
                if modify==criteria_options[i]:
                    # print(i,records[0])
                    # print(records[0][i])
                    if modify=='Vdt1':
                        #print("check if vdt1 is empty or not")
                        if records[0][6]==None or records[0][6]=='':
                            #empty
                            #print('check if valid')
                            new_value=input("Please input what you would like to change the value to: ")
                            records[0][i][modify]=new_value
                            invalid=0
                        else:
                            #not empty
                            print("Attribute is unable to be changed.")
                        
                            invalid=1
                    elif modify=='Vdt2':
                        #print("check if vdt2 is empty or not")
                        if records[0][7]==None or records[0][7]=='':
                            #emtpy
                            #print('check if valid')
                            new_value=input("Please input what you would like to change the value to: ")
                            records[0][i][modify]=new_value
                            invalid=0
                        else:
                            #not empty
                            print("Attribute is unable to be changed.")
                            invalid=1
                    elif modify=='Pno':
                        print("Attribute is unable to be changed.")
                        invalid=1
                    else:
                        print("You have selected: {}\n\nIt is currently set to {}".format(modify,records[0][i].get(modify)))
                        new_value=input("Please input what you would like to change the value to: ")
                        records[0][i][modify]=new_value
                        break
            if invalid==1:
                invalid=1
                needHelp('change')
                return
        else:
            needHelp('change')
            invalid=True
            return
            #mod_rec.append()
            
        #print(records)
        
        valid=validData(records[0][0][criteria_options[0]],records[0][1][criteria_options[1]],records[0][2][criteria_options[2]],records[0][3][criteria_options[3]],records[0][4][criteria_options[4]],records[0][5][criteria_options[5]],records[0][6][criteria_options[6]],records[0][7][criteria_options[7]],records[0][8][criteria_options[8]],records[0][9][criteria_options[9]])
        
        #print(valid)
    
        if valid==True and invalid==0:
            
            global record
            for i in range(0,len(record)):
                if record[i][0]['Pno']==records[0][0]['Pno']:
                    #hold=i
                    #print(record[i])
                    record[i]=records[0]
                    print(record[i])
        elif valid==False:
            print("The value was invalid.")
            needHelp('change')
            return
            
            

def importFile(text_op:str=None,location:str=None):
    """
    This will allow user to import new csv or text file <FileToImport> in correct format
    can import newrecords or modify existing records
    new records go through checks and validations
    new file will report to the user:
    -Follow allchecks and balances for file check
    -If ppl w/ existing pno in new file, give warning.
    -no overwrite notes strng, concat w/notes in new file
    -print total num of new patient records detected
    -append records to existing file


    Returns
    -------
    None.

    """
    import re
    import csv
    #print(text_op)
    file_csv=''
    file_txt=''
    
    do_print=False
    #print(location)
    if location!='main':
        do_print=True
    
    
    
    #find filename
    file_txt=re.search('(\w+.txt)', text_op)
    file_csv=re.search('(\w+.csv)', text_op)
    
    new_rec=[]
    valid=False
    
    if file_txt!=None:
        #print('.txt')
        filename=file_txt.group(1)
    elif file_csv!=None:
        #print('.csv')
        filename=file_csv.group(1)
    else:
        filename=''
        
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
                    new_rec.append([row['Pno'],row['Rdt'],row['Age'],row['Gen'],row['VStatus'],row['VType'],row['Vdt1'],row['Vdt2'],row['Email'],row['Notes']])
            #print(new_rec)
            #print(data)
        
        if '.csv' in filename:
            #print("It is csv")
            
            with open(filename,'r',newline='') as csvfile:
                #read pointer
                csvfile.seek(0)
                reader = csv.DictReader(csvfile)

                for row in reader:
                    #print(row['Pno'],row['Rdt'],row['Age'],row['Gen'],row['VStatus'],row['VType'],row['Vdt1'],row['Vdt2'],row['Email'],row['Notes'])
                    new_rec.append([row['Pno'],row['Rdt'],row['Age'],row['Gen'],row['VStatus'],row['VType'],row['Vdt1'],row['Vdt2'],row['Email'],row['Notes']])
            #print(new_rec)
            
        #it was able to read file
        valid=True
            
    except:
        print("Invalid file")
        valid=False
    
    categories=['Pno','Rdt','Age','Gen','VStatus','VType','Vdt1','Vdt2','Email','Notes']
    
    if valid==True:
        for i in range(0,len(new_rec)):
            for j in range(0,9):
                if new_rec[i][j]=='':
                    new_rec[i][j]=None
            
            valid=validData(new_rec[i][0],new_rec[i][1],new_rec[i][2],new_rec[i][3],new_rec[i][4],new_rec[i][5],new_rec[i][6],new_rec[i][7],new_rec[i][8],new_rec[i][9])
            #print(new_rec[i])
            
            if valid==False:
                #print(valid)
                print("Record: {} appears to contain invalid data".format(new_rec[i]))
                break
        
    
    record_appended=False
    #print(valid,len(new_rec))
    repeat_found=False
    if valid==True:
        #new inputs had valid data    
        #print("It is valid")
        global record
        orig_len=len(record)
        records_to_append=[]
        record_copy=record.copy()
        if len(record_copy)!=0:
            #print("record ! empty")
            for i in range(0,len(new_rec)):
                for j in range(0,len(record_copy)):
                    #print(new_rec[i][0],record[j][0]['Pno'])
                    if new_rec[i][0] in record_copy[j][0]['Pno']:
                        #there was a new record with the same Pno.
                        repeat_found=True
                        hold=[{categories[0]:new_rec[i][0]},{categories[1]:new_rec[i][1]},{categories[2]:new_rec[i][2]},{categories[3]:new_rec[i][3]},{categories[4]:new_rec[i][4]},{categories[5]:new_rec[i][5]},{categories[6]:new_rec[i][6]},{categories[7]:new_rec[i][7]},{categories[8]:new_rec[i][8]},{categories[9]:new_rec[i][9]}]
                        replace=''
                        while replace not in ['y','n']:
                            replace=input("Record already exists: \n{}\n\n Are you sure you wish to modify it with this record? \n\n{} \n\n(y/n): ".format(record_copy[j],hold))
                            if replace=='y':
                                #they want to change the record and append notes
                                print("You have chosen to modify the record")
                                new_notes=record_copy[j][9]['Notes']+''+new_rec[i][9]
                                record_copy[j]=[{categories[0]:new_rec[i][0]},{categories[1]:new_rec[i][1]},{categories[2]:new_rec[i][2]},{categories[3]:new_rec[i][3]},{categories[4]:new_rec[i][4]},{categories[5]:new_rec[i][5]},{categories[6]:new_rec[i][6]},{categories[7]:new_rec[i][7]},{categories[8]:new_rec[i][8]},{categories[9]:new_notes}]
                            elif replace=='n':
                                #they ignore the new record
                                print("you have chosen to not replace the record")
                            else:
                                #wrong option, choose y or n
                                print("invalid option")
                                needHelp("import")
                                return
                if repeat_found==False:  
                    #no repeat found, just append
                    records_to_append.append([{categories[0]:new_rec[i][0]},{categories[1]:new_rec[i][1]},{categories[2]:new_rec[i][2]},{categories[3]:new_rec[i][3]},{categories[4]:new_rec[i][4]},{categories[5]:new_rec[i][5]},{categories[6]:new_rec[i][6]},{categories[7]:new_rec[i][7]},{categories[8]:new_rec[i][8]},{categories[9]:new_rec[i][9]}])
                else:
                    repeat_found=False
                    
            for i in range(0,len(records_to_append)):
                record_copy.append(records_to_append[i])
        else:
            #emtpy
            record_appended=True
            #print("record empty")
            for i in range(0,len(new_rec)):

                record.append([{categories[0]:new_rec[i][0]},{categories[1]:new_rec[i][1]},{categories[2]:new_rec[i][2]},{categories[3]:new_rec[i][3]},{categories[4]:new_rec[i][4]},{categories[5]:new_rec[i][5]},{categories[6]:new_rec[i][6]},{categories[7]:new_rec[i][7]},{categories[8]:new_rec[i][8]},{categories[9]:new_rec[i][9]}])
            #print(location)
            if do_print==True:
                new_len=len(record)
                new_rec_num=new_len-orig_len
                print("New patient records detected: ",new_rec_num)
                    
    new_rec_num=0            
    if valid==True and record_appended==False:
        #record wasn't empty
        #new inputs had valid data        

        
        record=record_copy.copy()
    
    
        new_len=len(record_copy)
        new_rec_num=new_len-orig_len
        print("New patient records detected: ",new_rec_num)
    if valid==False:
        needHelp("import")
    
def acceptedArg(arguments=None):
    """
    This function will do a basic check if all the options and modes are valid. There can only be options from the options list (i,h,m,f,g). There are only 5 modes for -m, (search,add,addA,change,import). There are only 3 modes for -g, (day,age,type). And file names are either txt or csv. If it does not fall within the parameters it is not an accepted argument.
    """
    import re
    
    modes=['search','add','addA','change','import']
    options=['-i','-h','-m','-f','-g']
    graph_op=['day','age','type']
    try:
        #print(arguments)
        text_op=str(arguments)
        
        hold=re.split('-\w',text_op)
        s=re.findall('(-\w)',text_op)
        methods=[]
        invalid=False
        listing=[]
        graphs=[]
        filename=''
        for j in s:
            if j not in options:
                invalid=True
                break
            else:
                
                if j=='-m':
                    m=re.search('(?P<type>-m)\s+(?P<name>\w+)',text_op)
                    if m.group('name') not in modes:
                        invalid=True
                        #print('m')
                        break
                    else:
                        methods.append(j)
                        listing.append(m.group(2))
                elif j=='-f':
                    file_txt=re.search('(-f)\s+(\w+.txt)', text_op)
                    file_csv=re.search('(-f)\s+(\w+.csv)', text_op)
                    
                    if file_csv !=None:
                        #print('csv')
                        methods.append(j)
                        filename=file_csv.group(2)
                        #print(file_csv.group(0))
                        text_op=text_op.replace(file_csv.group(0), '')
                        #print(text_op)
                    elif file_txt!=None:
                        #print('txt')
                        methods.append(j)
                        filename=file_txt.group(2)
                        text_op=text_op.replace(file_txt.group(0), '')
                    else:
                        #print('file inval')
                        invalid=True
                        break
                    
                elif j=='-g':
                    q=re.search('(?P<type>-g)\s+(?P<name>\w+)',text_op)
                    if q!=None and q!='':
                        #print(q)
                        if q.group('name') not in graph_op:
                            #q has something in it
                            invalid = True
                        else:
                            methods.append(j)
                            text_op=text_op.replace(q.group(0),'')
                    else:
                        #it was only -g
                        invalid=True
                else:
                    #-i or -h so nothing should follow
                    check=re.search(j+'\s+(\w+)',text_op)
                    if check!=None:
                        #word followed
                        invalid=True
                        break
                    else:
                        methods.append(j)
                        #print("i or h")
                        text_op=text_op.replace(j,'')
                        
        #print("before -m: ",text_op)
    
        if '-m' in methods:
            for i in listing:
                if i == modes[0]: #search
                    check=re.findall('(-m\s+search)',text_op)
                    if len(check)==1:
                        #print("search")
                        replace=re.search('(-m\s+search)',text_op)
                        text_op=text_op.replace(replace.group(0), '')
                    else:
                        #they typed it more than once
                        invalid=True
                        needHelp('search')
                    
                    #print("Check Search")
                elif i==modes[1]: #add
                    #print("add")                                           
                    check=re.findall('(-m\s+add\s+\d+)',text_op)
                    if len(check)==1:
                        replacement=re.search('(-m\s+add\s+\d+)',text_op)
                        # print("Replacement")
                        # print(replacement.group(1))
                        # print("End")
                        text_op=text_op.replace(replacement.group(0), '')
                    else:
                        #they typed it more than once
                        check=re.findall('(-m\s+add)',text_op)
                        if len(check)==1:
                            replacement=re.search('(-m\s+add)',text_op)
                            text_op=text_op.replace(replacement.group(0), '')
                        else:
                            invalid=True
                            needHelp('add')
                        
                elif i==modes[2]: #addA
                    # print("addA")
                    check=re.findall('(-m\s+addA)',text_op)
                    # print(len(check))
                    # print("checked")
                    # print("Check: ",check)
                    if len(check)==1:
                        #print("in addA")
                        replacement=re.search('(-m\s+addA)\s+((\w+\s+\w+\s+\d+\s+\d+)|((\w+\s+\w+)\s+"(.+)"))',text_op)
                        #print(text_op)
                        #replacement=re.search('(-m\s+addA)\s+((VStatus\s+\w+)\s+"(.+)")',text_op)
                        #print(replacement)
                        try:
                            #print(replacement.group(0))
                            text_op=text_op.replace(replacement.group(0), '')
                        except:
                            invalid=True
                    else:
                        #they typed it more than once
                        invalid=True
                        
                elif i==modes[3]: #change
                    #print("change")
                    check=re.findall('(-m\s+change)',text_op)
                    #print(check)
                    if len(check)==1:
                        replacement=re.search('(-m\s+change)',text_op)
                        #print("replacement: ",replacement)
                        text_op=text_op.replace(replacement.group(1), '')
                elif i==modes[4]: #import
                    #check file
                    #print("Import")
                    file_txt=re.findall('(-m\s+import)\s+(\w+.txt)', text_op)
                    file_csv=re.findall('(-m\s+import)\s+(\w+.csv)', text_op)
                    #print("txt,csv",file_txt,file_csv)
                    if len(file_csv)==1 and len(file_txt)==0:
                        # 'csv' file
                        #print("at csv")
                        filename=re.search('(-m\s+import)\s+(\w+.csv)', text_op)
                        
                        #print('filename',filename.group(0))
                        text_op=text_op.replace(filename.group(0), '')
                    elif len(file_txt)==1 and len(file_csv)==0:
                        #'txt' file         
                        #print("at txt")
                        filename=re.search('(-m\s+import)\s+(\w+.txt)', text_op)
                        #print('filename',filename.group(0))
                        text_op=text_op.replace(filename.group(0), '')
                        
                    else:
                        invalid=True
                        break
                else:
                    invalid=True
                    
                
        #print("text: ",text_op)
        if (text_op.strip())!='':
            #print("Not empty")
            invalid = True
            
        if invalid==True:
            methods.clear()
            listing.clear()
            #print("Invalid")
            return False
        else:   
        
            return True
    except:
        #print("Problem")
        return False
    
        
def main():
    """
    

    Returns
    -------
    None.

    """
    import sys
    import re
    global record
    
    
    conditions=[]
    conditions=sys.argv    
    #print("In main")
    #print(conditions)
    

    conditions=[]
    conditions=sys.argv  
    #print('Conditions: ',conditions)
    current_conditions=conditions[1:len(conditions)]
    #print(current_conditions)
    text_op=''
    for i in range(0,len(current_conditions)):
        if current_conditions[i]=='addA':
            try:
                if current_conditions[i+1]=='VStatus':
                    current_conditions[i+3]='"'+current_conditions[i+3]+'"'
                    #print(current_conditions[i+3])
                break
            except:
                continue
            
    for i in str(current_conditions):
        if i=="'" or i=="," or i=="[" or i=="]":
            text_op=text_op
        else:
            text_op=text_op+i
    #print(text_op)
    # print("text op: ",text_op)    
    # print("text is ",text)
    modes=['search','add','addA','change','import']
    options=['-i','-h','-m','-f','-g']
    graph_op=['day','age','type']
    
    hold=re.split('-\w',text_op)
    s=re.findall('(-\w)',text_op)
    methods=[]
    invalid=False
    listing=[]
    graphs=[]
    filename=''
    
    #print("Before accepted Arg")
    is_valid=acceptedArg(text_op)
    #print("After accepted Arg")
    #print(is_valid)
    

            
    
    #print("methods: {} listings: {}".format(methods,listing))
    #print(filename)
    

    if is_valid==False or text_op=='':
        print("It appears you need help.")
        needHelp()
    else:
        for j in s:
            if j not in options:
                invalid=True
                break
            else:
                
                if j=='-m':
                    m=re.search('(?P<type>-m)\s+(?P<name>\w+)',text_op)
                    if m.group('name') not in modes:
                        invalid=True
                        #print('m')
                        break
                    else:
                        methods.append(j)
                        listing.append(m.group(2))
                elif j=='-f':
                    file_txt=re.search('(-f)\s+(\w+.txt)', text_op)
                    file_csv=re.search('(-f)\s+(\w+.csv)', text_op)
                    
                    if file_csv !=None:
                        #print('csv')
                        methods.append(j)
                        filename=file_csv.group(2)
                    elif file_txt!=None:
                        #print('txt')
                        methods.append(j)
                        filename=file_txt.group(2)
                    else:
                        invalid=True
                        break
                elif j=='-g':
                    q=re.search('(?P<type>-g)\s+(?P<name>\w+)',text_op)
                    if q.group('name') not in graph_op:
                        invalid = True
                        #print('g')
                    else:
                        methods.append(j)
                        graphs.append(q.group('name'))
                else:
                    check=re.search(j+'\s+(?P<name>\w+)',text_op)
                    if check!=None:
                        invalid=True
                        break
                    else:
                        methods.append(j)
                        invalid=False
    
        if invalid==True:
            methods.clear()
            listing.clear()
            #print("Invalid")
        
        
        if not('-f' in methods):
            filename='covidVaccineData.csv'
            #print("here")
            importFile(filename,location="main")
            global record
            
        else:
            importFile(filename,location="main")
    
        if '-m' in methods:
            for i in listing:
                if i==modes[0]: #search
                    searchMode()
                elif i==modes[1]:#add
                    number=re.search('(-m\s+add)\s+(\d+)', text_op)
                    if number!=None and number!='':
                        addRecord(number.group(2))
                    else:
                        addRecord()
                elif i==modes[2]:#addA
                    addAkey(text_op)
                elif i==modes[3]:#change
                    change()
                elif i==modes[4]:#import
                    file_txt=re.search('(-m\s+import)\s+(\w+.txt)', text_op)
                    file_csv=re.search('(-m\s+import)\s+(\w+.csv)', text_op)
                    if file_txt!=None and file_txt!='':
                        #print()
                        importFile(file_txt.group(2),location='')
                    if file_csv!=None and file_csv!='':
                        #print()
                        importFile(file_csv.group(2),location='')
                    
                else:
                    needHelp('-m')
        if '-i' in methods:
            info()
        if '-h' in methods:
            needHelp()
        if '-g' in methods:
            makeGraph(graphs)
            
        if methods=='':
            print("It appears you need help.")
            needHelp()    
        
if __name__=="__main__":
    main()
    