import os
import requests
from UCIGrid import uci_grid
from shhh import API_KEY

API_KEY = API_KEY
BASE_URL = "https://maps.googleapis.com/maps/api/streetview"

def fetch_images_for_grid(grid, output_dir, 
                          headings=[0, 45, 90, 135, 180], size="600x400"):
    os.makedirs(output_dir, exist_ok=True)
    
    for i, (lat, lng) in enumerate(grid):
        folder_name = f"{i}+{lat},{lng}"
        folder_path = os.path.join(output_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        for heading in headings:
            params = {
                "size": size,
                "location": f"{lat},{lng}",
                "heading": heading,
                "key": API_KEY,
            }
            response = requests.get(BASE_URL, params=params)
            
            if response.status_code == 200:
                filename = f"{heading}-{lat}-{lng}.jpg"
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Saved: {file_path}")
            else:
                print(f"Failed to fetch image for {lat}, {lng} (heading {heading})")

# test_grid = [
#     (33.64686570400261, -117.84192695425821),  # Justin's Location
# ]

output_directory = "./GojoShrineLocation"
fetch_images_for_grid(uci_grid, output_directory)
