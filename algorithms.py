from process import *
import copy
from process import Process

class Algorithms:
    def __init__(self):
        pass
    
    def fcfs(self, processes):
        
        processes.sort(key=lambda x: x.arrival_time)
        current_time = 0

        for process in processes:
            
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            
            start_time = current_time
            end_time = current_time + process.burst_time

            
            process.runs.append([start_time, end_time])
            current_time = end_time 

        
            process.response_time = start_time - process.arrival_time  
            process.turnaround_time = end_time - process.arrival_time  
            process.waiting_time = process.turnaround_time - process.burst_time  

        
        return processes

    def sjf_preemptive(self, process_list: list):
    
        gantt_chart = []
        time_intervals = {}        
        completed_process = {}
        initial_burst_times = {}
        
        for p in process_list:
            initial_burst_times[p.p_id] = p.burst_time
        
        t = sorted(process_list, key=lambda process: process.arrival_time)[0].arrival_time
           
        while len(process_list) != 0:
            
            available = []
    
            for p in process_list:
                if p.arrival_time <= t:
                    available.append(p)
            t += 1
            
            if len(available) != 0:
                available.sort(key=lambda process: process.burst_time)
                process = available[0]
                gantt_chart.append(process.p_id)
                process_list.remove(process)
                
                process.burst_time -= 1
    
                if process.p_id not in time_intervals:
                    time_intervals[process.p_id] = []
    
                time_intervals[process.p_id].append(t-1)
                
                if process.burst_time == 0:
                    process.burst_time = initial_burst_times[process.p_id]
            
                    CT = t
    
                    # Turnaround Time
                    process.turnaround_time = CT - process.arrival_time
    
                    # Waiting Time
                    process.waiting_time = process.turnaround_time - process.burst_time
    
                    # completed_process.append(process)
                    completed_process[process.p_id] = process
    
                else:
                    process_list.append(process)
    
        for key in time_intervals:
            min_time_boundary = 0
            max_time_boundary = 0
            
            for val in range(len(time_intervals[key])):
                if (val == len(time_intervals[key]) - 1) or (time_intervals[key][val + 1] - time_intervals[key][val] != 1):
                    completed_process[key].runs.append([time_intervals[key][min_time_boundary], time_intervals[key][max_time_boundary]+1])
                    min_time_boundary = val + 1    
                    max_time_boundary = val + 1    
    
                else:
                    max_time_boundary += 1    
    
        # list for final processes
        final_process_list = []
        
        for p in completed_process:
            # Response time
            completed_process[p].response_time = completed_process[p].runs[0][0] - completed_process[p].arrival_time
            final_process_list.append(completed_process[p])    
    
        return final_process_list

    
    def sjf_nonpreemptive(self, problem: list):
        current=0
        result=[]
        while problem:
            available=[]
            for i in problem:
                if i.arrival_time <=current:
                    available.append(i)
            if available:
                sj=available[0]
                for i in available:
                    if i.burst_time < sj.burst_time:
                        sj=i
                        
                problem.remove(sj)
                
                process = Process(sj.p_id, sj.arrival_time, sj.burst_time)
                
                start_time = max(current, process.arrival_time)
                complete_time = start_time + process.burst_time
                process.runs.append([start_time,complete_time])
                process.turnaround_time = complete_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                process.response_time = start_time - process.arrival_time

                current = complete_time
                
                result.append(process)
            else:
                current += 1
        return result
    
    
    def roundRobin(self, processes_ls:list[Process], qt:int):
        it = 0
        ls = []
        for i in processes_ls:
            i.sb = i.burst_time

        while (len(processes_ls) != 0):
            p = processes_ls.pop(0)
            if (p.arrival_time <= it):
                # if (len(p.runs) != 0):
                #     it = p.runs[-1][-1]

                if (p.burst_time > qt):
                    p.burst_time -= qt
                    it += qt
                    p.runs.append([it-qt, it])
                    processes_ls.append(p)
                else:
                    it += p.burst_time
                    p.runs.append([it-p.burst_time, it])
                    p.burst_time = p.sb
                    ct = p.runs[-1][1]
                    st = p.runs[0][0]
                    p.turnaround_time = ct - p.arrival_time
                    p.waiting_time = p.turnaround_time - p.burst_time
                    p.response_time = st - p.arrival_time
                    ls.append(p)
            else:
                processes_ls.append(p)
                it+=1
                
        
        return ls

    def priority_non_preemptive(self, processes: list):
        #processes.sort(key=lambda x: (x.arrival_time, x.priority if x.priority is not None else float('inf')))
        
        current_time = 0
        scheduled_processes = []
        
        while processes:

            available_processes = [p for p in processes if p.arrival_time <= current_time]
            if not available_processes:  
                current_time = processes[0].arrival_time
                continue
            
            selected_process = min(available_processes, key=lambda x: x.priority if x.priority is not None else float('inf'))
            
            selected_process.runs.append([current_time, current_time + selected_process.burst_time])
            selected_process.response_time = current_time - selected_process.arrival_time
            selected_process.waiting_time = current_time - selected_process.arrival_time
            selected_process.turnaround_time = selected_process.waiting_time + selected_process.burst_time
            
            current_time += selected_process.burst_time
            
            scheduled_processes.append(selected_process)
            processes.remove(selected_process)
        
        return scheduled_processes
    
    def premptive_priority(self, process_list):

        process_list.sort(key=lambda process: process.arrival_time)
        new_list = copy.deepcopy(process_list)
        t = 0
        available_process = []  
        completed_processes = []  
        while process_list or available_process:
            while process_list and process_list[0].arrival_time <= t:
                available_process.append(process_list.pop(0))
            if available_process:
                
                available_process.sort(key=lambda process: process.priority)
                current_process = available_process[0]
                #mainburst = current_process.burst_time
                if not current_process.runs or current_process.runs[-1][1] != t:
                    current_process.runs.append([t, t + 1]) 
                else:
                    current_process.runs[-1][1] += 1  

                current_process.burst_time -= 1

                if current_process.burst_time == 0:
                    available_process.remove(current_process)
                    computation_time = t + 1
                
                    current_process.turnaround_time = computation_time - current_process.arrival_time
                    
                    current_process.waiting_time = current_process.turnaround_time - sum(
                        run[1] - run[0] for run in current_process.runs
                    )
                    current_process.burst_time=[s for s in new_list if s.p_id == current_process.p_id][0].burst_time
                    completed_processes.append(current_process)
            else:
                pass
            # Increment time
            t += 1  
        # calc RT
        for process in completed_processes:
            process.response_time = process.runs[0][0] - process.arrival_time
       
        return completed_processes

    def sort_runtimes(self, processes: list):
        runtimes=[]
        for process in processes:
            for run in process.runs:
                runtimes.append([process.p_id,run])      
        sorted_data = sorted(runtimes, key=lambda x: x[1][0])
        return sorted_data
    
    def calculate_averages(self, processes: list):
        n = len(processes)
        total_turnaround_time = sum(p.turnaround_time for p in processes)
        total_waiting_time = sum(p.waiting_time for p in processes)
        total_response_time = sum(p.response_time for p in processes)

        return {
            "average_turnaround_time": total_turnaround_time / n,
            "average_waiting_time": total_waiting_time / n,
            "average_response_time": total_response_time / n
        }