from typing import Tuple

import cv2
import numpy as np


class ImageHandler:
    """Класс для обработки изображений."""

    def load_image(image_path: str) -> np.ndarray:
        """Считывает изображение из файла.

        :Args: image_path (str): Путь к файлу изображения.

        :Returns: np.ndarray: Загруженное изображение.

        :Raises: ValueError: Если изображение не удалось загрузить.
        """
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Ошибка: не удалось загрузить изображение по пути {image_path}")
        return image

    def display_image(image: np.ndarray, title: str) -> None:
        """Отображает изображение с заданным заголовком.

        :Args: image (np.ndarray): Изображение для отображения.
        :Args: title (str): Заголовок окна.
        """
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(image: np.ndarray, save_path: str) -> None:
        """Сохраняет изображение по заданному пути.

        :Args: image (np.ndarray): Изображение для сохранения.
        :Args: save_path (str): Путь для сохранения изображения.
        """
        cv2.imwrite(save_path, image)
        print(f"Изображение сохранено по пути: {save_path}")

    def print_image_size(image: np.ndarray) -> None:
        """Выводит размер изображения.

        :Args: image (np.ndarray): Изображение для получения размера.
        """
        height, width, _ = image.shape
        print(f"Размер изображения: {width}x{height}")

    def crop_image(image: np.ndarray, crop_size: Tuple[int, int]) -> np.ndarray:
        """Обрезает изображение до заданных размеров.

        :Args: image (np.ndarray): Изображение для обрезки.
        :Args: crop_size (Tuple[int, int]): Размер обрезки (высота, ширина).

        Returns:
            np.ndarray: Обрезанное изображение.
        """
        crop_height, crop_width = crop_size
        return image[0: crop_height, 0: crop_width]
