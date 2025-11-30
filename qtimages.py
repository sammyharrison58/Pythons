from __future__ import annotations

import sys
import logging
from pathlib import Path
from typing import Optional

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


logger = logging.getLogger(__name__)


def default_image_path() -> Path:
    # images/10.jpg next to this script (not dependent on CWD)
    return Path(__file__).with_name("images") / "10.jpg"


class MainWindow(QMainWindow):
    def __init__(self, image_path: Optional[Path] = None) -> None:
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(500, 500)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self._original_pixmap: Optional[QPixmap] = None

        path = image_path or default_image_path()
        self._load_image(path)
        self._update_pixmap_to_fit()

    def _load_image(self, path: Path) -> None:
        if not path.exists():
            logger.warning("Image path does not exist: %s", path)
            self.label.setText(f"Image not found:\n{path}")
            self._original_pixmap = None
            return

        pixmap = QPixmap(str(path))
        if pixmap.isNull():
            logger.warning("Failed to load image (null pixmap): %s", path)
            self.label.setText(f"Failed to load image:\n{path}")
            self._original_pixmap = None
            return

        self._original_pixmap = pixmap
        # Clear any previous text if successfully loaded
        self.label.setText("")

    def _update_pixmap_to_fit(self) -> None:
        if not self._original_pixmap or self._original_pixmap.isNull():
            return
        target_size: QSize = self.label.size()
        if target_size.width() <= 0 or target_size.height() <= 0:
            return
        scaled = self._original_pixmap.scaled(
            target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.label.setPixmap(scaled)

    def resizeEvent(self, event) -> None:  # type: ignore[override]
        super().resizeEvent(event)
        self._update_pixmap_to_fit()


def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s]: %(message)s",
    )

    app = QApplication(sys.argv if argv is None else argv)
    window = MainWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
