from utils import * 
import os

def get_image_filenames(dir):
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

def compareEverything(i,siftSim, imgList):
    scores = dict()
    for j in range(len(imgList)):
        scores[j] = siftSim.calculate_results_for(i,j)
    sorted_scores = sorted(scores,key=lambda x:-scores[x])
    
    print(f"Comparing Picture {i}: {imgList[i]}")
    print(f"Top 10 :",end="")
    print(", ".join([f"{imgList[sorted_scores[i]]}/ {scores[sorted_scores[i]]}" for i in range(1,1+10)]))


# def getBest(img, siftSim, imgList):
#     scores = dict()
#     for j in range(len(imgList)):
#         scores[j] = siftSim.calculate_results_for(i,j)
#     return max(scores,key=lambda x:scores[x])

#     sorted_scores = sorted(scores,key=lambda x:-scores[x])


def do_backend(imgName):
    img = image_resize_train(cv2.imread(imgName,0))

    imgList = get_image_filenames("data/images")
    siftSim = SiftSimilarity(imgList, None)
    kp, desc = siftSim.compute_sift(img)

    scores = dict()
    for i in range(len(imgList)):
        scores[i] = siftSim.calculate_score_back_end(i,kp,desc)
    return max(scores, key=lambda x:scores[x])



def main():
    imgList = get_image_filenames("data/images")
    siftSim = SiftSimilarity(imgList, None)
    for i in range (0,len(imgList),5):
        compareEverything(i,siftSim, imgList)
    # compareEverything(0, siftSim, imgList)
    

if __name__ == "__main__":
    main()
