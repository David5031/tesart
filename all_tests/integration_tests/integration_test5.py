import unittest

import td


class IntegrationTestMain5(unittest.TestCase):
    # scenario integration test n°5

    # Description : The user choose song 4
    # Precondition : The artwork is running.
    # Steps : 1) The user presses the key '4' on the keyboard.
    # Output : The next song should be song 4 and next true song should be song 1

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

    #keyboard 4
    def test_keyboard_4(self):

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'4',
                                                                           '4', False, 
                                                                           False, False, 
                                                                           False, False, 
                                                                           False,False, 
                                                                           False, False, 
                                                                           True, 0, 
                                                                           False, False, 
                                                                           False)
        prochain = td.op("/container31/project1/prochain").par.value0
        #print("(valeur de prochain)", prochain)
        vrai_prochain = td.op("/container31/project1/vraiProchain").par.value0

        self.assertEqual(prochain, 4 )
        self.assertEqual(vrai_prochain,1)



if __name__ == "__main__":
    unittest.main()
