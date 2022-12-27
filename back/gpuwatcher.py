import json
import time
import os
import pynvml
import socket
import threading

pynvml.nvmlInit()
gpu_nums = pynvml.nvmlDeviceGetCount()
handle_list = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(gpu_nums)]
body = {
    'gpu_nums': gpu_nums,
    'gpu_info': {}, 
    '_date': None}

def get_gpu_info():
    gpu_info = {}
    for i in range(len(handle_list)):
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle_list[i])
        gpu_info[i] = {
            'status': '{:.1f}M/{:.1f}M'.format(meminfo.used / 2**20, meminfo.total / 2**20),
            'percentage': round(meminfo.used / meminfo.total * 100)
        }
    return gpu_info