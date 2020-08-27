# Canvas

Canvas is a Cinema 4d Python script that allows you to import an image from a file location and turns it into a 3D plane.
Supports images with alpha, video and image sequences

## Canvas-image

Canvas-imag allows you to import image file into Cinema 4D. When the script is run, a file dialog will pop up. choose the image file. Finally give the material/plane an name. If the image has an alpha channel, Canvas will add it to the material. 

## Canvas-video

Canvas-video allows you to import video files into Cinema 4D. When the script is run, a file dialog will pop up. choose the video file. Finally give the material/plane an name. NOTE only formats Maxon Cinema 4D supports will work.

## Canvas-sequence

Canvas-sequence allows you to import image sequences into Cinema 4D. When the script is run, a file dialog will pop up. choose the first frame from your animation. Finally, input your framerate and give the material/plane an name. 


## Progress
[x] alpha iamges supported <br />
[x] support video files <br />
[x] support image sequences <br />


## Installation
to install, simply add the .py file to your scripts folder.

with C4D open, Script > User Scripts > Script Folder...

OR

Windows: C:\Users\ "" YOUR USERNAME ""  \AppData\Roaming\MAXON\ "" YOUR VERSION OF C4D "" \library\scripts
Mac: /Applications/MAXON/ "" YOUR VERSION OF C4D ""  /library/scripts

## Usage

Script > User Scripts > Canvas

A file dialog will pop up allowing you to choose an image. you then will be allowed to rename both the material and the plane to something 
easy to understand. if you click 'cancel' or the 'x' close icon, the material and plane wil be renamed after the image file.

## C4D Version 

Currently tested on R19-R22. If used on earlier/later versions please let me know so i can update this.






