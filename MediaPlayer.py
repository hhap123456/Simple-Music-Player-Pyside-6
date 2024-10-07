from pygame import mixer
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image
import io


class MediaPlayer():
    def __init__(self):
        self.isPlaying = False  # not playing
        self.playedMusics = []           # list of played music
        self.currentMusic = None         # current music

        self.selectedMusic = None
        mixer.init()

        self.__address = None
        self.__skipped_time = 0

    def play(self, address, loops=0, start=0):
        self.__skipped_time = 0
        self.__address = address
        self.currentMusic = address[address.rfind("\\") + 1:]

        mixer.music.load(address)
        mixer.music.play(loops, start)
        self.isPlaying = True

        self.playedMusics.append(self.currentMusic)

    def pause(self):
        mixer.music.pause()
        self.isPlaying = False

    def set_pos(self, pos):
        self.__skipped_time += pos

    @staticmethod
    def set_volume(volume):
        mixer.music.set_volume(volume)

    @staticmethod
    def get_busy_state():
        return mixer.music.get_busy()

    def get_pos(self):
        return self.__skipped_time

    def get_last(self):
        return self.playedMusics[-1]

    def get_thumbnail(self):
        audio = MP3(self.__address, ID3=ID3)

        # چک کردن تگ ID3 برای پیدا کردن کاور آلبوم
        for tag in audio.tags.values():
            if isinstance(tag, APIC):  # اگر تگ تصویر APIC باشد
                # ذخیره تصویر به عنوان فایل
                with open('album_cover.jpg', 'wb') as img_file:
                    img_file.write(tag.data)

                break

    def new_select(self):
        if self.currentMusic != self.selectedMusic:
            return True
        return False

    def get_time(self):
        audio = MP3(self.__address)
        return audio.info.length

    def get_current_pos(self):

        return mixer.music.get_pos() / 1000 + self.__skipped_time
