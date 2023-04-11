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

import sys
import numpy as np # pip install numpy
import pandas as pd # pip install pandas
import neurokit2 as nk # pip install neurokit2 ( from cmd administator )
# pip install mne ( as cmd admin )
# python -m pip install brainflow


def main(argv):
  #TODO: change to signal collected via lsl
  signal = []
  signal = 

    

if __name__ == '__main__':
  main(sys.argv[1:])
  
