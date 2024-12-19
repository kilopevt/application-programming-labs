import csv
import os


class ImageIterator:
    def __init__(self, annotation_path: str) -> None:
        """Эта функция извлекает абсолютный путь к файлу из строки и добавляет его в список.

        :param annotation_path: путь к файлу с аннотацией
        """
        self.image_paths = []
        self.current_index = 0

        try:
            with open(annotation_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)

                for row in csv_reader:
                    if len(row) < 2:
                        raise ValueError(f"Некорректная строка в CSV: {row}")
                    abs_path = row[1]
                    if not os.path.isfile(abs_path):
                        print(f"Предупреждение: Изображение по пути {abs_path} не существует.")
                    self.image_paths.append(abs_path)

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {annotation_path} не найден.")
        except Exception as e:
            raise Exception(f"Ошибка при чтении файла аннотаций: {e}")

    def __iter__(self) -> 'ImageIterator':
        """
        Возвращает текущий экземпляр класса, чтобы сделать его итерируемым.

        :return: текущий экземпляр класса
        """
        return self

    def __next__(self) -> str:
        """
        Получает следующий элемент из списка абсолютных путей к изображениям.

        :return: путь к текущему изображению
        """
        if self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index]
            self.current_index += 1
            return image_path
        else:
            raise StopIteration

    def reset(self) -> None:
        """
        Сбросит итератор, чтобы начать просмотр изображений с самого начала.
         """
        self.current_index = 0
