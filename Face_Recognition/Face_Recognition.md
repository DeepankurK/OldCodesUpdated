# Read Me:- Face_Recgnition.py
 
  

## Table of Contents

  
- [Description](#dscription)

  

- [Background](#background) 

 - [Usage](#Usage)

- [Short Comings](#shortcomings)  
- [Contributors](#contributors)

  

- [License](#license)

  

 
 
## Description:

  

Read_me is written to facilitate the understanding of the code.
This code reads images, and a csv file to train itself for
recognising people by looing at their faces(by a camera input).
The CSV file contains names of certain people for which database 
is available along with their code number.
It worked perfectly at the time of final testing.
```sh
with open('Data.csv', 'rt') as f:
	reader = csv.reader(f, delimiter=',')
	#read file seperate strings within a line by ';'
	for row in reader: #for every row in file
		if str(code) == row[1]:
			return row[0]
#return code number from the row number if the match is found.
```
```sh
image = Image.open(image_path)
#goto the image.
``` 
```sh
image_arr= np.array(image, 'uint8')
#create array for an image.    
```
```sh
images.append(image_arr)
labels.append(l)
#add this image to the 'images' matrix, and label to the 'labels' matrix.
```
```sh
recognizer.train(images, np.array(labels))
#train the face detection algorithm with the images provided.
```
```sh
faces=face_cascade.detectMultiScale(gray.copy(),1.3,5)
#Detect all the faces in the frame.
```
```sh
predicted_code,conf=recognizer.predict(gray[y:y+h,x:x+h])
#predict the identity of the person using the face rec algorithm we trained.
```
```sh
predicted_name=find(predicted_code)
#call the function 'find' defined earlier to find the name of the person from
#data loaded from the CSV file and the code predicted by the algorithm.
```
## Usage
Click on the file Face_Recognition.py to get the full code.
Keys:  Q     : Exit.
 Destination of images and csv file have to be specified 
 to the code before running it.  
 
## Short Comings

  

1. Works poorly in low light.

  

2. Can detect faces in frontal orientation only.

  

3. Assigns any random code to the faces for which database is not available.

 

4. Depends on then other code for correct output.(Image_Set_Creation.py)  

## Contributors 

[@Deepankur Kansal]([https://github.com/DeepankurK](https://github.com/DeepankurK)).

[@Paras Mittal](https://github.com/Paras69/)

  

## License

  

[IITK](LICENSE) © HUMANOID TEAM

