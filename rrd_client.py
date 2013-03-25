#!/usr/bin/python
import os, sys
import rrdtool
import glob
from .settings import *

def get_rrd_info(path):
    return rrdtool.info(path)["ds[sum].last_ds"]

def get_rrd_value(dir_path):
    cluster_file = glob.glob(dir_path)
    results = {}
    for v in cluster_file:
        result = get_rrd_info(v)
        results[v] = result
    return results

def get_rrd_detail(cluster_id,phost_id,rrd_id, default_path=DEFAULT_RRD_PATH):
    dir_rrd = os.path.join(default_path, cluster_id,phost_id,rrd_id)
    if not os.path.isfile(dir_rrd): return None
    return get_rrd_info(dir_rrd)

def get_phost_detail(cluster_id,phost_id, default_path=DEFAULT_RRD_PATH):
    dir_phost = os.path.join(default_path, cluster_id,phost_id, '*.rrd')
    return get_rrd_value(dir_phost)

def get_cluster_detail(cluster_id, default_path=DEFAULT_RRD_PATH):
    dir_cluster = os.path.join(default_path,cluster_id,'*', '*.rrd')
    return get_rrd_value(dir_cluster)

               
if __name__ == '__main__':
    pass
