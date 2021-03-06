# voc2yoloconv
An easy-to-use annotation converter in Python, to convert hundreds of annotation files from XML VOC format to YOLO format in few seconds.  
## Libraries which were used
Firstly, ensure all the libraries are installed in your Python environment.  
```
import os
import shutil
from xml.etree import ElementTree
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
```
## Input data format
XML file example:
```
<annotation>
	<folder>n04070727</folder>
	<filename>n04070727_7</filename>
	<source>
		<database>ImageNet database</database>
	</source>
	<size>
		<width>500</width>
		<height>400</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>Television</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>74</xmin>
			<ymin>0</ymin>
			<xmax>490</xmax>
			<ymax>398</ymax>
		</bndbox>
	</object>
</annotation>
```
## Output example in YOLO format
```
4 0.564000 0.497500 0.832000 0.995000
```
## Data organization
1. Put all .xml files in a directory: this will be the "source" directory, from which the code will take the data to convert (*1.PNG*). 
![alt text](https://github.com/bi94/voc2yoloconv/blob/main/1.png)
2. Create a new directory, in which .txt files will be put after conversion (*2.PNG*). 
![alt text](https://github.com/bi94/voc2yoloconv/blob/main/2.png)
3. Write a text file in which the names of all classes (**one for each line**) will be contained (*3.PNG*).  
![alt text](https://github.com/bi94/voc2yoloconv/blob/main/3.png)
## How to run in cmd
Run with command:
```
python VOC2YOLOlabelconverter.py
```
