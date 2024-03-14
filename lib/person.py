#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Bob', job="Admin"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)) and 1 <= len(name_param) <= 25:
            self._name = name_param.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    @job.setter
    def job(self, job_param):
        if(job_param in APPROVED_JOBS):
            self._job = job_param
        else:
            print( "Job must be in list of approved jobs.")

    
