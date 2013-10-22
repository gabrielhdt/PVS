#!/usr/bin/env python
#
# -*- encoding: utf-8 -*-
#
# generated by wxGlade HG on Wed Jul 18 14:54:33 2012
#

# This is the main entry point of the editor.

import wx, os.path, sys
import util
import constants
import platform
import time
import logging
import logging.config
from ui.images import getIDELogo
from ui.frame import MainFrame
from ui.plugin import PluginManager
from wx.lib.pubsub import setupkwargs, pub 
from config import PVSIDEConfiguration
import pvscomm
import gc

class PVSEditorApp(wx.App):
    """The main class that starts the application and shows the main frame"""
    
    def OnInit(self):
        #wx.InitAllImageHandlers()
        
        # Splash Screen:
        #splash = wx.SplashScreen(getIDELogo(), wx.SPLASH_CENTRE_ON_SCREEN|wx.SPLASH_TIMEOUT, 1000, None, style=wx.SIMPLE_BORDER|wx.STAY_ON_TOP)
        #time.sleep(1)
        
        #Initiate Main Frame:
        mainFrame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        #favicon = wx.Icon(PVSIDEConfiguration().applicationFolder + "/images/pvs.ico", wx.BITMAP_TYPE_ICO, 32, 32)
        #wx.Frame.SetIcon(mainFrame, favicon)
        mainFrame.Show()
        logging.info("Main Frame initialized...") 
        pm = PluginManager()
        pm.initializePlugins(PVSIDEConfiguration().pluginDefinitions)
        operatingSystem = platform.system()
        if operatingSystem == "Windows":
            mainFrame.showDialogBox("PVS does not run on Windows", constants.WARNING)
        mainFrame.restoreOpenFiles()
        return 1

# end of class PVSEditorApp

def processArguments(args):
    logging.info("Command Line Arguments: %s", args)
    del args[0]
    for arg in args:
        if arg.startswith(constants.INPUT_LOGGER):
            logLevel = arg[len(constants.INPUT_LOGGER):]
            if logLevel == constants.LOG_LEVEL_DEBUG:
                constants.LOGGER_LEVEL = logging.DEBUG
            elif logLevel == constants.LOG_LEVEL_DEBUG:
                constants.LOGGER_LEVEL = logging.FATAL
            
def processConfigFile(applicationFolder):
    configFile = os.path.join(applicationFolder, "src/pvside.cfg")
    cfg = PVSIDEConfiguration()
    cfg.initialize(applicationFolder)

def configLogger(applicationFolder):
    """Return a logger for the given name"""
    logConfigFile = os.path.join(applicationFolder, "src/logging.cfg")
    if os.path.exists(logConfigFile):
        logging.config.fileConfig(logConfigFile)
    else:
        print "Could not find the config file for logging. Using default settings..."
        hdlr = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(module)s %(funcName)s] %(levelname)s - %(message)s")
        hdlr.setFormatter(formatter)
        logging.addHandler(hdlr) 
        logging.setLevel(logging.DEBUG)

if __name__ == "__main__":
    #logging.debug("PubSub version is %s", pub.PUBSUB_VERSION)
    assert pub.PUBSUB_VERSION == 3
    utilDirectory = os.path.dirname(util.__file__)
    applicationFolder = os.path.abspath(os.path.join(utilDirectory, os.path.pardir))
    configLogger(applicationFolder)
    processConfigFile(applicationFolder)
    logging.debug("Application Folder is %s", applicationFolder)
    processArguments(list(sys.argv))
    gc.enable()
    gc.set_threshold(1, 2, 3)
    application = PVSEditorApp(0)
    logging.info("Entering MainLoop...")
    #pvscomm.PVSCommandManager().ping()
    
    application.MainLoop()
