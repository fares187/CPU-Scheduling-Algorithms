# CPU Scheduling Algorithms Simulator

This project is a simulation tool for various CPU scheduling algorithms, developed as a final project for the Operating Systems course. It provides a graphical user interface (GUI) to facilitate the visualization and analysis of different scheduling strategies.



https://github.com/user-attachments/assets/20f41c80-f47c-4958-a747-f1ef60dd7c0d



## Table of Contents

- [Overview](#overview)
- [Implemented Algorithms](#implemented-algorithms)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)

## Overview

The simulator allows users to input processes with specific attributes and observe how different CPU scheduling algorithms manage these processes. It calculates and displays key performance metrics such as:

- **Waiting Time**
- **Turnaround Time**
- **Response Time**
- **CPU Utilization**
- **Throughput**

A Gantt chart is generated to provide a visual representation of process execution over time.

## Implemented Algorithms

The simulator includes the following CPU scheduling algorithms:

1. **First Come First Serve (FCFS)**: Processes are executed in the order of their arrival without preemption.
2. **Shortest Job First (SJF) - Non-Preemptive**: Selects the process with the shortest burst time from the ready queue. Once a process starts execution, it runs to completion.
3. **Shortest Job First (SJF) - Preemptive**: Also known as Shortest Remaining Time First (SRTF). The process with the shortest remaining burst time is selected, and preemption occurs if a new process arrives with a shorter burst time.
4. **Priority Scheduling - Non-Preemptive**: Processes are scheduled based on priority. Higher priority processes are executed first. If two processes have the same priority, FCFS is used as a tie-breaker.
5. **Priority Scheduling - Preemptive**: Similar to the non-preemptive version but allows preemption if a higher priority process arrives.
6. **Round Robin (RR)**: Each process is assigned a fixed time quantum. Processes are executed in a cyclic order, and preemption occurs if a process's execution exceeds the time quantum.

## Features

- **User-Friendly GUI**: Built with Python's Tkinter library, the GUI allows users to:
  - Input process details (arrival time, burst time, priority).
  - Select the desired scheduling algorithm.
  - Set the time quantum for Round Robin scheduling.
  - Visualize the scheduling process through a Gantt chart.
  - View calculated performance metrics.

- **Modular Codebase**: The project is structured with modularity in mind, separating concerns across different files and classes for better maintainability and scalability.

## Project Structure

The repository consists of the following key files:

- `app.py`: Main application file that initializes and runs the GUI.
- `algorithms.py`: Contains implementations of the various CPU scheduling algorithms.
- `process.py`: Defines the `Process` class, representing individual processes with their attributes.
- `hotizntalscroll.py`: Handles horizontal scrolling functionality within the GUI.
- `image.png`: An image resource used in the GUI.
- `README.md`: This README file.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fares187/CPU-Scheduling-Algorithms.git
   ```


2. **Navigate to the project directory**:
   ```bash
   cd CPU-Scheduling-Algorithms
   ```


3. **Run the application**:
   ```bash
   python app.py
   ```
