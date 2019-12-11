sudo apt-get update
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3-pip
sudo python3.7 -m pip install pip
sudo python3.7 -m pip install scikit-learn
sudo python3.7 -m pip install scikit-image
sudo mkdir -p /users/geni
cd /users/geni
wget https://github.com/yizheshexin/CS655GeniProject/blob/master/server_final.py
nohup python3.7 server_final.py &