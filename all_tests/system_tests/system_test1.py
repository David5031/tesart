import unittest

import td


class SystemTestMain(unittest.TestCase):
    """system test : scenario 1."""

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


    # scenario system test number 1

    # Description : The user chooses song 10 and runs it
    # Precondition : The artwork is running with next song: number 1 and the next real song: number 2
    # Steps : 1) The user presses the key '0' on the keyboard. 2) The user presses the key '-' on the keyboard.
    # Output : The song 10 should be played, the next song should be song 5 and the next real song should be song 2

    def test_song_0(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiprochain = td.op("/container31/project1/vraiProchain")
        vraiprochain.par.value0 = 2


        tempbuttonb = td.op("/container31/project1/tempButtonB")
        tempbuttonb.par.value0 = 0


        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'0','0',
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, False,
                                                                           False, True,
                                                                           0, False,
                                                                           False,False)

        td.mod(td.op("/container31/project1/keyboardin1_callbacks")).onKey(None,'-',
                                                                           '-', False,
                                                                           False, False,
                                                                           False, False,
                                                                           False,False,
                                                                           False, False,
                                                                           True, 0,
                                                                           False, False,
                                                                           False)

        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)  # change prochain value

        self.assertEqual(td.op("/container31/project1/prochain").par.value0, 5 )
        self.assertEqual(td.op("/container31/project1/vraiProchain").par.value0,2)
        self.assertEqual(td.op("/container31/project1/tempButtonB").par.value0, 1)


if __name__ == "__main__":
    unittest.main()

