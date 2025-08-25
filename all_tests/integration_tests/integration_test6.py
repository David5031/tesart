import unittest

import td


class IntegrationTestMain6(unittest.TestCase):
    # scenario integration test n°6

    # Description : The user choose song 5
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '5' on the keyboard.
    # Output : The next song should be song 5

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

    #keyboard 5
    def test_keyboard_5(self):


        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'5',
                                                                           '5', False,
                                                                           False, False,
                                                                           False, False,
                                                                           False,False,
                                                                           False, False,
                                                                           True, 0,
                                                                           False, False,
                                                                           False)

        prochain = td.op("/container31/project1/prochain").par.value0
        td.op("/container31/project1/vraiProchain").par.value0

        self.assertEqual(prochain, 5 )



if __name__ == "__main__":
    unittest.main()