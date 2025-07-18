import sys
import pyautogui
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer

class TaskbarDog(QLabel):
    def __init__(self):
        super().__init__()

        # Load both dog animations
        self.movie_run = QMovie("dog_run.gif")
        self.movie_idle = QMovie("dog_idle.gif")
        self.current = None

        # Start with idle dog
        self.setMovie(self.movie_idle)
        self.movie_idle.start()

        # Make the window transparent and always-on-top
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(128, 128)

        # Place it on bottom-left near taskbar
        screen_height = pyautogui.size().height
        self.move(236, screen_height - 100 )  # Adjust -40 if needed
        self.show()

        # Mouse tracking
        self.prev_mouse = pyautogui.position()
        self.timer = QTimer()
        self.timer.timeout.connect(self.track_mouse)
        self.timer.start(50)  # Refresh every 50 ms

    def track_mouse(self):
        current_pos = pyautogui.position()
        if current_pos != self.prev_mouse:
            self.set_animation(self.movie_run)
        else:
            self.set_animation(self.movie_idle)
        self.prev_mouse = current_pos

    def set_animation(self, movie):
        if self.current is movie:
            return
        if self.current:
            self.current.stop()
        self.current = movie
        self.setMovie(movie)
        movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dog = TaskbarDog()
    sys.exit(app.exec_())
