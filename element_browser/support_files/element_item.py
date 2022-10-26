
import sys
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
import qdarkstyle
import threading

width = 200
height = 143


class ScrollingThumbnail(QWidget):
    """Icon widget item for the thumbnail"""

    def __init__(self,parent,image,rect=QRect(0, 0, width, height-25)):
        super(ScrollingThumbnail, self).__init__(parent)
        self.resize(width, height)
        self.image=image
        self.height = height-25
        self.width=width
        self.paused=False
        self.frame=5
        self.frames=20
        self.bar=False
        self.vis=True
        self.thumbRect=rect
        self.setMouseTracking(True)

    def leaveEvent(self, event):
        self.stop()

    def mouseMoveEvent(self,e):
        if(e.pos().y()>self.height*0.6):
            self.bar=True
            self.pause()
            self.frame=int(e.pos().x()/(self.width/self.frames))
            self.repaint()
        elif self.paused:
            self.paused=False
            self.bar=False
            self.play()

    def paintEvent(self,e):
        qP=QPainter()
        qP.begin(self)
        if self.vis:
            self.drawWidget(qP)
        qP.end()

    def drawWidget(self,qP):
        if not self.image.isNull():
            qP.drawPixmap(self.thumbRect,self.image,QRect(self.image.width()/self.frames*self.frame,0,self.image.width()/self.frames,self.image.height()))
            if self.bar:
                pen=QPen(QColor(255,255,255,50),self.height/60,cap=Qt.RoundCap)
                qP.setPen(pen)
                off=self.height/20
                inc=((self.width-(off*2))/(self.frames-1))
                qP.drawLine(off,self.height-off-20,off+(inc)*(self.frame),self.height-off-20)

    def play(self):
        if not self.paused:
            self.frame=(self.frame+1)%self.frames
            self.repaint()
            self.timer=threading.Timer(0.1,self.play)
            self.timer.start()

    def pause(self):
        try:
            self.timer.cancel()
        except:
            pass
        self.paused=True

    def stop(self):
        try:
            self.timer.cancel()
        except:
            pass
        self.frame=5
        self.repaint()
