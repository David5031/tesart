import unittest

import td


class IntegrationTestMain15(unittest.TestCase):
    # scenario integration test n°15

    # Description : The user changes song to song 5
    # Precondition : The artwork is running and next song is set to 5. The next true song is set to 2. audiofilein1B volume is set to 1 and constantBlackSpeed is 1.
    # Steps : 1) The user presses button2
    # Output : The next song should be 2 and next true song should be 3. constantBlackSpeed value should be 1. audiofilein1 volume should be 0.5 and it should be executed like audiofilein1B


    # tests for component presence

    @classmethod
    def setUpClass(cls):
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame_change_song_button.tox'
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


    # test sur le bouton pour changer la musique par la musique numéro 5

    def test_change_musique_button_num_5(self):
        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 5



        audiofilein1b = td.op("/container31/project1/audiofilein1B")
        audiofilein1b.par.volume = 1

        audiofilein1 = td.op("/container31/project1/audiofilein1")


        constantblackspeed = td.op("/container31/project1/constantBlackSpeed")
        constantblackspeed.par.value0 = 1

        vraiprochain = td.op("/container31/project1/vraiProchain")
        vraiprochain.par.value0 = 2


        #td.op("/container31/project1/button2").click( force = True) # it does not work
        #button2_component.par.value0=1
        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0,
                                                                   sampleIndex = 0,
                                                                   val = 1.0, prev = 0)
        print(prochain.par.value0)

        self.assertEqual(audiofilein1b.par.volume, 0.5) 
        self.assertEqual(audiofilein1.par.play, 1)
        self.assertEqual(audiofilein1b.par.play, 1)
        self.assertEqual(constantblackspeed.par.value0, 1)

        self.assertEqual(prochain.par.value0, 2)
        self.assertEqual(vraiprochain.par.value0, 3)

if __name__ == "__main__":
    unittest.main()