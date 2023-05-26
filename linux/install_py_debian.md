# 在Debian系統上安裝Python

檢查現有的python3版本
```python
ls -l /usr/bin/python*
```

先安裝編譯python必要的工具
```python
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev liblzma-dev
```

下載安裝檔，可在官網取得新版本下載連結，並解壓縮tar.xz
```python
wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tar.xz
tar -xf Python-3.11.3.tar.xz
cd Python-3.11.3
```

安裝Python 3.11，使用altinstall避免覆蓋現有的python(不建議覆蓋現有的python)
```python
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

修改預設python3路徑為python3.11
```python
sudo rm /usr/bin/python3
sudo ln -s /usr/local/bin/python3.11 /usr/bin/python3
```

檢查python3使用的版本
```python
python3 --version
```

安裝pip3
```python
sudo apt update
sudo apt install python3-pip
```