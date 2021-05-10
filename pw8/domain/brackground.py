import pickle
import threading


class BackgroundThread(threading.Thread):
    def __init__(self, mode, pickled, dumped=None, loaded=None):
        threading.Thread.__init__(self)
        self.__mode = mode
        self.__pickled = pickled
        self.__dumped = dumped
        self.__loaded = loaded

    def run(self):
        if self.__mode == "dump":
            if self.__dumped is not None:
                pickle.dump(self.__dumped, self.__pickled)
            else:
                return 0
        elif self.__mode == "load":
            if self.__loaded is not None:
                loaded_file = pickle.load(self.__pickled)
                self.__loaded.append(loaded_file)
            else:
                return 0
