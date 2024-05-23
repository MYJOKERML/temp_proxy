import os

def set_temp_proxy(mixedPort):
    """
    设置临时代理。

    参数:
    mixedPort (int): 代理端口号。
    """
    https_proxy = f"http://127.0.0.1:{mixedPort}"
    http_proxy = f"http://127.0.0.1:{mixedPort}"
    all_proxy = f"socks5://127.0.0.1:{mixedPort}"

    os.environ['https_proxy'] = https_proxy
    os.environ['http_proxy'] = http_proxy
    os.environ['all_proxy'] = all_proxy

def clear_temp_proxy():
    """
    清除临时代理设置。
    """
    os.environ.pop('https_proxy', None)
    os.environ.pop('http_proxy', None)
    os.environ.pop('all_proxy', None)
