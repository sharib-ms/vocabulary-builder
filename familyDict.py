import wx
import os
import random
import  cStringIO
import pygame

class WordFrame(wx.Frame):
   
    def __init__(self, parent, title, Rus, Fin, Nep, Eng):
        wx.Frame.__init__(self, parent, title=title, size=(460, 500))
        panel=wx.Panel(self)
     # variable to count words
        self.count=0
        self.vacabRus=Rus.load_dict()
        self.vacabFin=Fin.load_dict()
        self.vacabNep=Nep.load_dict()
        self.vacabEng=Eng.load_dict()


#        panel = wx.Panel(self)
#        self.quote = wx.StaticText(panel, label=label, pos=(50, 30))

 # # # # # # # setting a menu
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

# # # # #  images 
        
        # bitmap upper left corner is in the position tuple (x, y) = (5, 5)
        wx.StaticBitmap(panel, -1, Rus.load_img(), pos=(20, 35))
        wx.StaticBitmap(panel, -1, Fin.load_img(), pos=(20, 107))
        wx.StaticBitmap(panel, -1, Nep.load_img(), pos=(20, 175))
        wx.StaticBitmap(panel, -1, Eng.load_img(), pos=(20, 250))



# # # # # create a button
        # A button
        self.buttonRus =wx.Button(panel, label=self.vacabRus[self.count], size=(360,50), pos=(80,30))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.buttonRus)

        self.buttonFin =wx.Button(panel, label=self.vacabFin[self.count], size=(360,50), pos=(80,100))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.buttonFin)

        self.buttonNep =wx.Button(panel, label=self.vacabNep[self.count], size=(360,50), pos=(80,170))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.buttonNep)

        self.buttonEng =wx.Button(panel, label=self.vacabEng[self.count], size=(360,50), pos=(80,240))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.buttonEng)

#        self.buttonDone =wx.Button(panel, label="EMPTY", size=(150,90), pos=(20,350))
#        self.Bind(wx.EVT_BUTTON, self.OnClickDone,self.buttonDone)

        self.buttonNext =wx.Button(panel, label="NEXT", size=(200,90), pos=(130,350))
        self.Bind(wx.EVT_BUTTON, self.OnClickNext,self.buttonNext)


#        self.button =wx.Button(self, label="NEXT")
#        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)


 # # # # # # show the window
        self.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "An application to learn foreign language words.", "About the program", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnClickNext(self,e):
#        self.count+=1
#        if self.count>=len(self.vacab):
#            self.count=0
        self.count=random.randrange(0, len(self.vacabRus)-1, 1)

        self.buttonRus.SetLabel(self.vacabRus[self.count])
        self.buttonFin.SetLabel(self.vacabFin[self.count])
        self.buttonNep.SetLabel(self.vacabNep[self.count])
        self.buttonEng.SetLabel(self.vacabEng[self.count])

    def OnClick(self,e, v):
      
        pygame.mixer.init()
        wav_name="/sound/"+v+str(self.count)+".wav"
        pygame.mixer.music.load(wav_name)
        pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy() == True:
            #continue 


        pass

    def OnClickDone(self,e):
        pass


 
class WordDictionary():
    def __init__(self, name):
        self.dict=[]
        self.dictName='vacab/vacab'+name+'.txt'
        self.flagName='img/flag'+name+'.jpg'

    def load_dict(self):
        txt=open(self.dictName)
        self.dict=txt.read().splitlines()
        return self.dict
    def load_img(self):
            
        try:
        # actually you can load .jpg  .png  .bmp  or .gif files
            flag = wx.Image(self.flagName, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        except IOError:
            print "Image file %s not found" % imageFile
            raise SystemExit
        return flag
 
app = wx.App(False)

# DICTIONARIES
wdRus=WordDictionary('Rus')
wdRus.load_dict()

wdFin=WordDictionary('Fin')
wdFin.load_dict()

wdNep=WordDictionary('Nep')
wdNep.load_dict()

wdEng=WordDictionary('Eng')
wdEng.load_dict()

window_1=WordFrame(None, "LEARNING WORDS", wdRus , wdFin, wdNep, wdEng)
app.MainLoop()
