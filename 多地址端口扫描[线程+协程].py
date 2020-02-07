import asyncio
import functools
import threading


# 端口扫描
class PortScan:
    def __init__(self, ip_list, rate, all_ports=None):
        super(PortScan, self).__init__()
        self.ip_list = ip_list
        self.rate = rate if rate else 500
        self.scan_port_list = []
        self.common_port = "21,22,23,25,53,69,80,81,82,83,84,85,86,87,88,89,110,111,135,139,143,161,389,443,445,465,513,873,993,995,1080,1099,1158,1433,1521,1533,1863,2049,2100,2181,3128,3306,3307,3308,3389,3690,5000,5432,5900,6379,7001,8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017,8018,8019,8020,8021,8022,8023,8024,8025,8026,8027,8028,8029,8030,8031,8032,8033,8034,8035,8036,8037,8038,8039,8040,8041,8042,8043,8044,8045,8046,8047,8048,8049,8050,8051,8052,8053,8054,8055,8056,8057,8058,8059,8060,8061,8062,8063,8064,8065,8066,8067,8068,8069,8070,8071,8072,8073,8074,8075,8076,8077,8078,8079,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,8888,9000,9080,9090,9200,9300,9418,11211,27017,27018,27019,50060"
        self.ports = [port for port in range(11, 65535)] if all_ports else self.common_port.split(',')

    async def port_check(self, sem, ip_port):
        async with sem:
            ip, port = ip_port
            conn = asyncio.open_connection(ip, port)
            try:
                _, _ = await asyncio.wait_for(conn, timeout=2)
                return ip, port, 1
            except:
                return ip, port, 0

    async def async_tcp_scan(self, ip, loop):
        sem = asyncio.Semaphore(self.rate)
        asyncio.set_event_loop(loop)
        tasks = []
        for port in self.ports:
            one_ip_sacn_task = asyncio.ensure_future(self.port_check(sem, (ip, int(port))))
            one_ip_sacn_task.add_done_callback(self.callback)
            tasks.append(one_ip_sacn_task)
        futus = asyncio.gather(*tasks)

        def done_callback(loop,fufu):
            loop.stop()

        futus.add_done_callback(functools.partial(done_callback, loop))
        # loop.run_until_complete(asyncio.wait(tasks))

    def callback(self, future):
        ip, port, status = future.result()
        if status:
            print(ip, port, status)

    def thread_tcp_port_scan(self):
        def start_loop(loop):
            asyncio.set_event_loop(loop)
            loop.run_forever()

        for ip in self.ip_list:
            sub_loop = asyncio.new_event_loop()
            t = threading.Thread(target=start_loop, args=(sub_loop,))
            t.start()
            future = asyncio.run_coroutine_threadsafe(self.async_tcp_scan(ip, sub_loop), sub_loop)
            # future.add_done_callback(close_loop(sub_loop))


import time

if __name__ == '__main__':
    ip_list = ["127.0.0.1","106.75.227.164","14.116.225.3"]
    now = time.time
    start = now()
    ps = PortScan(ip_list, 500)
    # ps.async_tcp_scan(ip_list[0])
    ps.thread_tcp_port_scan()
    print("Time:", now() - start)
