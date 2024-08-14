from asyncio import run
import random
import string
import unittest
from unittest.mock import MagicMock

import td
import time

class SystemTestMain15(unittest.TestCase):
    """system test : scenario 15."""
    
    # scenario system test n°15
    
    # Description : The timer sets the right parameters values when in onCycle event is triggered
    # Precondition : The artwork is running with timer, audiofilein1, audiofilein1b and constantBlackSpeedinitialized to True or 0
    # Steps : 1) The on Cycle event is triggered.
    # Output : The audiofilein1, audiofilein1b and constantBlackSpeed should be rated at 1.
   
    
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

    
    def setUp(self):
        self.timer_op = td.op("/container31/project1/timerLoad")
        self.audiofilein1 = td.op("/container31/project1/audiofilein1")
        self.audiofilein1B = td.op("/container31/project1/audiofilein1B")
        self.constantBlackSpeed = td.op("/container31/project1/constantBlackSpeed")
        
        # reset operator values
        self.timer_op.par.initialize = True
        self.audiofilein1.par.play = 0
        self.audiofilein1B.par.play = 0
        self.constantBlackSpeed.par.value0 = 0

    def tearDown(self):
        # reset states 
        self.timer_op.par.initialize = True
        self.audiofilein1.par.play = 0
        self.audiofilein1B.par.play = 0
        self.constantBlackSpeed.par.value0 = 0

    def test_onCycle(self):
        # simulate onCycle event
        td.mod(td.op("/container31/project1/timer2_callbacks")).onCycle(self.timer_op, None, None)
        
      
        self.assertEqual(self.audiofilein1.par.play, 1)
        self.assertEqual(self.audiofilein1B.par.play, 1)
        self.assertEqual(self.constantBlackSpeed.par.value0, 1)
    
    
if __name__ == "__main__":
    unittest.main()
        
