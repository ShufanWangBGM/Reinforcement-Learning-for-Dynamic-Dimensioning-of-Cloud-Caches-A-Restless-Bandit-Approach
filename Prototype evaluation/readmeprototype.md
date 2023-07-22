# Usages about Prototype and ATS

Before using, please download ATS [here](https://doi.org/10.5281/zenodo.6543551). To implement installation, please follow below steps:

# 1. Installation
## install dependencies
```
sudo apt-get update

sudo snap install cmake --classic

sudo apt install -y make git build-essential libboost-all-dev python3-pip parallel libprocps-dev

sudo apt-get install -y libssl-dev libsasl2-dev flex libcap-dev libncurses5-dev pkg-config

sudo apt install libhwloc-dev libhwloc5 libunwind8 libunwind8-dev google-perftools

sudo apt install autoconf automake autotools-dev bison debhelper dh-apparmor flex gettext intltool-debian libbison-dev libcap-dev libexpat1-dev libfl-dev libpcre3-dev libpcrecpp0v5 libsigsegv2 libsqlite3-dev libssl-dev libtool m4 po-debconf tcl-dev tcl8.6-dev zlib1g-dev
```

## (a) Install Prototype

## install openjdk 1.8.
```
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install -y openjdk-8-jdk
```

Go to the prototype path
```
cd ./prototype
```

## install LightGBM
```
cd lib/LightGBM-eloiseh/build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
sudo make install
cd ../../..
```

## install mongo c
```
cd lib/mongo-c-driver-1.13.1/cmake-build/
cmake -DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF ..
make
sudo make install
cd ../../..
```

## install mongo-cxx
```
cd lib/mongo-cxx-driver-r3.4.0/build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local ..
sudo make
sudo make install
cd ../../..
```

## install libbf
```
cd lib/libbf-dadd48e/build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
sudo make install
cd ../../..
```

## install the library with API
```
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
sudo make install
sudo ldconfig
cd ..
```

## (b) Install Trafficserver (ATS)
```
cd ./trafficserver-8.0.3
autoreconf -if
make clean
./configure --prefix=/opt/ts
make
sudo make install
```

# 2. Configure ATS

## usages:
- ATS configuration files can be found in "/opt/ts/etc/trafficserver/"
- Modify corresponding files according to the configurations in folder "./tsconfigs", do not simply replace the configuration files by that in "./tsconfigs"
- "Ram Cache" is configured in the 129 line of "records.config"
- "Disk Cache" is configured in "storage.config"
- Caching algorithm is configured in the line 131 of "records.config", and the following means "Unmodified ATS":
```
CONFIG proxy.config.cache.vdisk_cache.algorithm STRING
```
- In terminal, using "sudo su" to enter root mode, below commands are necessary：
```
/opt/ts/bin/trafficserver start    # start ATS
/opt/ts/bin/trafficserver restart    #r estart ATS  
/opt/ts/bin/trafficserver stop    # stop ATS
/opt/ts/bin/traffic_top    # show ATS panel
```
- Aftering running ATS, "Record.log" can be found in "/opt/ts/var/log/trafficserver/", which records requests and responses information 

# 3. Others
- Prototype codes can be found in folders "./prototype/src/caches/" and "./prototype/include/webcachesim/caches/".
