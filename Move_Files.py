import os
import shutil


from_dir = "C:/Users/arnav/Downloads"

to_dir = "d:/projects/Project_102"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for x in list_of_files:
    name, extention = os.path.splitext(x)
    print(name)
    print(extention)

    if extention == "":
        continue
    if extention in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + x
        path2 = to_dir + '/' + "Download_Files"
        path3 = to_dir + '/' + "Download_Files" + x

        print(path2)

        if os.path.exists(path2):
            print("Moving " + x + "...")

            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving", x, "...")

            shutil.move(path1, path3)
     
