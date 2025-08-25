import unittest

import td


class IntegrationTestMain12(unittest.TestCase):
    # scenario integration test n°12

    # Description : The user enable tempButton
    # Precondition : The artwork is running and tempButton value is set to 0.
    # Steps : 1) The user presses the key '+' on the keyboard.
    # Output : The tempButton should be 1

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

     #keyboard +
    def test_keyboard_plus(self):
        temp_button = td.op("/container31/project1/tempButton")
        temp_button.par.value0 = 0

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'+','+',
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, True,
                                                                           0, False,
                                                                           False, False)

        self.assertEqual(temp_button.par.value0, 1)

if __name__ == "__main__":
    unittest.main()