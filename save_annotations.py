import os
from typing import List

import csv


def save_annotations(image_paths: List[str], annotation_file: str) -> None:
    """
    Saves image annotations to a CSV file.

    :param image_paths: A list of paths to images.
    :param annotation_file: The path to the file where the annotations will be saved.
    """
    with open(annotation_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['absolute_path', 'relative_path'])

        for image_path in image_paths:
            absolute_path = os.path.abspath(image_path)
            relative_path = os.path.relpath(image_path, start=os.path.dirname(annotation_file))
            writer.writerow([absolute_path, relative_path])
