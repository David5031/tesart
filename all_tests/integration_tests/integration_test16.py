from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class TestMain(unittest.TestCase):
    # scenario integration test n°15
    
    # Description : The user changes song to song 1 
    # Precondition : The artwork is running and next song is set to 1. The next true song is set to 1. audiofilein1B volume is set to 1 and constantBlackSpeed is 1.
    # Steps : 1) The user presses button2
    # Output : The song 1 should be executed. The next song should be 5. audiofilein1B volume should be 1. The timerLoad should be started


    # tests for component presence
    
    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_change_music_button.tox'
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


    # test sur le bouton pour changer la musique par une musique différent de 5
    
    def test_change_musique_button_num_diff_5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        audiofilein1B = td.op("/container31/project1/audiofilein1B")


        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1

        timerLoad = td.op("/container31/project1/timerLoad")

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)


        self.assertEqual(audiofilein1B.par.volume, 1)
      
  
        #self.assertTrue(timerLoad.par.start.pulse(), 1) à vérifier


        self.assertEqual(prochain.par.value0, 5)
     

if __name__ == "__main__":
    unittest.main()