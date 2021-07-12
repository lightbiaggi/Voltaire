#!/bin/bash
apt update -y
apt upgrade
#python-apt is needed for running the script so I keep it
apt install python-apt build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev -y

mkdir python_installation && cd python_installation

wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
rm -f Python-3.7.2.tgz

cd Python-3.7.2
./configure --enable-optimizations
make -j 4
make altinstall

cd ../..
rm -rf python_installation

apt --purge remove build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev -y
apt autoremove -y
apt clean


