import cv2
import pickle
import matplotlib.pyplot as plt
import os

# Resize Images
def image_resize_train(image):
    max_d = 1024
    height, width = image.shape
    aspect_ratio = width / height
    new_size = (int(max_d * aspect_ratio), max_d) if aspect_ratio < 1 else (max_d, int(max_d / aspect_ratio))
    return cv2.resize(image, new_size)

def image_resize_test(image):
    max_d = 1024
    height, width, channel = image.shape
    aspect_ratio = width / height
    new_size = (int(max_d * aspect_ratio), max_d) if aspect_ratio < 1 else (max_d, int(max_d / aspect_ratio))
    return cv2.resize(image, new_size)

class SiftSimilarity:
    def __init__(self, image_list=None, images_bw=None):
        """
        Initialize SiftSimilarity with optional image list and grayscale images.
        """
        self.image_list = image_list or []
        self.images_bw = images_bw or []
        self.sift = cv2.SIFT_create()
        self.bf = cv2.BFMatcher()

    # Compute SIFT features
    def compute_sift(self, image):
        return self.sift.detectAndCompute(image, None)

    # Generate keypoints and descriptors
    def generate_keypoints_desc(self):
        keypoints = []
        descriptors = []
        for i, image in enumerate(self.images_bw):
            # print(f"Processing image: {self.image_list[i]}")
            kp, desc = self.compute_sift(image)
            keypoints.append(kp)
            descriptors.append(desc)
            self.store_keypoints_descriptors(kp, desc, self.image_list[i])
        return keypoints, descriptors

    # Store keypoints and descriptors
    def store_keypoints_descriptors(self, keypoints, descriptors, image_name):
        deserialized_keypoints = [
            (kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id) for kp in keypoints
        ]
        keypoints_path = f"data/keypoints/{image_name.split('.')[0]}.txt"
        descriptors_path = f"data/descriptors/{image_name.split('.')[0]}.txt"

        os.makedirs(os.path.dirname(keypoints_path), exist_ok=True)
        os.makedirs(os.path.dirname(descriptors_path), exist_ok=True)

        with open(keypoints_path, 'wb') as kp_file:
            pickle.dump(deserialized_keypoints, kp_file)

        with open(descriptors_path, 'wb') as desc_file:
            pickle.dump(descriptors, desc_file)

    # Fetch keypoints and descriptors from file
    def fetch_keypoints(self, index):
        filepath = f"data/keypoints/{self.image_list[index].split('.')[0]}.txt"
        with open(filepath, 'rb') as file:
            deserialized_keypoints = pickle.load(file)
        return [cv2.KeyPoint(x=pt[0][0], y=pt[0][1], size=pt[1], angle=pt[2], response=pt[3], octave=pt[4], class_id=pt[5]) for pt in deserialized_keypoints]

    def fetch_descriptors(self, index):
        filepath = f"data/descriptors/{self.image_list[index].split('.')[0]}.txt"
        with open(filepath, 'rb') as file:
            return pickle.load(file)

    # Calculate matches
    def calculate_matches(self, desc1, desc2):
        matches1 = self.bf.knnMatch(desc1, desc2, k=2)
        matches2 = self.bf.knnMatch(desc2, desc1, k=2)

        good_matches = []
        for m, n in matches1:
            if m.distance < 0.7 * n.distance:
                good_matches.append(m)

        return good_matches

    # Calculate similarity score
    def calculate_score(self, matches, kp1_len, kp2_len):
        return 100 * (len(matches) / min(kp1_len, kp2_len))

    # Plot matches
    def get_plot(self, image1, image2, kp1, kp2, matches):
        image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        return cv2.drawMatches(image1_rgb, kp1, image2_rgb, kp2, matches, None, flags=2)

    # Calculate results for two images
    def calculate_results_for(self, i, j):
        kp1 = self.fetch_keypoints(i)
        desc1 = self.fetch_descriptors(i)
        kp2 = self.fetch_keypoints(j)
        desc2 = self.fetch_descriptors(j)

        matches = self.calculate_matches(desc1, desc2)
        score = self.calculate_score(matches, len(kp1), len(kp2))

        # image1 = image_resize_test(cv2.imread(f"data/images/{self.image_list[i]}"))
        # image2 = image_resize_test(cv2.imread(f"data/images/{self.image_list[j]}"))

        # plot = self.get_plot(image1, image2, kp1, kp2, matches)
        # plt.imshow(plot)
        # plt.show()
        return score
    
    def calculate_score_back_end(self, i, kp, desc):
        kp1 = self.fetch_keypoints(i)
        desc1 = self.fetch_descriptors(i)

        matches = self.calculate_matches(desc1, desc)
        score = self.calculate_score(matches, len(kp1), len(kp))
        return score

    def generate_keypoints_desc_back_end(self, image):
        kp, desc = self.compute_sift(image)
        return kp, desc
