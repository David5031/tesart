import unittest

import td


class IntegrationTestMain(unittest.TestCase):
    """Collection of integration tests ."""
    # scenario integration test number 1

    # Description : The user choose song 10
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '0' on the keyboard.
    # Output : The next song should song 10

    # integrations tests

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

    #keyboard 0
    def test_keyboard_0(self):
        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'0','0',
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, True,
                                                                           0, False,
                                                                           False, False)

        prochain = td.op("/container31/project1/prochain").par.value0
        self.assertEqual(prochain, 10 )


if __name__ == "__main__":
    unittest.main()


