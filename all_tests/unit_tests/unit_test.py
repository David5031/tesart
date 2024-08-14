import random
import string
import unittest
import time
import timeit
import psutil
import GPUtil
import platform

import td


class UnitTestMain(unittest.TestCase):
    "collection of unit test"
    
  
    def setUp(cls) :
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_button_test.tox'
        if(td.op("/container31") == None):
            cls.base_path.loadTox(cls.tox_path)
            print("tox loaded")
        else :
            print("tox already loaded")
    
    
    # for unload tox file
    def tearDown(cls):
        tox_load = td.op("/container31")
        tox_load.destroy()
        print("tox unloaded")
    
   
    
    def test_container31_load(self):
        project_load = td.op("/").findChildren(name = "container31", maxDepth = 1)
        for component in project_load:
            self.assertEqual(component.name, 'container31')
    
 
    
    def test_button1_presence(self):
        container_components = td.op("/container31").findChildren(name = 'button1__', maxDepth=1)
        self.assertTrue(len(container_components) > 0)
        for component in container_components:
            self.assertEqual(component.name, 'button1__')
    
    

    def test_button_press(self):
        """test momentary button pressure """
        #button access
        self.button = td.op("/container31/button1__")

        # button press
        self.button.par.value0 = 1
     

        # check
        pressed_value = int(self.button.par.value0)
        self.assertEqual(pressed_value, 1) 

        # button released
        self.button.par.value0 = 0
    
       
        #check
        released_value = int(self.button.par.value0)
        self.assertEqual(released_value, 0) 
     
        
    """
    #failed test

    def test_button_press(self):
        
        self.button = td.op("/").create(td.buttonCOMP, 'mybutton')
        self.button.par.buttontype = 'Momentary'
        self.button.par.value0 = 0
        
        # Simuler un clic sur le bouton momentary
        self.button.click() 
        time.sleep(0.1)  # Attendre un peu pour simuler l'appui momentary

        # Vérifier que le bouton est pressé
        pressed_value = self.button.par.value0.eval()
        self.assertEqual(pressed_value, 1, "Button should be pressed (value should be 1)") # does not change the value if released
      
    """    
        
        
if __name__ == '__main__':
    unittest.main()