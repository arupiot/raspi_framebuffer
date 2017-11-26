## Kivy UI framework installation on Raspberry Pi

The Kivy is an open-source Python library and framework for developing multitouch applications. 

**Kivy installation:**

1. Install dependencies first: *sudo apt-get -y install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
python-pygame python-setuptools libgstreamer1.0-dev git-core \
gstreamer1.0-plugins-{bad,base,good,ugly} \
gstreamer1.0-{omx,alsa} python-dev*
2. Install ‘cython’ (it may take up to 2 hours!): *sudo pip install cython* 
3. Finally install kivy: *sudo pip install kivy*
4. Make sure the installation was succesfull, type *kivy* and then *import kivy* (see sample output)

```
~> kivy
Python 2.7.10 (default, Jul 15 2017, 17:16:57) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import kivy
[INFO   ] [Logger      ] Record log in /Users/alkopop79/.kivy/logs/kivy_17-11-26_17.txt
[INFO   ] [Kivy        ] v1.10.0
[INFO   ] [Python      ] v2.7.10 (default, Jul 15 2017, 17:16:57) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)]
>>>
```


**fbcp installation:**

1. cmake is neccessary to create make-file for compilation: *sudo apt-get install cmake* 
2. disable VNC in sudo rasp-config
3. download and build **fbcp**: 
	*wget https://github.com/tasanakorn/rpi-fbcp
	
	cd rpi-fbcp
	
	mkdir build
	
	cmake ..
	
	make*
	
4. to run fbcp, *cd /home/pi/rpi-fbcp/build/*,  then run executable with *./fbcp*





 
