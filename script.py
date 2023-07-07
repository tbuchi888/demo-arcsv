#!/usr/bin/env python3
import subprocess
subprocess.run("date && echo \"--- Start --\"", shell=True)
subprocess.run("hostname", shell=True)
subprocess.run("whoami", shell=True)
subprocess.run("ip a", shell=True)
subprocess.run("date && echo \"---  End  --\"", shell=True)
