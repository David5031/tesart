import unittest

import td


class SystemTestMain2(unittest.TestCase):
    """system test : scenario 2 ."""

    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame.tox'
        if(td.op("/container31") is None):
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


    # scenario system test n°2

    # Description : The user choose song 1 and run it
    # Precondition : The artwork is running with next song: n°1 and the next real song: n°2
    # Steps : 1) The user presses the key '1' on the keyboard. 2) The user presses the key '-' on the keyboard.
    # Output : The song 1 should be played, the next song should be song 5 and the next real song should be song 2

    def test_song_1(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiprochain = td.op("/container31/project1/vraiProchain")
        vraiprochain.par.value0 = 2

        tempbuttonb = td.op("/container31/project1/tempButtonB")
        tempbuttonb.par.value0 = 0

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'1','1',
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, True,
                                                                           0, False,
                                                                           False, False)

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-','-',
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, True,
                                                                           0, False,
                                                                           False, False)

        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)  # change prochain value

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 5 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,2)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)



if __name__ == "__main__":
    unittest.main()

