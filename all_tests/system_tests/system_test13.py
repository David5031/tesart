import unittest

import td


class SystemTestMain13(unittest.TestCase):
    """system test : scenario 13."""

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


    # scenario system test n°13

    # Description : The user runs applause music
    # Precondition : The artwork is running with next song: n°5 and the next real song: n°1 with silence music loaded and constant black speed = 1
    # Steps : 1) The user presses on "button1__". 
    # Output : The applause music should be played, the next song should be song 1 and the next real song should be song 2

    def test_applause(self):

        audio_filein2 = td.op("/container31/project1/audiofilein2")
        #self.assertEqual(audio_filein2.type, "audiofilein")

        prochain = td.op("/container31/project1/prochain")
        #print("valeur de prochain par defaut", prochain.par.value0) 
        prochain.par.value0 = 5
        #print("value prochain pour applause normalement (5)" , prochain.par.value0)
        self.assertEqual(5, prochain.par.value0)

        vraiprochain = td.op("/container31/project1/vraiProchain")
        vraiprochain.par.value0 = 1


        constantblackspeed = td.op("/container31/project1/constantBlackSpeed")
        constantblackspeed.par.value0 = 1

        td.mod(td.op("/container31/project1/chopexec5")).onOffToOn(channel =0,
                                                                   sampleIndex = 0,
                                                                   val = 1.0, prev = 0)

        td.mod(td.op("/container31/project1/chopexec4")).onOffToOn(channel =0,
                                                                   sampleIndex = 0,
                                                                    val = 1.0, prev = 0) # chopexec4 is executed


        self.assertEqual(audio_filein2.par.file, "audio/transition-applaudissements.wav")
        self.assertEqual(constantblackspeed.par.value0, 1.0)  # -1 first

        self.assertEqual(audio_filein2.par.play, 1)


        self.assertEqual(prochain.par.value0, 1) # 5 if chopexec4 is not executed
        self.assertEqual(vraiprochain.par.value0, 2)

if __name__ == "__main__":
    unittest.main()

