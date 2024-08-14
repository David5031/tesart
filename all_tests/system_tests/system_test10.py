from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time


class SystemTestMain10(unittest.TestCase):
    """system test : scenario 10."""
   
    
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
    
    
    """ to find container31
    def success_load(self):
        project_load = td.op("/").findChildren(name = "container31*", maxDepth = 1)
        for component in project_load:
            self.assertEqual(component.name, 'container31')
    """

   
    # scenario system test n°10
    
    # Description : The user chooses song 9 and runs it
    # Precondition : The artwork is running with next song: n°1 and the next real song: n°2
    # Steps : 1) The user presses the key '9' on the keyboard. 2) The user presses the key '-' on the keyboard.
    # Output : The song 9 should be played, the next song should be song 5 and the next real song should be song 2
   
    
    def test_song_9(self):

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 2

        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0


        td.op('/container31/project1/prochain').par.value0 = 5

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'9','9', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)  # change prochain value

      
        
        print("normalement prochain est 5")
        print(td.op('/container31/project1/prochain').par.value0)


        self.assertEqual(prochain.par.value0, 5 )
        self.assertEqual(vraiProchain.par.value0,2)
        self.assertEqual(tempButtonB.par.value0, 1)
    
    
if __name__ == "__main__":
    unittest.main()
        
