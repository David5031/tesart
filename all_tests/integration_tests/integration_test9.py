from asyncio import run
import random
import string
import unittest
#import coverage
from unittest.mock import MagicMock

import td
import time
#import HtmlTestRunner


class IntegrationTestMain9(unittest.TestCase):
    # scenario integration test n°9
    
    # Description : The user choose song 8
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '8' on the keyboard. 
    # Output : The next song should be song 8
     
    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_keyboard.tox'

        
        if(td.op("/container31") == None):
            cls.base_path.loadTox(cls.tox_path)
            print("tox loaded")
        else :
            print("tox already loaded")

        cls.container = td.op(cls.base_path)
    
    # for unload tox file
    @classmethod
    def tearDownClass(cls):
        tox_load = td.op("/container31")
        tox_load.destroy()
        print("tox unloaded")
    

    """
    def setUp(self):
        # Sauvegarder les paramètres avant chaque test
        self.test_params = TestMain.save_all_parameters(self.container)

    def tearDown(self):
        # Restaurer les paramètres après chaque test
        TestMain.restore_all_parameters(self.container, self.test_params)
    """

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

    #test songs choices with keyboards
 
        
    
         
    #keyboard 8
    def test_keyboard_8(self):
        

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'8','8', False, False, False, False, False, False,False, False, False, True, 0, False, False, False)
        
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vraiProchain = td.op("/container31/project1/vraiProchain").par.value0

        self.assertEqual(prochain, 8 )
        
    
    
   
if __name__ == "__main__":
    unittest.main()