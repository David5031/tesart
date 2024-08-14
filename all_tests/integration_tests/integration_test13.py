from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class IntegrationTestMain13(unittest.TestCase):
    # scenario integration test n°13
    
    # Description : The user runs applause music
    # Precondition : The artwork is running and next song is set to 5.
    # Steps : 1) The user presses button1__
    # Output : The audio_filein2 should be executed and loaded with 'transition-applaudissements.wav' and constantBlackSpeed value should be -1
     


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

   
     # test sur les boutons pour les applaudissements 
 

    def test_applause_button_1(self):
        button1_component = td.op("/container31/project1/button1__")
        #print(button1_component.type)
        #self.assertEqual(button1_component.type, "button")

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        
        
        prochain = td.op("/container31/project1/prochain")
     
        prochain.par.value0 = 5
      
        self.assertEqual(5, prochain.par.value0)
       

        
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        #button1_component.par.value0 = 1 
        time.sleep(5)
        #print("clique ensuite pour l'applaudissement")
        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
     
        self.assertEqual(audio_filein2.par.file, "audio/transition-applaudissements.wav") 
        #self.assertTrue(audio_filein2.par.cue.pulse())
        self.assertEqual(audio_filein2.par.play, 1)
        self.assertEqual(constantBlackSpeed.par.value0, -1.0) 
     
if __name__ == "__main__":
    unittest.main()
        
 