# Read Me:- Image_Set_Creation.py
 ## Table of Contents  
 - [Desciption](#discription)
- [Background](#background)   
- [Usage](#usage)
- [Short Comings](#short-comings)  
- [Maintainers](#maintainers)  
- [Contributors](#contributors)  
- [License](#license)  
 


## Description:
Read_me is written to facilitate the understanding of the code. 
This code captures images from a camera, detects faces in it,
 and on recieving command, saves a cropped image of the face in 
 jpg format, having a name that is a code that we assign, and a 
 random number seperated by a '.'  .
        
It also creates a CSV file that stores the name and code of the
person whose data set is being collected.
These name and code are taken from the input.
```sh
path='/home/deepank/Downloads/Face_Recognition/Image_Set'
#set path for destination of the images clicked.
```
```sh
faces=faceCascade.detectMultiScale(gray.copy(),1.3,5)
#find all the faces in the frame.
```
```sh
for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#draw rectangles on each face detected.
```
```sh
gray=gray[y:y+h,x:x+w]
resized=cv2.resize(gray,(300,300),interpolation=cv2.INTER_AREA)
#crop the region containing the face and resize it.
# it is resized so that every image captured has he same dimentions.
```
```sh
cv2.imwrite(os.path.join(path , str(code)+'.'+str(int(random.random()*1000000)))+'.jpg', resized)
# save the cropped image with the name format explained in the beginning.Example 1.29875.jpg
```
```sh
#create a row matrix to store name and code.
row=[name,code]
        
#open the csv file and add this row.
 with open('Data.csv','a') as f:
 write=csv.writer(f)
 write.writerow(row)
```
```sh
```
## Background  
Image_Set_Creation.py is created under a new branch of humanoid technology i.e. Social Skills.
It is a first step towards the dream of Humanoid team to develop a fully functional self indigenous humanoid.
It is written by Deepankur Kansal and Paras Mittal.
  
## Usage  
Click on the file Image_Set_Creation.py to get the full code.
Keys:
      SPACE  :  Capture Image.
    Q     : Exit.
 Destination of images and csv file have to be specified 
 to the code before running it.  
 
## Short Comings
1. It will require proper lighting to recognize the image.
2. You will have to set the code yourself.
3. It will only recognize the face in a different position.

## Contributors  
 
[@Deepankur Kansal](https://github.com/DeepankurK)
[@Paras Mittal](https://github.com/Paras69)    
## License  
[IITK](LICENSE) © HUMANOID CLUB

