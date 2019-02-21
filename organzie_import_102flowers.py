# organize imports
import os
import glob
import datetime
import scipy.io as scio

# print start time
print ("[INFO] program started on - " + str(datetime.datetime.now))

# get the input and output path
input_path  = r"D:\Program\TensorFlow\programs\flower_classify\102flowers\jpg"
output_path = r"D:\Program\TensorFlow\programs\flower_classify\dataset\102flowers\train"

mat_path = r"D:\Program\TensorFlow\programs\flower_classify\102flowers\imagelabels"

# get the class label limit
class_limit = 102

# take all the images from the dataset
image_paths = glob.glob(input_path + "\\*.jpg")

mat = scio.loadmat(mat_path)
labels_array = mat['labels'][0]

# variables to keep track
label = 0
i = 0

# flower102 class names
class_names = []
for i in range(1, class_limit+1):
	class_names.append(str(i))

# change the current working directory
os.chdir(output_path)

# loop over the class labels
for x in range(1, class_limit+1):
	# create a folder for that class
	os.system("mkdir " + class_names[label])
	# get the current path
	cur_path = output_path + "\\" + class_names[label] + "\\"
	# loop over the images in the dataset
	i = 0
	for image_path in image_paths:
		if labels_array[i] == int(class_names[label]):
			original_path = image_path
			image_path = image_path.split("\\")
			image_path = image_path[len(image_path)-1]
			os.system("copy " + original_path + " " + cur_path + image_path)
		i += 1
	label += 1

# print end time
print ("[INFO] program ended on - " + str(datetime.datetime.now))