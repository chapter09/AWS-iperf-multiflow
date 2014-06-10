#!/usr/bin/python

import os, sys
import subprocess

dst = sys.argv[1]
cli_num = int(sys.argv[2])

port = 5201

for i in range(0, cli_num):
  p = subprocess.Popen(['sh', 'iperf-c.sh', dst, str(port), str(cli_num)],\
      stdout=subprocess.PIPE)
  port += 1
