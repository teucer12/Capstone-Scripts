#!/usr/bin/env python3
import subprocess

subprocess.call("chmod 755 Bashscript.sh", shell=True)
subprocess.call("./Bashscript.sh", shell=True)
