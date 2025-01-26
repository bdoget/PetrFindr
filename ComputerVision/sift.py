from utils import * 
import os

def get_image_filenames(dir):
    # Returns a list of image filenames with their full path in the given folder dir

    if not os.path.exists(dir):
        print(f"Error: Folder '{dir}' does not exist.")
        return None
    
    # image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif", ".webp"} 
    extensions = {".jpg", ".jpeg", ".png"}  # Supported image extensions
    out = []
    for file in os.listdir(dir):
        if os.path.splitext(file)[1].lower() in extensions:     # Check file extension
            out.append(file)         # Add full file path
    return out


def process_images(dir, images):
    imagesBW = []
    for imageName in images:
        imagePath = "data/images/" + str(imageName)
        imagesBW.append(image_resize_train(cv2.imread(imagePath,0))) # flag 0 means grayscale
    return imagesBW


def main():
    dir = "data/images"
    imgList = get_image_filenames(dir)          # print("Images found:\n" + "".join(f"{img}\n" for img in imageList),end = "")
    imagesBW = process_images(dir, imgList)     # print(len(imagesBW))
    
    siftSim = SiftSimilarity(imgList,imagesBW)
    keypoints, descriptors = siftSim.generate_keypoints_desc()
    
if __name__ == "__main__":
    main()
