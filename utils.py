from PIL import Image
import io
import base64

def image_to_base64(img):
    """Конвертирует изображение в base64 строку"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def resize_image(img, max_size=500):
    """Изменяет размер изображения для отображения"""
    width, height = img.size
    if width > max_size or height > max_size:
        ratio = min(max_size/width, max_size/height)
        new_size = (int(width * ratio), int(height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
    return img