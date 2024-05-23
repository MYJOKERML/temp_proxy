### 使用方法文档

# temp_proxy

`temp_proxy`是一个用于设置和清除临时代理的Python包。

## 安装

你可以通过以下命令安装这个包：

```sh
git clone https://github.com/MYJOKERML/temp_proxy.git && cd temp_proxy
pip install .
```

## 使用方法

### 1. 设置临时代理

`set_temp_proxy(mixedPort)`函数用于设置临时代理。

#### 参数：
- `mixedPort` (int): 代理端口号。

#### 示例：

```python
from temp_proxy import set_temp_proxy

# 设置临时代理，代理端口为1080
set_temp_proxy(1080)
```

设置临时代理后，HTTP、HTTPS和SOCKS5请求将通过指定端口的代理服务器进行。

### 2. 清除临时代理

`clear_temp_proxy()`函数用于清除临时代理设置。

#### 示例：

```python
from temp_proxy import clear_temp_proxy

# 清除临时代理
clear_temp_proxy()
```

在代码运行结束后调用此函数，以确保清除代理设置。

## 完整示例

以下是一个完整的示例，展示如何设置和清除临时代理：

```python
from temp_proxy import set_temp_proxy, clear_temp_proxy

# 设置临时代理，代理端口为1080
set_temp_proxy(1080)

# 这里可以添加需要通过代理执行的代码
# 例如，发送HTTP请求等

# 清除临时代理
clear_temp_proxy()
```

## 函数详细说明

### set_temp_proxy

```python
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
```

此函数通过设置环境变量`https_proxy`、`http_proxy`和`all_proxy`来配置临时代理。

### clear_temp_proxy

```python
def clear_temp_proxy():
    """
    清除临时代理设置。
    """
    os.environ.pop('https_proxy', None)
    os.environ.pop('http_proxy', None)
    os.environ.pop('all_proxy', None)
```

此函数通过删除环境变量`https_proxy`、`http_proxy`和`all_proxy`来清除临时代理设置。

## 注意事项

- 代理设置仅在当前Python进程中生效，不会影响系统的全局设置。
- 确保在代码运行结束后调用`clear_temp_proxy`函数，以清除代理设置，避免对后续代码的影响。
