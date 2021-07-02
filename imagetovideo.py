import os 
import cv2 
from PIL import Image
from tkinter import filedialog
def imgtovid():
    print("HELLO")
    print(os.getcwd())
    dir_name = filedialog.askdirectory()
    os. chdir(dir_name)
    path=(dir_name)
     
    #os.chdir("C:\\Python\\imagesfolder") 
    #path = "C:\\Python\\imagesfolder"
    
    mean_height = 0
    mean_width = 0
    
    num_of_images = len(os.listdir('.')) 
    
    
    for file in os.listdir('.'): 
    	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
    		im = Image.open(os.path.join(path, file)) 
    		width, height = im.size 
    		mean_width += width 
    		mean_height += height 
    
    mean_width = int(mean_width / num_of_images) 
    mean_height = int(mean_height / num_of_images) 
    
    
    for file in os.listdir('.'): 
    	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
    		
    		im = Image.open(os.path.join(path, file)) 
    
    		width, height = im.size 
    		print(width, height) 
    
    		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS) 
    		imResize.save( file, 'JPEG', quality = 100) # setting quality 
    		print(im.filename.split('\\')[-1], " is resized") 
    
    
    def generate_video(): 
    	image_folder = '.' 
    	video_name = 'imagestovideo.avi'
    	os.chdir(dir_name) 
    	
    	images = [img for img in os.listdir(image_folder) 
    			 if img.endswith("_matte.jpg")] #or
    			# 	img.endswith(".jpeg") or
    			# 	img.endswith("png")] 
    	images.sort()
    	print(images) 
    
    	frame = cv2.imread(os.path.join(image_folder, images[0])) 
    	height, width = mean_height,mean_width
    
    	video = cv2.VideoWriter(video_name, 0, 24, (width, height)) 
    	for image in images: 
    		video.write(cv2.imread(os.path.join(image_folder, image))) 
    	
    	cv2.destroyAllWindows() 
    	video.release() 
        #print("END OF VIDEO GENERATION")
    generate_video() 
    