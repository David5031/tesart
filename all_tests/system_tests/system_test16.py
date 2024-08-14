from asyncio import run
import random
import string
import unittest

import td
import time

class SystemTestMain16(unittest.TestCase):
    """system test : scenario 16."""
   
    # scenario system test n°16
    
    # Description : The user presses an invalid key and runs it
    # Precondition : The artwork is running with next song: n°1 and the next real song: n°2
    # Steps : 1) The user presses the key '/' on the keyboard. 2) The user presses the key '-' on the keyboard.
    # Output : The song 1 should be played, the next song should be song 5 and the next real song should be song 2


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

    
    def test_invalid_key_pressed(self):


        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 2

        tempButtonB = td.op("/container31/project1/tempButtonB")
        tempButtonB.par.value0 = 0 

        
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'/','/', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)  # change prochain value
    
        self.assertEqual(prochain.par.value0, 5 )
        self.assertEqual(vraiProchain.par.value0,2)
        self.assertEqual(tempButtonB.par.value0, 1)

    
    
if __name__ == "__main__":
    unittest.main()