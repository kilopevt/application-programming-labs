import os
from typing import List

from icrawler.builtin import GoogleImageCrawler


def download_images(keyword: str, download_folder: str, num_images: int = 50) -> List[str]:
    """
    Downloads images from Google by the specified keyword.

    :param keyword: The keyword for image search.
    :param download_folder: A folder for saving images.
    :param num_images: The maximum number of images to download (50 by default)

    :return: A list of paths to uploaded images.
    """
    crawler = GoogleImageCrawler(storage={'root_dir': download_folder})
    crawler.crawl(keyword=keyword, max_num=num_images)

    image_paths = []
    for dirname, _, filenames in os.walk(download_folder):
        for filename in filenames:
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_paths.append(os.path.join(dirname, filename))

    return image_paths
