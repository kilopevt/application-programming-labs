import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)

from iterator import ImageIterator

OPEN_DATASET_TEXT = "Open dataset."
NEXT_IMG_TEXT = 'Cant open pic press "Next img" to continue viewing.'


class MyWindow(QWidget):
    def __init__(self):
        """
        Инициализирует главное окно.
        """
        super().__init__()
        self.iterator = None
        self.path = None

        self.open_btn = QPushButton("Open annotation-file")
        self.next_btn = QPushButton("Next img")
        self.image_label = QLabel(OPEN_DATASET_TEXT)
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.init_ui()

    def init_ui(self) -> None:
        """
        Настройка интерфейс.
        """
        self.setGeometry(100, 100, 600, 400)
        self.setFixedSize(600, 400)
        self.setWindowTitle("Cow")

        self.next_btn.setEnabled(False)
        self.image_label.setScaledContents(True)

        self.hbox.addWidget(self.open_btn)
        self.hbox.addWidget(self.next_btn)

        self.vbox.addStretch(1)
        self.vbox.addWidget(self.image_label)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

        self.open_btn.clicked.connect(self.open_annotations)
        self.next_btn.clicked.connect(self.show_next_img)

    def open_annotations(self) -> None:
        """
        Загружает файл аннотации и передает его итератору.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотаций", "",
                                                   "Text Files (*.csv);;All Files (*)", options=options)
        if file_name:
            try:
                self.iterator = ImageIterator(file_name)
                self.next_btn.setEnabled(True)
                self.show_next_img()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл аннотаций: {e}")

    def show_next_img(self) -> None:
        """
        Отображение следующего изображение в наборе данных.
        """
        if self.iterator:
            try:
                self.path = next(self.iterator)
                if not os.path.isfile(self.path):
                    raise FileNotFoundError(f"Изображение {self.path} не найдено.")

                pixmap = QPixmap(self.path)

                if pixmap.isNull():
                    raise ValueError("Изображение не может быть загружено.")
                self.image_label.setPixmap(pixmap)

            except (ValueError, FileNotFoundError) as e:
                self.image_label.setText(NEXT_IMG_TEXT)

            except StopIteration:
                self.end_of_images()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ошибка: {e}")

    def end_of_images(self) -> None:
        """
        Обработка случая, когда в наборе данных больше нет изображений.
        """
        reply = QMessageBox.question(
            self,
            "Конец",
            "Изображения закончились. Хотите начать заново?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.iterator.reset()
            self.show_next_img()
        else:
            self.image_label.setText(OPEN_DATASET_TEXT)
            self.next_btn.setEnabled(False)


def main() -> None:
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
