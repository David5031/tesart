from asyncio import run
import random
import string
import unittest

import td
import time

class SystemTestMain17(unittest.TestCase):
    """system test : scenario 17."""
   
    # scenario system test n°17  
    # Description : test of display timer
    # Precondition : The artworks is running with the default timer values
    # Steps : 1) Simulate value change by value 1, 5 and 10
    # Output : the Cycle number should be reset to 0 , the display timer should be 31 sec (101 sec and then 14 sec) and triggered. The display number should be 1 (0 and then 1)


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
        # Initialize the operators
        self.numeroCycle = td.op('/container31/project1/numeroCycle')
        self.timerAffichage = td.op('/container31/project1/timerAffichage')
        self.numeroAffichage = td.op('/container31/project1/numeroAffichage')

        # Initialize values
        self.timers1 = [30.0, 18.5, 33.0, 35.5, 100.0, 8.0, 13.0, 14.0, 14.4, 13.0]

    def tearDown(self):
        # Reset the operators' parameters to their default state
        self.numeroCycle.par.value0 = 0
        self.timerAffichage.par.length = 0
        self.numeroAffichage.par.value0 = 0

    def test_onValueChange(self):
        # Test the onValueChange function with different values
        test_values = [1, 5, 10]
        
        for val in test_values:
            # Simulate the value change
            td.mod(td.op("/container31/project1/chopexec1")).onValueChange(None, None, val, None)
            
            # Check if numeroCycle is reset to 0
            self.assertEqual(self.numeroCycle.par.value0, 0)
            
            # Check if timerAffichage length is correctly set
            new_length = self.timers1[val - 1] + 1
            self.assertEqual(self.timerAffichage.par.length, new_length)
            
            # Check if timerAffichage start pulse is triggered
            self.assertTrue(self.timerAffichage.par.start.pulse, 1) 
            
            # Check if numeroAffichage is correctly set
            new_numeroAffichage = 0 if val == 5 else 1
            self.assertEqual(self.numeroAffichage.par.value0,  new_numeroAffichage)

    
    
if __name__ == "__main__":
    unittest.main()