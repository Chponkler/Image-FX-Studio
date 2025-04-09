from PIL import Image
import random
import numpy as np


def apply_glitch(img, intensity=5):
    """Применяет глитч-эффект к изображению"""
    img = img.convert("RGB")
    width, height = img.size
    pixels = np.array(img)

    # Случайные смещения для создания эффекта
    for i in range(intensity):
        # Выбираем случайную область для смещения
        slice_height = random.randint(1, height // 10)
        slice_y = random.randint(0, height - slice_height)
        offset_x = random.randint(-intensity * 2, intensity * 2)

        # Смещаем выбранную область по горизонтали
        if offset_x > 0:
            pixels[slice_y:slice_y + slice_height, offset_x:] = pixels[slice_y:slice_y + slice_height,
                                                                :width - offset_x]
        elif offset_x < 0:
            offset_x = abs(offset_x)
            pixels[slice_y:slice_y + slice_height, :width - offset_x] = pixels[slice_y:slice_y + slice_height,
                                                                        offset_x:]

    # Добавляем цветовые искажения
    if intensity > 3:
        channel = random.randint(0, 2)
        pixels[:, :, channel] = np.roll(pixels[:, :, channel], random.randint(-intensity, intensity))

    return Image.fromarray(pixels)