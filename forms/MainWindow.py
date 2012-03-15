# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4.QtGui import QMainWindow, QFileDialog
from PyQt4.QtCore import pyqtSignature

from Ui_MainWindow import Ui_MainWindow

from FreeRTOSFileConfig import FreeRTOSFileConfig

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fileConfig = None
    
    def UpdateDisplay(self):
        if isinstance(self.fileConfig, FreeRTOSFileConfig):
            # Enable GoupBox
            self.groupBox.setEnabled(True)
            # Update data to display
            self.checkBoxPreemptive.setChecked(self.fileConfig.getPreemption())
            self.checkBoxUseIdleHook.setChecked(self.fileConfig.getUseIdleHook())
            self.checkBoxUseTickHook.setChecked(self.fileConfig.getUseTickHook())
        
    @pyqtSignature("bool")
    def on_checkBoxPreemptive_clicked(self, checked):
        """
        Change FreeRTOS preemption configuration.
        """
        self.fileConfig.setPreemption(checked)
    
    @pyqtSignature("")
    def on_actionOpen_triggered(self):
        """
        Open dialog to select the configuration file to open.
        """
        fileName = QFileDialog.getOpenFileName(self, self.tr("Open File"), "."  , self.tr("FreeRTOS config file (*.h)"))
        
        if (len(fileName)>0):
            print "Valid file name"
            self.fileConfig = FreeRTOSFileConfig(fileName)
            self.UpdateDisplay()
            
        else:
            print "Not valid file name"
        # TODO: not implemented yet
         #raise NotImplementedError
    
    @pyqtSignature("")
    def on_actionClose_triggered(self):
        """
        Slot documentation goes here.
        """
        self.fileConfig.SaveFile()
    
    @pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Request confirmation before closing
        del(self.fileConfig)
        self.close()
    
    @pyqtSignature("")
    def on_actionHelp_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("bool")
    def on_checkBoxUseIdleHook_clicked(self, checked):
        """
        Change FreeRTOS 'Use idle hook' configuration.
        """
        self.fileConfig.setUseIdleHook(checked)
    
    @pyqtSignature("bool")
    def on_checkBoxUseTickHook_clicked(self, checked):
        """
        Change FreeRTOS 'Use Tick Hook' configuration
        """
        self.fileConfig.setUseTickHook(checked)
