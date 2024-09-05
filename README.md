# Supervisor Assignment System for Exams

## Project Overview
This Python project automates the process of assigning supervisors to exam sessions at the **Athens University of Economics and Business (AUEB)**. The system manages both lessons and supervisors, ensuring that all exams are properly supervised while respecting the availability constraints of the supervisors.

## Features

- **Input Data**:
  - **Lessons**: Each lesson is described by an ID, title, exam date/time, exam rooms, number of required supervisors, and the instructor's name.
  - **Supervisors**: Each supervisor has an ID, name, email, and a limit on how many lessons they can supervise. They can also declare up to 5 lessons in which they are unavailable.
  
- **Functionality**:
  - Assigns supervisors to exam sessions while respecting their availability.
  - Outputs the final assignments in a structured, human-readable format (CSV or TXT).
  
- **File-Based Input**:
  - The system reads lesson and supervisor data from two CSV files (`lessons.csv` and `supervisors.csv`).
