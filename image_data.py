import os
from typing import List, Tuple

import pandas as pd


class ImageData:
    """Класс для работы с данными изображений."""

    def __init__(self, image_folder: str) -> None:
        """
        Инициализация класса ImageData.

        :param image_folder: Путь к папке с изображениями.
        """
        self.image_folder = image_folder
        self.data_frame = pd.DataFrame()

    def create_dataframe(self) -> pd.DataFrame:
        """
        Создает DataFrame с абсолютными и относительными путями к файлам изображений.

        :return: DataFrame с путями к изображениям.
        """
        image_paths = []
        for root, _, files in os.walk(self.image_folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    abs_path = os.path.abspath(os.path.join(root, file))
                    rel_path = os.path.relpath(abs_path, self.image_folder)
                    image_paths.append((abs_path, rel_path))

        self.data_frame = pd.DataFrame(image_paths, columns=['Absolute Path', 'Relative Path'])
        return self.data_frame

    def add_image_dimensions(self, dimensions: List[Tuple[int, int, int]]) -> None:
        """
        Добавляет размеры изображений в DataFrame.

        :param dimensions: Список кортежей с размерами изображений (высота, ширина, глубина).
        """
        self.data_frame[['Height', 'Width', 'Depth']] = pd.DataFrame(dimensions)
