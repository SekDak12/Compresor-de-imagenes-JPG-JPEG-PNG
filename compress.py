from PIL import Image
import os
def compress(dowloadsfolder, newfolder):
    dowloadsfolder = dowloadsfolder
    basura = newfolder
    if __name__ == "__main__" :
        for filename in os.listdir(dowloadsfolder):
            name, extension = os.path.splitext(dowloadsfolder + filename)
            
            if extension == ".png" or extension == ".jpg" or extension == ".jpeg":
                picture = Image.open(dowloadsfolder + filename)
                picture.save(basura + "compressed__" + filename, optimize=True, quality=65)
                os.remove(dowloadsfolder + filename)
        
print("What is the path of the folder you want to compress?")
dowloadsfolder = input()
print("What is the path of the folder you want to save the compressed files?")
newfolder = input()

compress(dowloadsfolder, newfolder)
