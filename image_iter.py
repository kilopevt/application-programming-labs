import csv


class ImageIterator:
    def __init__(self, annotation_file: str):
        """
        Initializes the image iterator.

        :param annotation_file: The path to the file with annotations.
        """
        self.annotation_file = annotation_file
        self.image_paths = []
        self.current_index = 0
        self.load_annotations()

    def load_annotations(self):
        """
        Loads image annotations from a CSV file.
        """
        with open(self.annotation_file, mode='r') as f:
            reader = csv.reader(f)
            next(reader)
            self.image_paths = [row[0] for row in reader]

    def __iter__(self):
        """
        Returns an iterator object.
        """
        return self

    def __next__(self) -> str:
        """
        Returns the following path to the image.

        :return: The path to the next image.
        """
        if self.current_index < len(self.image_paths):
            image_path = self.image_paths[self.current_index]
            self.current_index += 1
            return image_path
        else:
            raise StopIteration
