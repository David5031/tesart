import unittest

import td


class IntegrationTestMain8(unittest.TestCase):
    # scenario integration test n°8

    # Description : The user choose song 7
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '7' on the keyboard.
    # Output : The next song should be song 7

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

    #keyboard 7
    def test_keyboard_7(self):

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'7',
                                                                           '7', False,
                                                                           False, False,
                                                                           False, False,
                                                                            False,False,
                                                                            False, False,
                                                                            True, 0,
                                                                            False, False,
                                                                            False)

        prochain = td.op("/container31/project1/prochain").par.value0
        td.op("/container31/project1/vraiProchain").par.value0
        self.assertEqual(prochain, 7 )

if __name__ == "__main__":
    unittest.main()