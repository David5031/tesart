from asyncio import run
import random
import string
import unittest

import td
import time

class SystemTestMain18(unittest.TestCase):
    """system test : scenario 18."""
   
    # scenario system test n°18  
    
    # Description : test onCycle event
    # Precondition : The artwork is running with the default timer values (song number to 1). Song number value  = 1 and cycle number value = 0
    # Steps :Simulate onCycle event
    # Output : The display number should be 2, the cycle number should be 1 and the diplay timer should be 18.9 seconds


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
        self.numeroChanson = td.op('/container31/project1/numeroChanson')
        self.numeroCycle = td.op('/container31/project1/numeroCycle')
        self.numeroAffichage = td.op('/container31/project1/numeroAffichage')
        self.timerAffichage = td.op('/container31/project1/timerAffichage')
        
        # Set initial values
        self.numeroChanson.par.value0 = 1
        self.numeroCycle.par.value0 = 0
        self.numeroAffichage.par.value0 = 0
        self.timerAffichage.par.length = 0

    def tearDown(self):
        # Reset the operators' parameters to their default state
        self.numeroChanson.par.value0 = 0
        self.numeroCycle.par.value0 = 0
        self.numeroAffichage.par.value0 = 0
        self.timerAffichage.par.length = 0

    def test_onCycle(self):
        timers1 = [30.0, 18.5, 33.0, 35.5, 100.0, 8.0, 13.0, 14.0, 14.4, 13.0] 
        timers2 = [48.9, 43.2, 55.7, 58.4, 200.0, 16.0, 26.0, 28.0, 28.8, 26.0]
        timers3 = [68.5, 60.0, 300.0, 77.5, 300.0, 24.0, 39.0, 42.0, 43.2, 39.0]
        timers4 = [77.7, 400.0, 400.0, 400.0, 400.0, 32.0, 52.0, 56.0, 47.6,52.0]


        # Set test values
        self.numeroChanson.par.value0 = 1
        self.numeroCycle.par.value0 = 0

     
        td.mod(td.op("/container31/project1/timer1_callbacks")).onCycle(None, None, None)

        # Check the expected results
      
        self.assertEqual(self.numeroAffichage.par.value0, 2)
        self.assertEqual(self.numeroCycle.par.value0, 1)
        self.assertEqual(self.timerAffichage.par.length, 18.9)

    
    
if __name__ == "__main__":
    unittest.main()