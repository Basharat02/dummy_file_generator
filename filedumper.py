#Python script to generate files of our desired size. You can change the value of bytes you want to specify in this script as well.

#first import python os in order to deal with the os related tasks.
import os


#os.path.expanduser('~') will simply diplay the path of user's home directory in which the python script is being saved and from where it will run itself.You can 
#save the python scripit wherever you want to dump generated files.

location = os.path.expanduser('~')

#os.path.join will join the paths of the home directory with the location where you want to dump the files.In this case it is desktop
location2 = os.path.join(location,"\\Desktop")



# You can add any string you want to add in the text files we are going to be generating.
#This will print the string 100 times on the newly creaetd notepad file.
string = ""
for i in range(100):
    string = string + "Let us celebrate the life and have a tea\n\n"



#Specify the number of files you want to create in for filecount in range(10):, In my case it is 10
filecount = 0
for filecount in range(10):
    file = open('texter{}.txt'.format(filecount),'w')
    file.write(string)
   
    file.close()
    filecount =+ 1

#This part will be writing binary in those newly created 10 files. file.seek() will specify the size of the files you want.In my case it is almost
# 10 GB.
for filecount in range(10):
    file = open('texter{}.txt'.format(filecount),'wb')
    file.seek(1073741824-1)
    file.write(b"\0")
    
   
    file.close()



print(os.walk("."))






