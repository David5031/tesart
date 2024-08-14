from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class SystemTestMain13(unittest.TestCase):
    """system test : scenario 13."""
   
    
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

   
    # scenario system test n°13
    
    # Description : The user runs applause music
    # Precondition : The artwork is running with next song: n°5 and the next real song: n°1 with silence music loaded and constant black speed = 1
    # Steps : 1) The user presses on "button1__". 
    # Output : The applause music should be played, the next song should be song 1 and the next real song should be song 2
   
    
    def test_applause(self): 
      

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")
        
        
        prochain = td.op("/container31/project1/prochain")
        #print("valeur de prochain par defaut", prochain.par.value0) 
        prochain.par.value0 = 5
        #print("value prochain pour applause normalement (5)" , prochain.par.value0)
        self.assertEqual(5, prochain.par.value0)

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1

        
        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        constantBlackSpeed.par.value0 = 1
       

        
        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0) # chopexec4 is executed

       
     
        self.assertEqual(audio_filein2.par.file, "audio/transition-applaudissements.wav") 
        self.assertEqual(constantBlackSpeed.par.value0, 1.0)  # -1 first
        #self.assertTrue(audio_filein2.par.cue.pulse())
        self.assertEqual(audio_filein2.par.play, 1)
       

        self.assertEqual(prochain.par.value0, 1) # 5 if chopexec4 is not executed
        self.assertEqual(vraiProchain.par.value0, 2) 
    
    
if __name__ == "__main__":
    unittest.main()
        
