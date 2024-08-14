import random
import string
import unittest
import time
import timeit
import psutil
import GPUtil
import platform

import td

class LoadTestMain(unittest.TestCase):
    """load test : 1."""
    
    @classmethod
    def setUpClass(cls) :
        cls.base_path = td.op("/")
        cls.tox_path = './wall_of_fame.tox'
        if(td.op("/container31") == None):
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

    def simulate_key_press(key):
        keyboardin1_callbacks = td.op("/container31/project1/keyboardin1_callbacks")
        td.mod(keyboardin1_callbacks).onKey(None,key,key, False, False, False, False, False, False,False, False, False, True, 0, False, False, False)

    def simulate_music_change():
        chopexec4 = td.op("/container31/project1/chopexec4")
        td.mod(chopexec4).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)

    def simulate_applause():
        chopexec5 = td.op("/container31/project1/chopexec5")
        td.mod(chopexec5).onOffToOn(channel =0, sampleIndex = 0, val = 1.0, prev = 0)

    
    def test_load(self):   
        print("load test :")

        system_info = platform.uname()
        print("System information:")
        print("System:" + system_info.system)
        print("Node name :" + system_info.node)
        print("Machine :" + system_info.machine)
        print("Processor :" + system_info.processor + "\n")
    
        
        
        #print("channels in perform1:")
        #for chan in perform1_chop.chans():
        #    print(chan.name)
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print("Data before tests :")
            print("GPU" + str(gpu.id) + ":")
            print("Name:" + str(gpu.name))
            print(f"Memory: {gpu.memoryUsed} MiB / {gpu.memoryTotal} MiB")
            print(f"Utilization: {gpu.load * 100}%")
            print(f"Temperature: {gpu.temperature} °C")
            print("\n")
      
        #simulation
        num_iterations = 3
        start_time = time.time()

        prochain = td.op("/container31/project1/prochain")
        prochain.par.value0 = 1

        vraiProchain = td.op("/container31/project1/vraiProchain")
        vraiProchain.par.value0 = 1

        LoadTestMain.simulate_music_change()
        print('ca devrait 5')
        print(prochain.par.value0)

        for i in range(num_iterations):
            key = str(i%10)
            print("key :", key)
            
            
            LoadTestMain.simulate_key_press(key)  
            LoadTestMain.simulate_key_press('-')
            print('valeur de prochain')
            print(prochain.par.value0)
            time.sleep(3)

        #print('ca devrait 5 aussi')
        print(prochain.par.value0)
        LoadTestMain.simulate_applause()
        print('peut etre applaudissement')
        print(td.op("/container31/project1/audiofilein2").par.file)

        
        perform1_chop = td.op("/perform1")
        if perform1_chop == None:
            print("Perfom CHOP not found")
        
        # mise a jour
        perform1_chop.cook(force=True)

       
        
        print('\n')
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
                print(f" {fps} fps")
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

        frameTime_chan = perform1_chop.chan("msec") 
        frameTime = frameTime_chan.eval()
        print(f"frametime: {frameTime} msec")
        

        droppedframes_chan = perform1_chop.chan("dropped_frames")
        if droppedframes_chan != None :
            #droppedframes = droppedframes_chan.eval()
            print(f"dropped frames: {droppedframes_chan} frames")
        else:
            print("pas de dropped frames ")

        gpumemused_chan = perform1_chop.chan("gpu_mem_used")
        if gpumemused_chan :
            gpumemused = gpumemused_chan.eval()
            print(f"gpu mem used: {gpumemused} megabytes")
        else:
            print("pas de gpu mem used ")   

        cpumemused_chan = perform1_chop.chan("cpu_mem_used")
        if cpumemused_chan :
            cpumemused = cpumemused_chan.eval()
            print(f"cpu mem used: {cpumemused} megabytes")
        else:
            print("pas de cpu mem used ") 
       
        end_time= time.time()
        print(f"load test duration : {end_time - start_time} secondes")


        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU usage: {cpu_usage} %")

        memory_usage = psutil.virtual_memory()
        print(f"Memory usage: {memory_usage.percent}%")

        disk_usage = psutil.disk_usage('/')
        print(f"disk usage: {disk_usage.percent}%")
        print('\n')

        p = psutil.Process()
        # touchdesigner process
        process_name = p.name()
        process_cpu_percent = p.cpu_percent() 
        process_memory_percent = p.memory_percent()
  

        print("process name :"  + str (process_name) ,
               "process cpu percent :" + str(process_cpu_percent) , 
               "process memory percent :" + str(process_memory_percent) ,)
           
        print('\n')
    
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print("Data after tests :")
            print("GPU" + str(gpu.id) + ":")
            print("Name:" + str(gpu.name))
            print(f"Memory: {gpu.memoryUsed} MiB / {gpu.memoryTotal} MiB")
            print(f"Utilization: {gpu.load * 100}%")
            print(f"Temperature: {gpu.temperature} °C")
            print("\n")
     
    
if __name__ =="__main__":
    unittest.main()
