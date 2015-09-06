'''
Using kazoo to listen the agent numbers in zookeeper
'''
import time
import os

WORK_PATH = os.path.join('/tmp', 'AgentIteratorWatcher')

from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch, DataWatch

print 'start the kazoo watcher...'
zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()
#mock here would remove if rational team fix the path error
zk.create('/testcluster1/master/iterator', '40')

#@zk.DataWatch("/testcluster1/master/iterator")
#def changed(data, stat, event):
#    print "--------------DataWatch---------------"
#    print "data:", data
#    print "stat:", stat
#    print "event:", event

def _scale_agent(data, stat): 
    print "--------------DataWatch---------------"
    print data
    print stat
    join_ip_file = os.path.join('/tmp', 'agentNum')
    with open(join_ip_file, 'w+') as f:
        f.write(data)
   
try:
    watcher = DataWatch(zk, "/testcluster1/master/iterator", _scale_agent)
    while True:
        time.sleep(1)
except Exception as e:
    print(e)
    zk.stop()




