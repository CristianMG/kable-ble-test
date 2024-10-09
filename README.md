CPUTemp Based on https://github.com/Douglas6/cputemp
========== 
Scripts are developed on raspberry pi 3.

Added the next configuration in this file
/etc/bluetooth/main.      
[General]
PairableTimeout = 0
DiscoverableTimeout = 0
ControllerMode = le
Experimental = true

Execute 
```bash
pip install virtualenv
virtualenv kable-env
source venv/bin/activate
pip install -r requirements.txt
python cputemp.py
