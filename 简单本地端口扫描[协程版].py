import asyncio
import socket
import time


async def get_ip_status(semaphore,ip, port):
    conn = asyncio.open_connection(ip, port)
    async with semaphore:
        try:
            _, _ = await asyncio.wait_for(conn, timeout=1)
            return ip, port, 1
        except:
            return ip, port, 0


def callback(future):
    ip, port, result = future.result()
    if result == 1:
        print('{0} port {1} is open'.format(ip, port))


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    name = socket.getfqdn(socket.gethostname())
    host = socket.gethostbyname(name)
    port_range = (0, 10000)
    sem = asyncio.Semaphore(500)  # 限制并发量
    tasks = []
    for port in range(port_range[0], port_range[1]):
        task = asyncio.ensure_future(get_ip_status(sem, host, port))
        task.add_done_callback(callback)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)
