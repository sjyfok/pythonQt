# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:52:10 2017

@author: song
"""

from distutils.core import setup
import py2exe

#setup(windows=[{"script" : "swbptester.py"}], options={"py2exe" : {"includes" : ["sip", "PyQt4._qt"]}})
setup(console=['swbptester.py'])