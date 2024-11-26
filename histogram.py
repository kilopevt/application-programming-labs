import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(image: np.ndarray) -> None:
    """Строит и отображает гистограмму изображения.

    :Args: image (np.ndarray): Изображение для построения гистограммы.
    """
    color = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность')
    plt.ylabel('Частота')
    plt.legend(['Синий', 'Зелёный', 'Красный'])
    plt.grid()
    plt.show()
