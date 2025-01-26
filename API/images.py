import requests
import os
from shhh import API_KEY

def fetch_streetview_image(location, heading, fov, pitch, size, api_key, output_dir, filename):
    base_url = "https://maps.googleapis.com/maps/api/streetview"

    params = {
        "size" : size,
        "location" : location,
        "heading" : heading,
        "fov" : fov,
        "pitch" : pitch,
        "key" : api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:  # if successful
        filepath = os.path.join(output_dir, filename)
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Image saved as {filepath}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    API_KEY = API_KEY
    LOCATION = "33.648705420569435, -117.84248843393041"  # DD coordinates
    HEADING = [0, 45, 90, 135, 180]
    FOV = 80  # field of view
    PITCH = 0  # camera pitch
    SIZE = "600x400"  # image size
    NAME = "StudentCenterStage"  # changes according to the doc Justin sent me

    output_dir = NAME
    os.makedirs(output_dir, exist_ok=True)

    for heading in HEADING:
        FILENAME = f"{NAME}-{heading}.jpg"
        fetch_streetview_image(LOCATION, HEADING, FOV, PITCH, SIZE, API_KEY, 
                               output_dir, FILENAME)
