from flask import Flask, render_template, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from pixelate import pixelate_image
from glitch import apply_glitch
from utils import resize_image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_image():
    data = request.json
    image_data = data['image'].split(',')[1]
    effect_type = data.get('effect_type', 'pixelate')

    img = Image.open(BytesIO(base64.b64decode(image_data)))
    img = resize_image(img)

    if effect_type == 'pixelate':
        block_size = data['block_size']
        processed_img = pixelate_image(img, block_size)
    elif effect_type == 'glitch':
        intensity = data.get('intensity', 5)
        processed_img = apply_glitch(img, intensity)

    buffered = BytesIO()
    processed_img.save(buffered, format="PNG")
    processed_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({
        'processed_image': processed_base64
    })

if __name__ == '__main__':
    app.run(debug=True)  # debug=True для автоматической перезагрузки