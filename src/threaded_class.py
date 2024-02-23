from  multiprocessing import Process, Queue, Pipe

def threaded_class(cls):
    main_process = Process(target=cls)
    main_process.start()