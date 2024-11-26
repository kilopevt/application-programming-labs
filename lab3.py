import argparse

from image_handler import ImageHandler
from histogram import plot_histogram


def parser() -> tuple[str, str, tuple[int, int]]:
    parser = argparse.ArgumentParser(description='Обработка изображения.')
    parser.add_argument('image_path', type=str, help='Путь к файлу изображения')
    parser.add_argument('save_path', type=str, help='Путь для сохранения результата')
    parser.add_argument('crop_size', type=int, nargs=2, help='Размер обрезки (высота ширина)')

    args = parser.parse_args()
    crop_size = tuple(args.crop_size)
    return (args.image_path, args.save_path, crop_size)


def main() -> None:
    """
    Основная функция обработки изображения.
    """

    image_path, save_path, crop_size = parser()
    try:
        image = ImageHandler.load_image(image_path)
        ImageHandler.print_image_size(image)
        plot_histogram(image)

        cropped_image = ImageHandler.crop_image(image, crop_size)
        ImageHandler.display_image(image, 'Исходное изображение')
        ImageHandler.display_image(cropped_image, 'Обрезанное изображение')

        ImageHandler.save_image(cropped_image, save_path)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
