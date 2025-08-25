import platform
import time
import unittest

import GPUtil
import psutil
import td


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
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



    def simulate_key_press(self, key):
        keyboardin1_callbacks = td.op("/container31/project1/keyboardin1_callbacks")
        td.mod(keyboardin1_callbacks).onKey(None,key,key,
                                            False, False,
                                            False, False,
                                            False, False,
                                            False, False,
                                            False, True,
                                            0, False,
                                            False, False)

    def simulate_music_change():
        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)

    def simulate_applause():
        chopexec5 = td.op("/container31/project1/chopexec5")
        td.mod(chopexec5).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)

    def test_stress(self):
        system_info = platform.uname()
        print("System information:")
        print("System:" + system_info.system)
        print("Node name :" + system_info.node)
        print("Machine :" + system_info.machine)
        print("Processor :" + system_info.processor + "\n")


        print("stress test :")

        #version Nvidia
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print("Data before simulation :")
            print("GPU" + str(gpu.id) + ":")
            print("Name:" + str(gpu.name))
            print(f"GPU Memory: {gpu.memoryUsed} MiB / {gpu.memoryTotal} MiB")
            print(f"GPUUtilization: {gpu.load * 100}%")
            print(f"GPU Temperature: {gpu.temperature} °C")
            print("\n")

        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU usage : {cpu_usage} %")

        memory_usage = psutil.virtual_memory()
        print(f"Virtual memory : {memory_usage.percent}%")

        disk_usage = psutil.disk_usage('/')
        print(f"disk usage : {disk_usage.percent}%")

        num_iterations = 50

        # pour verifier les ressources

        print('\n')
        perform1_chop = td.op("/perform1")
        if perform1_chop is None:
            print("Perfom CHOP not found")

        perform1_chop.cook(force=True)

        td.op("/container31").cook(force=True)
        cook_chan = perform1_chop.chan("cook")
        if cook_chan :
            cook = cook_chan.eval()
            print(f"cook: {cook}")
        else:
            print("pas de cook " )

        perform1_chop.cook(force=True)
        fps_chan = perform1_chop.chan("fps")
        if fps_chan :
            fps = fps_chan.eval()
            if fps:
                print(f"{fps} fps ")
            else:
                print("pas de fps valide")
        else:
            print("pas de fps ", fps_chan )

        cook_realtime_chan = perform1_chop.chan("cookrealtime")
        if cook_realtime_chan :
            cook_realtime = cook_realtime_chan.eval()
            print(f"cook realtime: {cook_realtime}")
        else:
            print("pas de cook realtime " )

        frametime_chan = perform1_chop.chan("msec")
        frametime = frametime_chan.eval()
        print(f"frame time: {frametime} msec")

        droppedframes_chan = perform1_chop.chan("dropped_frames")
        if droppedframes_chan is not None :

            print(f"dropped frames: {droppedframes_chan} frames")
        else:
            print("pas de dropped frames ")

        gpumemused_chan = perform1_chop.chan("gpu_mem_used")
        if gpumemused_chan :
            gpumemused = gpumemused_chan.eval()
            print(f"gpu memory used: {gpumemused} megabytes")
        else:
            print("pas de gpu mem used ")

        cpumemused_chan = perform1_chop.chan("cpu_mem_used")
        if cpumemused_chan :
            cpumemused = cpumemused_chan.eval()
            print(f"cpu memory used: {cpumemused} megabytes")
        else:
            print("pas de cpu mem used ")

        print('\n')

        #simulation
        for i in range(num_iterations):
            key = str(i%10)
            print("key :", key)
            #self.simulate_key_press(key)
            TestMain.simulate_music_change()
            TestMain.simulate_applause()
            self.simulate_key_press('-')
            time.sleep(0.5)

        print('\n')

        perform1_chop = td.op("/perform1")
        if perform1_chop is None:
            print("Perfom CHOP not found")

        perform1_chop.cook(force=True)
        td.op("/container31").cook(force=True)

        cook_chan = perform1_chop.chan("cook")
        if cook_chan :
            cook = cook_chan.eval()
            print(f"cook: {cook}")
        else:
            print("pas de cook " )

        fps_chan = perform1_chop.chan("fps")
        if fps_chan :
            fps = fps_chan.eval()
            if fps:
                print(f"{fps} fps ")
            else:
                print("pas de fps valide")
        else:
            print("pas de fps ", fps_chan )

        cook_realtime_chan = perform1_chop.chan("cookrealtime")
        if cook_realtime_chan :
            cook_realtime = cook_realtime_chan.eval()
            print(f"cook realtime: {cook_realtime}")
        else:
            print("pas de cook realtime " )

        frametime_chan = perform1_chop.chan("msec")
        frametime = frametime_chan.eval()
        print(f"frame time: {frametime} msec")


        droppedframes_chan = perform1_chop.chan("dropped_frames")
        if droppedframes_chan is not None :

            print(f"dropped frames: {droppedframes_chan} frames")
        else:
            print("pas de dropped frames ")

        gpumemused_chan = perform1_chop.chan("gpu_mem_used")
        if gpumemused_chan :
            gpumemused = gpumemused_chan.eval()
            print(f"gpu memory used: {gpumemused} megabytes")
        else:
            print("pas de gpu mem used ")

        cpumemused_chan = perform1_chop.chan("cpu_mem_used")
        if cpumemused_chan :
            cpumemused = cpumemused_chan.eval()
            print(f"cpu memory used: {cpumemused} megabytes")
        else:
            print("pas de cpu mem used ")

        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU usage: {cpu_usage} %")


        cpu_times = psutil.cpu_times()
        print(f"CPU times: {cpu_times} ")


        cpu_stats = psutil.cpu_stats()
        print(f"CPU stats: {cpu_stats} ")

        cpu_frequency = psutil.cpu_freq()
        print(f"CPU frequence: {cpu_frequency} ")

        virtual_memory_usage = psutil.virtual_memory()
        print(f"Virtual memory usage: {virtual_memory_usage.percent}%")


        swap_memory = psutil.swap_memory()
        print(f"swap memory: {swap_memory} ")

        disk_usage = psutil.disk_usage('/')
        print(f"disk usage: {disk_usage.percent}%")

        p = psutil.Process()

        # touchdesigner process
        process_name = p.name()
        process_cpu_percent = p.cpu_percent() 
        process_memory_percent = p.memory_percent()

        print("process name :"  + str (process_name),
               "process cpu percent :" + str(process_cpu_percent),
               "process memory percent :" + str(process_memory_percent), )

        print('\n')

        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print("Data after tests :")
            print("GPU" + str(gpu.id) + ":")
            print("Name:" + str(gpu.name))
            print(f"GPU Memory: {gpu.memoryUsed} MiB / {gpu.memoryTotal} MiB")
            print(f"GPU Utilization: {gpu.load * 100}%")
            print(f"GPU Temperature: {gpu.temperature} °C")
            print("\n")


if __name__=="__main__":
    unittest.main()
