import socket
import threading


def get_ip_status(lock, ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(1)
    try:
        result = server.connect_ex((ip, port))
        with lock:
            if result == 0:
                print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        pass
    finally:
        server.close()


if __name__ == '__main__':
    import time
    start = time.time()
    name = socket.getfqdn(socket.gethostname())
    host = socket.gethostbyname(name)
    port_range = (0, 10000)
    lock = threading.Lock()
    for port in range(port_range[0], port_range[1]):
        t = threading.Thread(target=get_ip_status, args=(lock, host, port))
        t.start()
    print(time.time()-start)
