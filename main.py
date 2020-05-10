import datetime
import os

print ('P: ',os.getcwd())
thedir = os.getcwd()+"\\test"

Folder_List =  ([ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]) # Creates a list with the names of the folders
''' Out_List example
    Out_List[i] = ['The folder original name',  'The datetime object of the folder',   'The converted filename object ']
    Out_List[i] = ['10-4-2020',                  datetime.datetime(2020, 4, 10, 0, 0)]

'''

Out_List=[]
for i in range(len(Folder_List)):
    try:
        Out_List.append([Folder_List[i]]+ [datetime.datetime.strptime(Folder_List[i], '%d-%m-%Y')]) # Convert the date name to a datetime object for easier sorting later]
    except:
        print("The folder name '"+Folder_List[i]+"'"+' is not valid and will be skiped.')
del Folder_List  

Out_List.sort(key=lambda tup: tup[1])


for i in range(len(Out_List)):
    Out_List[i] = Out_List[i] + [str(i+1)+'. '+Out_List[i][0]]
    
for i in range(len(Out_List)):
    os.rename(thedir+'\\'+Out_List[i][0], thedir+'\\'+Out_List[i][2])