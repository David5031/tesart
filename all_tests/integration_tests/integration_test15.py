from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class IntegrationTestMain15(unittest.TestCase):
    # scenario integration test n°15
    
    # Description : The user changes song to song 5
    # Precondition : The artwork is running and next song is set to 5. The next true song is set to 2. audiofilein1B volume is set to 1 and constantBlackSpeed is 1.
    # Steps : 1) The user presses button2
    # Output : The next song should be 2 and next true song should be 3. constantBlackSpeed value should be 1. audiofilein1 volume should be 0.5 and it should be executed like audiofilein1B


    # tests for component presence
    
    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_change_song_button.tox'
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


    
    
    # test sur le bouton pour changer la musique par la musique numéro 5
    
    def test_change_musique_button_num_5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 5

       

        audiofilein1B = td.op("/container31/project1/audiofilein1B")
        audiofilein1B.par.volume = 1

        audiofilein1 = td.op("/container31/project1/audiofilein1")
        

        constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        constantBlackSpeed.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 2
        

        #td.op("/container31/project1/button2").click( force = True) # it does not work
        #button2_component.par.value0=1
        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)
        print(prochain.par.value0)

        self.assertEqual(audiofilein1B.par.volume, 0.5) 
        self.assertEqual(audiofilein1.par.play, 1)
        self.assertEqual(audiofilein1B.par.play, 1)
        self.assertEqual(constantBlackSpeed.par.value0, 1)

        self.assertEqual(prochain.par.value0, 2)
        self.assertEqual(vraiProchain.par.value0, 3)

      
if __name__ == "__main__":
    unittest.main()