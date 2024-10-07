from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

app = QApplication([])

# ساختن یک پنجره اصلی
window = QWidget()
layout = QVBoxLayout()

# ساختن یک QLabel برای نمایش عکس
label = QLabel()

# بارگذاری عکس از فایل
pixmap = QPixmap('album_cover.jpg')

# تغییر اندازه عکس به اندازه 300x300 (یا هر اندازه دلخواه)
scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)

# تنظیم عکس در QLabel
label.setPixmap(scaled_pixmap)

# اضافه کردن QLabel به layout
layout.addWidget(label)

# تنظیم layout در پنجره
window.setLayout(layout)
window.show()

app.exec()
