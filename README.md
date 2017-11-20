# raspi_framebuffer


Kivy install 

1. install dependencies: sudo apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
python-pygame python-setuptools libgstreamer1.0-dev git-core \
gstreamer1.0-plugins-{bad,base,good,ugly} \
gstreamer1.0-{omx,alsa} python-dev
2. install ‘cython’ (it may take up to 2 hours!): sudo pip install cython 
3. install kivy: sudo pip install kivy


fbcp install

1. sudo apt-get install cmake 
2. disable VNC (sudo rasp-config)
3. download and build ‘fbcp’: 
	wget https: github.com/tasanakorn/rpi-fbcp
	cd rpi-fbcp
	mkdir build
	cmake ..
	make
4. daemonize ‘fbcp’





 
