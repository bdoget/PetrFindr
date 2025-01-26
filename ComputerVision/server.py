from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import os
import compare
import re

app = Flask(__name__)
CORS(app)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Check if an image file is in the request
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        # Get the image file from the request
        image_file = request.files['image']
        
        if image_file.filename == '':
            return jsonify({"error": "No image selected"}), 400
        
        # Save the image temporarily
        file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(file_path)
        
        ans = compare.do_backend(file_path)
        ans = ans.rsplit('_', 1)[0] # stripping .txt


        # def add_space_before_capitals(text):
        #     return re.sub(r'(?<!^)([A-Z])', r' \1', text)

        processed_text = re.sub(r'(?<!^)([A-Z])', r' \1', ans)
        os.remove(file_path)        # Clean up the saved image file

        return jsonify({"message": processed_text})     # Send the processed text back as a response
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
