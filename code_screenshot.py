import time
import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pyautogui

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def take_screenshot():
    resolution = (1920,1080)  # screenshot resolution take it same as of your screen (see in settings)
    screenshot=pyautogui.screenshot(region=(0,0,resolution[0], resolution[1])) 
    return screenshot

"""here region decides what region is being screenshotted and 
(0,0,resolution[0], resolution[1])
    ^ ^       ^              ^       
    | |       |              |
    | |       |              |
left|     width          height
    top
here resolution[0] is set to 1920 and resolution[1] is set to 1080"""

def save_screenshot(image,folder, filename):
    image.save(os.path.join(folder,filename))


def convert_to_pdf(image_filenames,pdf_filename,folder_name,image_resolution=(1920,1080),scaling_factor=3.52): #8.52 = s_f
    c=canvas.Canvas(os.path.join(folder_name,pdf_filename),pagesize=letter)
    
    for img_filename in image_filenames:
        #open the image to get its size in pixels
        img=Image.open(os.path.join(folder_name,img_filename))
        img_width,img_height = img.size

        #calculate the size to fit the image on the page at the desired resolution
        img_width_points = (img_width / image_resolution[0])*72* float(scaling_factor)
        img_height_points = (img_height / image_resolution[1])*50*float(scaling_factor)

        #calculate the center position on the page
        x_center = (letter[0] - img_width_points) / 2
        y_center = (letter[1] - img_height_points) / 2

        #draw th image on the pdf canvas at the calculated center position
        c.drawImage(os.path.join(folder_name,img_filename),x_center,y_center,width=img_width_points,height=img_height_points)
        c.showPage()
    
    c.save()

def read_counter():
    try:
        with open("counter.txt","r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 1

def write_counter(counter):
    with open("counter.txt","w") as file:
        file.write(str(counter))
def main():
    initial_delay=3
    interval = 2 # set the interval of time in seconds
    num_screenshots = 3 # sets the number of screenshots
    
    print("waiting for {initial_delay} seconds before taking the first screenshot...")

    time.sleep(initial_delay)

    pdf_counter=read_counter()
    folder_name = f"screenshot{pdf_counter}"
    create_folder(folder_name)

    pdf_filename=f"screenshots_{pdf_counter}.pdf"

    screenshots = []

    for i in range(1,num_screenshots +1):
        screenshot = take_screenshot()
        screenshot_filename = f"screenshot_{pdf_counter}_{i}.png"
        save_screenshot(screenshot, folder_name,screenshot_filename)
        screenshots.append(screenshot_filename)
        time.sleep(interval)
    

    pdf_filename = f"folder_name.pdf"
    convert_to_pdf(screenshots, pdf_filename, folder_name)



    pdf_counter+=1
    write_counter(pdf_counter)

if __name__ == "__main__":
    main()