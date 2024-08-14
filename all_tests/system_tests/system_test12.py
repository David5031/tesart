from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class SystemTestMain12(unittest.TestCase):
    """system test : scenario 12."""
   
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

   
    # scenario system test n°12
    
    # Description : The user changes song for another song (1) different from song 5 and runs it
    # Precondition : The artwork is running with next song: n°1 and the next real song: n°1
    # Steps : 1) The user presses on "button2". 
    # Output : The song 1 should be played, the next song should be song 5 and the next real song should be song 1
   
    
    def test_change_song_diff5(self):
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
        self.assertEqual(vraiProchain.par.value0, 1)
        self.assertEqual(prochain.par.value0, 5)
    
    
if __name__ == "__main__":
    unittest.main()
        
