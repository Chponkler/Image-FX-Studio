from PIL import Image
import numpy as np


def pixelate_image(img, block_size):
    """Пикселизирует изображение с заданным размером блока"""
    img = img.convert("RGB")
    image_array = np.array(img)

    h, w = image_array.shape[:2]
    h_new = h // block_size * block_size
    w_new = w // block_size * block_size

    # Обрезаем изображение до размеров, кратных block_size
    image_array = image_array[:h_new, :w_new]

    # Пикселизация
    temp = image_array.reshape(h_new // block_size, block_size, w_new // block_size, block_size, 3)
    pixelated = temp.mean(axis=(1, 3)).astype(np.uint8)

    # Масштабируем обратно к исходному размеру
    pixelated = np.repeat(np.repeat(pixelated, block_size, axis=0), block_size, axis=1)

    return Image.fromarray(pixelated)