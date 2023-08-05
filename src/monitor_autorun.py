# testing...

# https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
# https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
# watch files
"""
  Coding is not easy when there different os effect how it coded.
  window = ok
  Linux = not tested
  Mac = note tested
"""


import signal
from os import kill
import subprocess
import os
from subprocess import Popen

#subprocess.run(["python", "my_script.py"])

#proc = subprocess.Popen(["python", "src/main.py"])
pro = subprocess.Popen("python src/main.py", stdout=subprocess.PIPE, 
                       shell=True) 
try:
  pro.wait(timeout=5)
except subprocess.TimeoutExpired:
  #pro.kill()
  Popen("TASKKILL /F /PID {pid} /T".format(pid=pro.pid))
print("end test")