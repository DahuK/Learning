'''
Using kazoo to listen the agent numbers in zookeeper
'''
import time
import os
import tarfile
import subprocess
import traceback

WORK_PATH = os.path.join('/tmp', 'AgentIteratorWatcher')
print 'installing six package first...'
tar = tarfile.open(os.path.join(WORK_PATH, "six-1.9.0.tar.gz"))
tar.extractall()
tar.close()
#subprocess.call(['python', 'setup.py', 'install'], cwd=os.path.join(WORK_PATH, 'six-1.9.0'))
install_cmd = 'python setup.py install'
try:
    rc = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, shell=True, cwd=os.path.join(WORK_PATH, 'six-1.9.0')).communicate()[0].strip()
    print(rc)
    print('Successful install six' )
except subprocess.CalledProcessError as e:
    print('Fail to install six!')
    exit(1)
    
print 'installing kazoo package...'
tar = tarfile.open("kazoo-2.2.1.tar.gz")
tar.extractall()
tar.close()
try:
    rc = subprocess.Popen(install_cmd, stdout=subprocess.PIPE, shell=True, cwd=os.path.join(WORK_PATH, 'kazoo-2.2.1')).communicate()[0].strip()
    print(rc)
    print('Successful install kazoo' )
except subprocess.CalledProcessError as e:
    print('Fail to install kazoo!')
    exit(1)
    
time.sleep(3)

start_watcher_cmd = 'python num_watcher.py'
try:
    subprocess.Popen(['python', 'num_watcher.py'], cwd=WORK_PATH)
except subprocess.CalledProcessError as e:
    traceback.print_exc()
    exit(1)



