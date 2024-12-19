import pandas as pd
import matplotlib.pyplot as plt


def filter_by_dimensions(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по максимальным значениям ширины и высоты.

    :param df: Исходный DataFrame.
    :param max_width: Максимальная ширина.
    :param max_height: Максимальная высота.
    :return: Отфильтрованный DataFrame.
    """
    filtered_df = df[(df['Height'] <= max_height) & (df['Width'] <= max_width)]
    return filtered_df


def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбец с площадью изображений в DataFrame.

    :param df: Исходный DataFrame.
    :return: DataFrame с добавленным столбцом площади.
    """
    df['Area'] = df['Height'] * df['Width']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортирует DataFrame по площади изображений.

    :param df: Исходный DataFrame.
    :return: Отсортированный DataFrame.
    """
    return df.sort_values(by='Area')


def plot_area_distribution(df: pd.DataFrame) -> None:
    """
    Строит гистограмму распределения площадей изображений.

    :param df: DataFrame с данными об изображениях.
    """
    plt.hist(df['Area'], bins=7, color='blue', alpha=0.7)
    plt.title('Распределение областей изображения')
    plt.xlabel('Площадь (пикселей)')
    plt.ylabel('Частота')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
