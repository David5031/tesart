from asyncio import run
import random
import string
import unittest
#import coverage
from unittest.mock import MagicMock

import td
import time
#import HtmlTestRunner

#cov = coverage.Coverage()
#cov.start()
#print("il devrait être couvert")

class SystemTestMain(unittest.TestCase):
    """system test : scenario 1."""

    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame.tox'
        if(td.op("/container31") == None):
            cls.base_path.loadTox(cls.tox_path)
            print("tox loaded")
        else :
            print("tox already loaded")

    
    
    # for unload tox file
    @classmethod
    def tearDownClass(cls):
        tox_load = td.op("/container31")
        tox_load.destroy()
        print("tox unloaded")
    
    
    """
    @classmethod
    def setUp(cls):
        cls.reset_parameters()
    
    @classmethod
    def tearDown(cls):
        cls.reset_parameters()
    
    def reset_parameters():
        td.op("/container31/project1/tempButtonB").par.value0 = 0 
        button1_component = td.op("/container31/project1/button1__") # ?
    
        
        td.op("/container31/project1/audiofilein2").par.file = "audio/silence5sec.wav"
        td.op("/container31/project1/prochain").par.value0 = 5
       
        
        td.op("/container31/project1/constantBlackSpeed").par.value0 = 1

        

     
        

        

    
        
        
    """
    
    """ pour trouver le container31
    def success_load(self):
        project_load = td.op("/").findChildren(name = "container31*", maxDepth = 1)
        for component in project_load:
            self.assertEqual(component.name, 'container31')
    """

    """
     # test sur les boutons pour les applaudissements 
    
    def applause_button_1(self):
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        #self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        
        
        prochain = td.op("/container31/project1/prochain")
        #print("valeur de prochain par defaut", prochain.par.value0) 
        prochain.par.value0 = 5
        #print("value prochain pour applause normalement (5)" , prochain.par.value0)
        self.assertEqual(5, prochain.par.value0)
       

        
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        #button1_component.par.value0 = 1 
        
       
        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        print(constantBlackSpeed.par.value0)
     
        self.assertEqual(audio_filein2.par.file, "audio/transition-applaudissements.wav") 
        #self.assertTrue(audio_filein2.par.cue.pulse())
        self.assertEqual(audio_filein2.par.play, 1)
        self.assertEqual(constantBlackSpeed.par.value0, -1.0) 
    
   
    # tester les boutons pour le silence
    
    def silence_button_1(self):

        #arrange
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1
        print("value prochain pour silence normalement (1)" , prochain.par.value0)

        constant_black_speed = td.op("/container31/project1/constantBlackSpeed")
        
        #act
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        print("clique d'abord pour le silence")

        audio_filein2.par.file = "audio/silence5sec.wav"
        #assert
        self.assertEqual(audio_filein2.par.file, "audio/silence5sec.wav") 
        self.assertEqual(constant_black_speed.par.value0, -1.0)
        
    
    
    
   
    

    # test sur le bouton pour changer la musique par la musique numéro 5
  
    def change_musique_button_num_5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 5

        button2_component = td.op("/container31/project1/button2")

        audiofilein1B = td.op("/container31/project1/audiofilein1B")
        audiofilein1B.par.volume = 1

        audiofilein1 = td.op("/container31/project1/audiofilein1")
        

        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        constantBlackSpeed.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1
        

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)


        #self.assertEqual(audiofilein1B.par.volume, 0.5) # prob avec le volume
        #self.assertEqual(audiofilein1.par.play, 1)
        #self.assertEqual(audiofilein1B.par.play, 1)
        #self.assertEqual(constantBlackSpeed.par.value0, 1.0)

        #self.assertEqual(prochain.par.value0, 2)
        #self.assertEqual(vraiProchain.par.value0, 2)

    
    
    

    
    # test sur le bouton pour changer la musique par une musique différent de 5
    
    def change_musique_button_num_diff_5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        button2_component = td.op("/container31/project1/button2")

        audiofilein1B = td.op("/container31/project1/audiofilein1B")

        audiofilein1 = td.op("/container31/project1/audiofilein1")

        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1
        

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)


        #self.assertEqual(audiofilein1B.par.volume, 0.5)
        #self.assertEqual(audiofilein1.par.play, 1)
        #self.assertEqual(prochain.par.value0, 5)
      
    

    




    #test musics choices with keyboards
 
    #keyboard 0
    def keyboard_0(self):
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'0','0', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        #self.assertEqual(prochain, 10 )
       
    
    #keyboard 1
    def keyboard_1(self):

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'1','1', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 1 )
        #self.assertEqual(vraiProchain,2)
    
    #keyboard 2
    def keyboard_2(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'2','2', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 2 )
        #self.assertEqual(vraiProchain,3)
    
    #keyboard 3
    def keyboard_3(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'3','3', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 3 )
        #self.assertEqual(vraiProchain,4)

    #keyboard 4
    def keyboard_4(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'4','4', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 4 )
        #self.assertEqual(vraiProchain,1)
    
    #keyboard 5
    def keyboard_5(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'5','5', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 5 )
       
    #keyboard 6
    def keyboard_6(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'6','6', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 6 )
        

    #keyboard 7
    def keyboard_7(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'7','7', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 7 )
        
    #keyboard 8
    def keyboard_8(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'8','8', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 8 )
        
    #keyboard 9
    def keyboard_9(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'9','9', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        #self.assertEqual(prochain, 9 )
     
  
    #keyboard -
    def keyboard_minus(self):
        
        tempButtonB = td.op("/container31/project1/tempButtonB")
        #print("(valeur de prochain)", prochain)
        print("la val de tempBUTTON avant: " + str(tempButtonB.par.value0))
        tempButtonB.par.value0 = 0 
    
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
       
        #self.assertEqual(tempButtonB.par.value0, 1) 
    
    #keyboard +
    def keyboard_plus(self):
        
        tempButton = td.op("/container31/project1/tempButton")
        #print("(valeur de prochain)", prochain)
        tempButton.par.value0 = 0
    
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'+','+', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
       
        #self.assertEqual(tempButton.par.value0, 1)
    """
    # scenario system test number 1
    
    # Description : The user chooses song 10 and runs it
    # Precondition : The artwork is running with next song: number 1 and the next real song: number 2
    # Steps : 1) The user presses the key '0' on the keyboard. 2) The user presses the key '-' on the keyboard.
    # Output : The song 10 should be played, the next song should be song 5 and the next real song should be song 2
   
    def test_song_0(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 2


        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 


        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'0','0', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)  # change prochain value
       
        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 5 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,2)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1) 
    
    """
    def test_music_1(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'1','1', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 1 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,2)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1) 

    def test_music_2(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'2','2', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 2 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,3)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)

    def test_music_3(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'3','3', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 3 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,4)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_music_4(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'4','4', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 4 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0, 1)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_music_5(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'5','5', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 5 )
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_music_6(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'6','6', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 6 )
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_music_7(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 
        
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'7','7', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 7 )
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_music_8(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 
        
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'8','8', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 8 )
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)

    def test_music_9(self):
        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'9','9', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 9 )
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)
    
    def test_change_music_for5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 5

        button2_component = td.op("/container31/project1/button2")

        audiofilein1B = td.op("/container31/project1/audiofilein1B")
        audiofilein1B.par.volume = 1

        audiofilein1 = td.op("/container31/project1/audiofilein1")
        

        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        constantBlackSpeed.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1
        

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)


        self.assertEqual(audiofilein1B.par.volume, 0.5)
        self.assertEqual(audiofilein1.par.play, 1)
        self.assertEqual(audiofilein1B.par.play, 1)
        self.assertEqual(constantBlackSpeed.par.value0, 1.0)

        self.assertEqual(prochain.par.value0, 1)
        self.assertEqual(vraiProchain.par.value0, 2)

        

    def test_change_music_diff5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        button2_component = td.op("/container31/project1/button2")

        audiofilein1B = td.op("/container31/project1/audiofilein1B")

        audiofilein1 = td.op("/container31/project1/audiofilein1")

        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1
        

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)


        self.assertEqual(audiofilein1B.par.volume, 1)
        #self.assertEqual(audiofilein1.par.play, 1)
        self.assertEqual(prochain.par.value0, 5)
 
    def test_applause(self): 
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        #self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        
        
        prochain = td.op("/container31/project1/prochain")
        #print("valeur de prochain par defaut", prochain.par.value0) 
        prochain.par.value0 = 5
        #print("value prochain pour applause normalement (5)" , prochain.par.value0)
        self.assertEqual(5, prochain.par.value0)
       

        
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        #button1_component.par.value0 = 1 
        
       
        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        print(constantBlackSpeed.par.value0)
     
        self.assertEqual(audio_filein2.par.file, "audio/transition-applaudissements.wav") 
        #self.assertTrue(audio_filein2.par.cue.pulse())
        self.assertEqual(audio_filein2.par.play, 1)
        self.assertEqual(constantBlackSpeed.par.value0, -1.0) 

    def test_silence(self):
        #arrange
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1
        print("value prochain pour silence normalement (1)" , prochain.par.value0)

        constant_black_speed = td.op("/container31/project1/constantBlackSpeed")
        
        #act
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        print("clique d'abord pour le silence")

        audio_filein2.par.file = "audio/silence5sec.wav"
        #assert
        self.assertEqual(audio_filein2.par.file, "audio/silence5sec.wav") 
        self.assertEqual(constant_black_speed.par.value0, -1.0)

    """
   
    #tests suite 

    #def tests_suite(self):
    #    testSuite = unittest.TestSuite()

    #    testSuite.addTest(TestMain("test_music_0"))
    #    testSuite.addTest(TestMain("test_music_1"))
    #    testSuite.addTest(TestMain("test_music_2"))
    #    testSuite.addTest(TestMain("test_music_4"))
    #    testSuite.addTest(TestMain("test_music_5"))
    #    testSuite.addTest(TestMain("test_music_6"))
    #    testSuite.addTest(TestMain("test_music_7"))
    #    testSuite.addTest(TestMain("test_music_8"))
    #    testSuite.addTest(TestMain("test_music_9"))

    #    return testSuite


    
if __name__ == "__main__":
    unittest.main()
        
