#!/usr/bin/python

import os, sys
import subprocess

dst = sys.argv[1]
cli_range = int(sys.argv[2])

port = 5201

for cli_num in range(1, cli_range+1):
    print "---", cli_num, "---"
    iperfc = []
    for i in range(0, cli_num):
        p = subprocess.Popen(['sh', 'iperf-c.sh', dst, str(port), str(cli_num)],\
        stdout=subprocess.PIPE)
        iperfc.append(p)
        port += 1
    print "--- WAITING ---"
    for p in iperfc:
        ret = p.wait()
        print cli_num, "---", ret
    
