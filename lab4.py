from image_data import ImageData
from data_analysis import (
    filter_by_dimensions,
    add_area_column,
    sort_by_area,
    plot_area_distribution
)


def main() -> None:
    image_folder = '..\lab4\downloads'
    image_data = ImageData(image_folder)

    try:
        df = image_data.create_dataframe()
        dimensions = [(600, 800, 3), (400, 600, 3), (300, 400, 3),
                      (1080, 1920, 3), (480, 720, 3), (100, 200, 3)]
        image_data.add_image_dimensions(dimensions)

        # Вычисляем статистику
        print(df.describe())

        # Фильтруем по размерам
        max_width = 4000
        max_height = 3000
        filtered_df = filter_by_dimensions(df, max_width, max_height)

        # Добавляем площадь и сортируем
        df_with_area = add_area_column(filtered_df)
        sorted_df = sort_by_area(df_with_area)

        # Строим гистограмму
        plot_area_distribution(sorted_df)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
