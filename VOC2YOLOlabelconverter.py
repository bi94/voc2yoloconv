import os
import shutil
from xml.etree import ElementTree
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if __name__ == '__main__':
    source = askdirectory(initialdir="./", title='Please select root directory')
    dest = askdirectory(initialdir="./", title='Please select destination directory')
    classTxt = askopenfilename(initialdir="./", title='Please select txt file for classes')
    classList = []
    with open(classTxt) as f:
        classList = [line.rstrip() for line in f]
    for subdir, dirs, files in os.walk(source):
        for file in files:
            # root of xml file
            root = ElementTree.parse(source+'/'+file).getroot()
            # find tags in xml file
            sizeTag = root.find('size') 

            # read tags values in xml tags
            for element in sizeTag.getchildren():
                #print(element.tag, element.text)
                if element.tag == 'width':
                    width = int(element.text)
                    #print('width ' + str(width))
                if element.tag == 'height':
                    height = int(element.text)
                    #print('height ' + str(height))

            for objTag in root.findall("object"):
                classTag = objTag.find('name')
                if(classTag.text in classList):
                    print(classList.index(classTag.text))
                    classNum = classList.index(classTag.text)
                else:
                    print('Bounding box not translated, class name not in class list.')
                    classNum = ''
                    continue
                # ElementTree.dump(objTag)
                for element in objTag.getchildren():
                    #print(element.tag, element.text)
                    if element.tag == 'bndbox':
                        for bndboxAtt in element.getchildren():
                            #print(bndboxAtt.tag, bndboxAtt.text)
                            if bndboxAtt.tag == 'xmin':
                                xmin = int(bndboxAtt.text)
                                #print('xmin ' + str(xmin))
                            elif bndboxAtt.tag == 'ymin':
                                ymin = int(bndboxAtt.text)
                                #print('ymin ' + str(ymin))
                            elif bndboxAtt.tag == 'xmax':
                                xmax = int(bndboxAtt.text)
                                #print('xmax ' + str(xmax))
                            elif bndboxAtt.tag == 'ymax':
                                ymax = int(bndboxAtt.text)
                                #print('ymax ' + str(ymax))                    
                        v1 = ((xmax+xmin)/2)/width
                        v2 = ((ymax+ymin)/2)/height
                        v3 = (xmax-xmin)/width
                        v4 = (ymax-ymin)/height
                        print('Saving to '+dest+'/'+os.path.splitext(file)[0]+'.txt')

                        YOLOTxt = open(dest+'/'+os.path.splitext(file)[0]+'.txt', "a+")
                        YOLOTxt.write(str(classNum) + " " + "{:.6f}".format(v1) + " " + "{:.6f}".format(v2) + " " + "{:.6f}".format(v3) + " " + "{:.6f}".format(v4) + "\n")
        YOLOTxt.close()          