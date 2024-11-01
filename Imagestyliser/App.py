from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# Dummy function to simulate style transfer
def stylize_image(image_bytes, prompt):
    # Here you would load your model and apply style transfer
    # For now, we just return the input image bytes as a placeholder
    return image_bytes

@app.route('/stylize', methods=['POST'])
def stylize():
    if 'image' not in request.files or 'prompt' not in request.form:
        return jsonify({"error": "Invalid input"}), 400
    
    image = request.files['image']
    prompt = request.form['prompt']
    
    image_bytes = image.read()
    stylized_image_bytes = stylize_image(image_bytes, prompt)
    
    return jsonify({"message": "Image stylized successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
