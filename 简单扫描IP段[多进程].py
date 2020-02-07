import os
import time
import subprocess
from multiprocessing import Pool
from IPy import IP


def ping_call(ip):
    fnull = open(os.devnull, 'w')
    ipaddr = 'ping ' + str(ip)
    result = subprocess.call(ipaddr + ' -n 2', shell=True, stdout=fnull, stderr=fnull)
    current_time = time.strftime('%Y%m%d-%H:%M:%S', time.localtime())
    if result:
        print('时间:{} ip地址:{} ping fall'.format(current_time, ipaddr))
    else:
        print('时间:{} ip地址:{} ping ok'.format(current_time, ipaddr))
    fnull.close()


if __name__ == '__main__':
    start_time = time.time()
    p = Pool(100)
    res_l = []
    for ip in IP("192.168.0.0/24"):
        res = p.apply_async(ping_call, args=(ip,))
        res_l.append(res)
    for res in res_l:
        res.get()
    print('程序耗时{:.2f}'.format(time.time() - start_time))
