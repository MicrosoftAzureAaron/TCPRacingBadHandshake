#!/bin/bash
#block host from sending TCP RST due to  wrong order non RFC tcp
sudo iptables -A OUTPUT -p tcp -d 192.168.1.105 --tcp-flags RST RST -j DROP

# Set the duration for running the loop in seconds (5 minutes in this example)
duration=$((15 * 60))

# Get the start time
start_time=$(date +%s)

srcprt=2000
dstprt=4000

while [ $(( $(date +%s) - start_time )) -lt $duration ]; do
    # for ((i=0; i<100; i++)); do
    #     sp=$((srcprt + i))
    #     dp=$((dstprt + i))
    #     python3 client.py "$sp" "$dp" &
    # done
    python3 client.py
    # Sleep for 5.5 to wait for TCP RSTs from VFP half open state
    sleep 7
done

echo "Python script loop completed."