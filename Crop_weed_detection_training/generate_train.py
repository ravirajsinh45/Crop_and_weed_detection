import os

image_files = []
os.chdir(os.path.join("data", "agri_data/data"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpeg"):
        image_files.append("data/agri_data/data/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")