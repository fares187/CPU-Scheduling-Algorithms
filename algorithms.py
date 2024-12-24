from process import *

class Algorithms:
    def __init__(self, processes: list):
        self.processes=processes
    
    def sort_runtimes(self):
        runtimes=[]
        for process in self.processes:
            for run in process.runs:
                runtimes.append([process.p_id,run])      
        sorted_data = sorted(runtimes, key=lambda x: x[1][0])
        return sorted_data