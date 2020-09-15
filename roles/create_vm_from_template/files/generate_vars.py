#!/usr/bin/python

import re
import sys

outfile2 = open('./roles/create_vm_from_template/vars/vm_vars.yml', 'w')

file_head = '''---
myvms:
'''
outfile2.write(file_head)

# 通过对vm_list文件中的内容来制作用于创建虚拟机的虚拟机配置信息数据
with open('./roles/create_vm_from_template/files/vm_list', 'r') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        #linetest = re.split(r'[;,]+', line)
        linetest = re.split(r'[;,\t]+', line)
        host2text = '''
  - vm_name: {0}
    template_name: {1}
    cluster: {2}
    esxi_hostname: {3}
    folder_path: {4}
    datastore: {5}
    d1_size_gb: {6}
    d2_size_gb: {7}
    memory_mb: {8}
    num_cpus: {9}
    ip: {10}
    gw: {11}
    hostname: {12}
    domain: {13}
    vlan: {14}
    version: {15}'''.format(linetest[0],linetest[1],linetest[2],linetest[3],linetest[4],linetest[5],linetest[6],linetest[7],linetest[8],linetest[9],linetest[10],linetest[11],linetest[12],linetest[13],linetest[14],linetest[15])
        print >> outfile2, host2text

