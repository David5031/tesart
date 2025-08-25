import unittest

import td


class IntegrationTestMain11(unittest.TestCase):
    # scenario integration test n°11

    # Description : The user runs a loaded song
    # Precondition : The artwork is running and tempButtonB value is set to 0.
    # Steps : 1) The user presses the key '-' on the keyboard.
    # Output : The tempButtonB should be 1

    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_keyboard.tox'


        if(td.op("/container31") is None):
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


    #test songs choices with keyboards

     #keyboard -
    def test_keyboard_minus(self):

        temp_button_b = td.op("/container31/project1/tempButtonB")
        #print("(valeur de prochain)", prochain)
        print("la val de tempBUTTON avant: " + str(temp_button_b.par.value0))
        temp_button_b.par.value0 = 0

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-',
                                                                           '-', False,
                                                                           False, False,
                                                                           False, False,
                                                                           False,False,
                                                                           False, False,
                                                                           True, 0,
                                                                           False, False,
                                                                           False)

        self.assertEqual(temp_button_b.par.value0, 1)

if __name__ == "__main__":
    unittest.main()