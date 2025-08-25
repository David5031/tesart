import unittest

import td


class IntegrationTestMain10(unittest.TestCase):
    # scenario integration test n°10

    # Description : The user choose song 9
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '9' on the keyboard.
    # Output : The next song should be song 9

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

    #keyboard 9
    def test_keyboard_9(self):

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'9',
                                                                         '9', False,
                                                                         False, False,
                                                                         False, False,
                                                                         False,False,
                                                                         False, False,
                                                                         True, 0, False,
                                                                         False, False)

        prochain = td.op("/container31/project1/prochain").par.value0
        td.op("/container31/project1/vraiProchain").par.value0

        self.assertEqual(prochain, 9)

if __name__ == "__main__":
    unittest.main()