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

class IntegrationTestMain14(unittest.TestCase):
    # scenario integration test n°14
    
    # Description : The user runs silence music
    # Precondition : The artwork is running and next song is set to 1 and audiofilein_2 is set to "audio/transition-applaudissements.wav" .
    # Steps : 1) The user presses button1__
    # Output : The audio_filein2 should be executed and loaded with 'silence5sec.wav' and constantBlackSpeed value should be -1


    # tests for component presence
    
    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_applause_button.tox'
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

    # tester les boutons pour le silence
    
    def test_silence_button_1(self):

        #arrange
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        audio_filein2.par.file = "audio/transition-applaudissements.wav"

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1
        print("value prochain pour silence normalement (1)" , prochain.par.value0)

        constant_black_speed = td.op("/container31/project1/constantBlackSpeed")
        
        #act
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
    
        #print(button1_component.par.value0)

        #time.sleep(5)

   
        
        #assert
        print(audio_filein2.par.file)
        self.assertEqual(audio_filein2.par.file, "audio/silence5sec.wav") 
        #self.assertTrue(audio_filein2.par.cue.pulse())
        self.assertEqual(audio_filein2.par.play, 1)   #run music
        self.assertEqual(constant_black_speed.par.value0, -1.0)  #fail quand la musique tourne en continue
        
        #button1_component.par.value0 = 0
    
    
    
   
    
    
     
if __name__ == "__main__":
    unittest.main()
        
 