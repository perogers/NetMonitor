# Simple script to monitor if host is reachable.

## Scripts

* `monitor_runner.sh` runs the python 2 script.
* `monitor.py` the host and logs failures to `monitor.log`


## Usage:

`nohup ./monitor_runner.sh <host to monitor> <ping timeout seconds> <delay between pings seconds> &`
