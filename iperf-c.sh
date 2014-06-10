#!/bin/bash

iperf -c $1 -t 180 -i 1 -p $2 > $1-$2-c$3.log
