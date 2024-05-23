# setup.py
from setuptools import setup, find_packages

setup(
    name="temp_proxy",
    version="0.1",
    packages=find_packages(),
    description="A package to set temporary proxy",
    author="Jerry Lu",
    author_email="280215476@qq.com",
    # url="https://github.com/yourusername/temp_proxy",  # 如果有GitHub仓库的话
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
