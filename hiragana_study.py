import sys, random
from functools import partial

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton

# All the Hiragana I need to study
# We define tuples to assure none are modified at runtime
__hira = (('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e', 'え'), ('o', 'お'),
          ('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ'),
          ('sa', 'さ'), ('shi', 'し'), ('su', 'す'), ('se', 'せ'), ('so', 'そ'),
          ('ta', 'た'), ('chi', 'ち'), ('tsu', 'つ'), ('te', 'て'), ('to', 'と'),
          ('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の'),
          ('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ'),
          ('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も'),
          ('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ'),
          ('ga', 'が'), ('gi', 'ぎ'), ('gu', 'ぐ'), ('ge', 'げ'), ('go', 'ご'),
          ('za', 'ざ'), ('ji', 'じ'), ('zu', 'ず'), ('ze', 'ぜ'), ('zo', 'ぞ'),
          ('da', 'だ'), ('dji', 'ぢ'), ('dzu', 'づ'), ('de', 'で'), ('do', 'ど'),
          ('ba', 'ば'), ('bi', 'び'), ('bu', 'ぶ'), ('be', 'べ'), ('bo', 'ぼ'),
          ('pa', 'ぱ'), ('pi', 'ぴ'), ('pu', 'ぷ'), ('pe', 'ぺ'), ('po', 'ぽ'),
          ('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ'),
          ('wa', 'わ'), ('wo', 'を'),
          ('v', 'ゔ'), ('n', 'ん'))


def get_rand_hira(level):
    """ return random index from __hira tuple """
    index = random.randint(0, level)
    return [__hira[index][0], __hira[index][1]]


# Get Hiragana
randHira = get_rand_hira(72)
sound = randHira[0]
sym = randHira[1]


class HiraganaStudy(QWidget):

    def __init__(self):
        super().__init__()

        self.label = QLabel(sym, self)
        self.label.move(20, 20)

        reveal = QPushButton("Reveal Answer", self)
        reveal.clicked.connect(self.on_click)

        self.setGeometry(300, 150, 1280, 720)
        self.setWindowTitle("Hiragana Study App - By: Malik Tillman")

    def on_click(self):
        self.label.setText(sound)


if __name__ == '__main__':
    """" Initial point of application """
    app = QApplication([])
    hs = HiraganaStudy()
    hs.show()

    sys.exit(app.exec_())
