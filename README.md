##Kivy UI framework installation on Raspberry Pi##

The Kivy framework allows developers to create touch-based graphical interfaces. 

**Kivy installation:**

1. Install dependencies first: *sudo apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
python-pygame python-setuptools libgstreamer1.0-dev git-core \
gstreamer1.0-plugins-{bad,base,good,ugly} \
gstreamer1.0-{omx,alsa} python-dev*
2. Install ‘cython’ (it may take up to 2 hours!): *sudo pip install cython* 
3. Finlly install kivy: *sudo pip install kivy*


**fbcp installation:**

1. cmake is neccessary to create make-file for compilation: *sudo apt-get install cmake* 
2. disable VNC in sudo rasp-config
3. download and build **fbcp: 
	*wget https://github.com/tasanakorn/rpi-fbcp
	*cd rpi-fbcp
	*mkdir build
	*cmake ..
	*make
4. to run fbcp, cd to **/home/pi/rpi-fbcp/build/ and and the executable with **./fbcp





 
