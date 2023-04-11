import os
path = "../faces"
#path = "C:/Users/abril/Desktop/Repos/Crux/tinder-expo/assets/faces"
dir_list = os.listdir(path)
print(dir_list)

i = len(dir_list)
print(i)
while(0<i):  #"../images/01.jpg";
    print("import IMG"+str(i)+" from \"../faces/"+str(dir_list[i-1]) + '\"')
    i -= 1

i=1
while(i<89): 
    print( "{\n" + "\tid:" + str(i) + ",\n" +"\timage: IMG"+str(i)+","+ "\n\tname: \"\",\n\tisOnline: true,\n\tmatch: \'\',\n\tdescription: \'\',\n\tmessage: \'\'," + "\n},") 
    i+=1
