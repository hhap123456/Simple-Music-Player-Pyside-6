from time import strftime, gmtime

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QTimer, QSize, Qt
from PySide6.QtGui import QPixmap

from Ui_Player import Ui_MainWindow
from models import PlayerModel
from models import DirWalker
from MediaPlayer import MediaPlayer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.modelDir = DirWalker(r"C:\Users\hosse", "db_Json")
        self.modelPlayer = PlayerModel(data=self.modelDir.load())
        self.player = MediaPlayer()
        # self.modelDir.moveToJson()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_widgets)

        # Widgets
        self.listView.setModel(self.modelPlayer)
        self.listView.pressed.connect(self.on_selection)

        self.refresh()

        # Line Edit
        # self.lineEdit.textChanged.connect()

        self.update_butt.pressed.connect(self.update_db)

        self.playPause_butt.pressed.connect(self.play_pause)
        self.next_butt.pressed.connect(self.next)
        self.prev_butt.pressed.connect(self.previous)

        self.horizontalSlider.sliderReleased.connect(self.slider_released)
        self.horizontalSlider.sliderMoved.connect(self.change_labelTime)

        self.dialVolume.valueChanged.connect(self.on_volume_changed)
        self.dialVolume.setValue(100)

        self.lcdVolume.setStyleSheet("QLCDNumber { background-color: green }")

    def show_thumbnail(self):
        self.player.get_thumbnail()

        pixmap = QPixmap('album_cover.jpg')
        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)

        self.labelImage.setPixmap(scaled_pixmap)

    def on_selection(self, index):
        self.player.selectedMusic = self.modelPlayer.playlist[index.row()][1]

    def on_volume_changed(self):
        volume = self.dialVolume.value()

        if volume >= 99:
            volume = 100  # max

        self.player.set_volume(volume / 100)
        self.update_lcd(volume)

    def update_db(self) -> None:
        self.modelDir.moveToJson()
        self.modelPlayer.playlist = self.modelDir.load()
        self.refresh()

    def get_music_data(self):
        indexes = self.listView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()
            address, name = self.modelPlayer.playlist[row]

            return address, name

    def play_pause(self):
        if self.player.isPlaying and not self.player.new_select():
            self.horizontalSlider.setEnabled(False)
            self.player.pause()

        elif not self.player.isPlaying:

            address, name = self.get_music_data()
            self.horizontalSlider.setEnabled(True)

            self.player.play(address)

            self.timer.start(300)

        else:
            self.player.pause()

    def next(self):
        current_index = self.listView.currentIndex()

        next_row = current_index.row() + 1

        if next_row < self.modelPlayer.rowCount():
            next_index = self.modelPlayer.index(next_row, 0)
            self.listView.setCurrentIndex(next_index)

            if self.player.isPlaying:
                address, name = self.get_music_data()
                self.player.play(address)
                self.update_widgets()

    def previous(self):
        current_index = self.listView.currentIndex()

        prev_row = current_index.row() - 1

        if prev_row < self.modelPlayer.rowCount():
            prev_index = self.modelPlayer.index(prev_row, 0)
            self.listView.setCurrentIndex(prev_index)

            if self.player.isPlaying:
                address, name = self.get_music_data()
                self.player.play(address)
                self.update_widgets()

    def slider_released(self):
        time_pos = self.horizontalSlider.value()
        address, name = self.get_music_data()

        self.player.pause()

        self.player.play(address, start=time_pos)
        self.player.set_pos(time_pos)
        print(self.player.get_current_pos())

        self.timer.start(300)

    def change_labelTime(self):
        time_pos = self.horizontalSlider.value()
        self.labelTime.setText(strftime("%M:%S", gmtime(time_pos )))

    def update_widgets(self) -> None:
        self.update_slider()
        self.update_time()
        self.on_volume_changed()
        self.show_thumbnail()
        self.go_next()

    def update_time(self) -> None:
        currentTime = int(self.player.get_current_pos())
        formatted = strftime("%M:%S", gmtime(currentTime))

        self.labelTime.setText(formatted)

    def update_slider(self):
        music_pos = self.player.get_current_pos()
        music_length = self.player.get_time()

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(music_length)
        self.horizontalSlider.setValue(music_pos)

    def update_lcd(self, value):
        self.lcdVolume.display(value)
        self.lcdVolume.show()

    def go_next(self):
        if not self.player.get_busy_state():
            self.next()

    def refresh(self):
        self.modelPlayer.layoutChanged.emit()


app = QApplication()
window = MainWindow()
window.show()
app.exec()