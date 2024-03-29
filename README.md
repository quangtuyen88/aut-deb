1.

requirement :

```
sudo apt-get install dpkg-dev devscripts python3-setuptools python3-pip git

```
2. build deb :

```
dpkg-buildpackage -us -uc

```

This will create a Debian package named aut_1.0_all.deb in the parent directory.



Tested on Ubuntu 22.04 : 

```
dpkg -i aut_0.4.0_all.deb
Selecting previously unselected package aut.
(Reading database ... 57787 files and directories currently installed.)
Preparing to unpack aut_0.4.0_all.deb ...
Unpacking aut (0.4.0) ...
Setting up aut (0.4.0) ...
Collecting git+https://github.com/autonity/aut.git
  Cloning https://github.com/autonity/aut.git to /tmp/pip-req-build-876w86jt
  Running command git clone --filter=blob:none --quiet https://github.com/autonity/aut.git /tmp/pip-req-build-876w86jt
  Resolved https://github.com/autonity/aut.git to commit ce7e34cc92a34572fe88cc9f03c4c01d5dc120a8
  Running command git submodule update --init --recursive -q
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting autonity==3.0.0
  Downloading autonity-3.0.0-py3-none-any.whl (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.3/44.3 KB 1.6 MB/s eta 0:00:00
Collecting click==8.1.3
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 KB 6.0 MB/s eta 0:00:00
Collecting typing-extensions
  Downloading typing_extensions-4.10.0-py3-none-any.whl (33 kB)
Collecting web3==6.14.0
  Downloading web3-6.14.0-py3-none-any.whl (1.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 54.0 MB/s eta 0:00:00
Collecting pyunormalize>=15.0.0
  Downloading pyunormalize-15.1.0.tar.gz (515 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 515.5/515.5 KB 42.8 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting eth-utils>=2.1.0
  Downloading eth_utils-4.0.0-py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.7/77.7 KB 12.2 MB/s eta 0:00:00
Collecting jsonschema>=4.0.0
  Downloading jsonschema-4.21.1-py3-none-any.whl (85 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.5/85.5 KB 15.1 MB/s eta 0:00:00
Collecting lru-dict<1.3.0,>=1.1.6
  Downloading lru_dict-1.2.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Collecting eth-abi>=4.0.0
  Downloading eth_abi-5.0.1-py3-none-any.whl (29 kB)
Collecting protobuf>=4.21.6
  Downloading protobuf-5.26.0-cp37-abi3-manylinux2014_x86_64.whl (302 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 302.8/302.8 KB 37.3 MB/s eta 0:00:00
Collecting eth-typing>=3.0.0
  Downloading eth_typing-4.0.0-py3-none-any.whl (14 kB)
Requirement already satisfied: requests>=2.16.0 in /usr/lib/python3/dist-packages (from web3==6.14.0->autonity==3.0.0->aut==0.4.0) (2.25.1)
Collecting eth-hash[pycryptodome]>=0.5.1
  Downloading eth_hash-0.7.0-py3-none-any.whl (8.7 kB)
Collecting aiohttp>=3.7.4.post0
  Downloading aiohttp-3.9.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
  ....
====
check version 
 aut --version
aut, version 0.4.0
```

