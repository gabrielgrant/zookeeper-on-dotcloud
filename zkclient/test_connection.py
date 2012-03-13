import os

import zookeeper
import pykeeper

host = os.environ['DOTCLOUD_ZOOKEEPER_CONNECTION_HOST']
port = os.environ['DOTCLOUD_ZOOKEEPER_CONNECTION_PORT']
connection_str = '%s:%s' % (host, port)
#client = pykeeper.ZooKeeper(connection_str)

def callback(*args, **kwargs):
    print args
    print kwargs

handle = zookeeper.init(connection_str, callback)

zookeeper.client_id(handle)
zookeeper.exists(handle, '/')
zookeeper.get(handle, '/')
zookeeper.get_children(handle, '/')
zookeeper.state(handle)
