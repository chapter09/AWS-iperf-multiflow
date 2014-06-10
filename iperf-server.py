#!/usr/bin/python

import os, sys
import subprocess

cli_num = int(sys.argv[1])
port = 5201

for cli_num in range(0, cli_num):
  p = subprocess.Popen(['sh', 'iperf-s.sh', str(port)],\
      stdout=subprocess.PIPE)
  port += 1
