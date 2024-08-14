from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time

class SystemTestMain14(unittest.TestCase):
    """system test : scenario 14."""
   
    
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
    
    
    """ pour trouver le container31
    def success_load(self):
        project_load = td.op("/").findChildren(name = "container31*", maxDepth = 1)
        for component in project_load:
            self.assertEqual(component.name, 'container31')
    """

   
    # scenario system test n°14
    
    # Description : The user runs silence music
    # Precondition : The artwork is running with next song: n°1 and the next real song: n°1 with applause music loaded and constant black speed = 1
    # Steps : 1) The user presses on "button1__". 
    # Output : The silence music should be played, the next song should be song 5 and the next real song should be song 2
   
    
    def test_silence(self):
        #arrange

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        audio_filein2.par.file = "audio/transition-applaudissements.wav"

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1
        print("value prochain pour silence normalement (1)" , prochain.par.value0)

        constant_black_speed = td.op("/container31/project1/constantBlackSpeed")
        constant_black_speed.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 2
       
        
        #act
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        print("clique d'abord pour le silence")

      

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0) # chopexec4 is executed

        #assert
        self.assertEqual(audio_filein2.par.file, "audio/silence5sec.wav") 
        self.assertEqual(constant_black_speed.par.value0, -1.0)

        self.assertEqual(prochain.par.value0, 5) #1 if chopexec4 is not executed
        self.assertEqual(vraiProchain.par.value0, 2) 
    
    
if __name__ == "__main__":
    unittest.main()
        
