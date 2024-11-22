import argparse
import os

from download_imag import download_images
from image_iter import ImageIterator
from save_annotations import save_annotations


def get_args() -> tuple:
    parser = argparse.ArgumentParser(description="download images by keyword.")
    parser.add_argument("keyword", type=str, help="keyword for finding images")
    parser.add_argument("download_folder", type=str, help="download folder")
    parser.add_argument("annotation_file", type=str, help="file for saving annotations")

    args = parser.parse_args()

    keyword = args.keyword
    download_folder = args.download_folder
    annotation_file = args.annotation_file

    return keyword, download_folder, annotation_file


def main():
    keyword, download_folder, annotation_file = get_args()

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    image_paths = download_images(keyword, download_folder)

    save_annotations(image_paths, annotation_file)

    image_iterator = ImageIterator(annotation_file)
    for image_path in image_iterator:
        print(image_path)


if __name__ == "__main__":
    main()
