import os

os.system("bash takelist.sh")

first_file = open("first","r")
second_file = open("second","r")
third_file = open("third","r")

first_file_list = []
second_file_list = []
third_file_list = []

for i in first_file:
    first_file_list.append(i)

for i in second_file:
    second_file_list.append(i)

for i in third_file:
    third_file_list.append(i)

first_file.close()
second_file.close()
third_file.close()

for i in first_file_list:
    for j in second_file_list:
        if i == j:
            for k in third_file_list:
                if i == k:
                    i = i.split("\t")
                    i = i[1].split("\n")
                    print(i[0])
                    os.system(f"rm -rf {selected_dir}/{selected_dir}/{i[0]}")
                    os.system(f"rm -rf {selected_dir}/{selected_dir}/{selected_dir}/{i[0]}")
    pass