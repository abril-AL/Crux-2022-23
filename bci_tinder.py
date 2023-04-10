#!/usr/bin/python

'''
  bci_tinder.py
  ---------------
  UCLA Crux UCLA - Team 12
  Author - Abril Aguilar Lopez
  ---------------
  This is the main program for the BCI tinder app
  This include the implementation of the LSL stream we will use
  for real time data streaming from the board to the program

  Package Requirements:
     pylsl (version 1.10.5 or greater) 
     pyserial (version 3.1.1 or greater) 
     numpy (version 1.11.1 or greater) 
     pyqtgraph (version 0.9.10 or greater) (optional: needded for GUI functionality only)
     scipy (version 0.17.1 or greater) (optional: needed for GUI functionality only) 
  To install packages, use requirements file shortcut and some manual installations: 
     `pip install -r ./misc/requirements.txt --use-pep517`
     `pip install numpy`
     `python -m pip install scipy`
  Also need to separately install PyQt4 to use GUI features:
     `pip install sip`

  To run: `python bci_tinder.py`. 
  For more information, see Github:
  https://github.com/abril-AL/Crux
'''

import pylsl
from pyOpenBCI import OpenBCIBoard
# to stream data, use appropriate port (macro to represent this port) 
lsl_port = 'openbci_eeg1' # Time Series Data Type

#to do: lsl stuff and other neurokit stuff


def main(argv):
  
  # if no arguments are provided, default to the GUI application
  if not argv:
    import lib.gui as gui
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    window = gui.GUI()
    sys.exit(app.exec_())
  else:
    sys.exit(app.exec_())
