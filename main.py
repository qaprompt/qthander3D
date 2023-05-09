import sys
import numpy as np
from mayavi import mlab
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton  
from PyQt5.QtCore import pyqtSlot

# 三维坐标点集 
points = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0],  
                   [1, 1, 0], [2, 1, 0], [3, 1, 0],  
                   [2, 2, 0], [3, 2, 0]])

# 三维连接线  
lines = np.array([[0, 1], [0, 4], [0, 7], [1, 2], [2, 3], 
                  [4, 5], [5, 6], [5, 8], [7, 8], [8, 9]])

# QT界面和按钮事件  
class Window(QWidget):
    def __init__(self):
        super().__init__()   
        
        self.initUI()
        
    def initUI(self):      
        # 添加三个视角按钮 
        v1_button = QPushButton('Side View')
        v1_button.clicked.connect(self.plot_sideview)
        
        v2_button = QPushButton('Front View')         
        v2_button.clicked.connect(self.plot_frontview)
        
        v3_button = QPushButton('Top View')         
        v3_button.clicked.connect(self.plot_topview) 
        
        # 添加到布局
        layout = QVBoxLayout()
        layout.addWidget(v1_button)
        layout.addWidget(v2_button)
        layout.addWidget(v3_button) 
        self.setLayout(layout)
        
    # 侧视图      
    @pyqtSlot()
    def plot_sideview(self):        
        mlab.figure(1, bgcolor=(1, 1, 1))
        mlab.points3d(points[:, 0], points[:, 1], points[:, 2], 
                      color=(1, 0, 0), scale_factor=0.1)
        mlab.plot3d(points[:, 0], points[:, 1], points[:, 2], color=(0, 0, 1))
        
    # 前视图
    @pyqtSlot()
    def plot_frontview(self):
        mlab.figure(2, bgcolor=(1, 1, 1))
        mlab.points3d(points[:, 0], points[:, 2], -points[:, 1], 
                      color=(1, 0, 0), scale_factor=0.1)
        mlab.plot3d(points[:, 0], points[:, 2], -points[:, 1], color=(0, 0, 1))  
        
    # 俯视图        
    @pyqtSlot() 
    def plot_topview(self):
        mlab.figure(3, bgcolor=(1, 1, 1)) 
        mlab.points3d(-points[:, 1], points[:, 0], points[:, 2], 
                      color=(1, 0, 0), scale_factor=0.1)
        mlab.plot3d(-points[:, 1], points[:, 0], points[:, 2], color=(0, 0, 1))      

if __name__ == '__main__':  
    app = QApplication(sys.argv) 
    window = Window()
    window.show()
    sys.exit(app.exec_()) 
