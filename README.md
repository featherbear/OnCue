<a href="http://featherbear.navhaxs.au.eu.org"><img src="https://raw.githubusercontent.com/bearbear12345/OnCue/documentation/graphics/banner.png" height="160px"/></a> by **[featherbear](http://featherbear.navhaxs.au.eu.org)**  
  
OnCue Projector is an easy to use multimedia presentation wrapper to facilitate the seamless playback of sequential content.  
Currently only supports Windows.

> **FYI:** This is my HSC major project for Software Design & Development

## Downloads
Version: 0.0.0.1-alpha  
*we'll see...*  

| [Installation Guide](https://github.com/bearbear12345/OnCue/raw/documentation/OnCue%20-%20Installation%20Guide.pdf) |  
| [User Manual](https://github.com/bearbear12345/OnCue/raw/documentation/OnCue%20-%20User%20Manual.pdf) |  
| [Troubleshooting](https://github.com/bearbear12345/OnCue/raw/documentation/OnCue%20-%20Troubleshooting.pdf) |  
| [Technical Manual](https://github.com/bearbear12345/OnCue/raw/documentation/OnCue%20-%20Technical%20Manual.pdf) |  


## Features
*???*

### TODO

#### Cross platform support

#### Stage Display
* Stage basher
* Stage countdown
* Stage timer
* Stage clock
* Colour & font

#### Remote
* DMX integration
* Web view & control
* Client / Server networking
### Current Bugs
*lol too many?*

## Development

### Stuff used to make this:

 * [Python](https://www.python.org/) `version 3.6.0 #41df79263a11`
 * [Qt](https://www.qt.io/) `version 5.8.0`
 * [PyWin32](https://sourceforge.net/projects/pywin32/) `build 221`
 * [PyQt](https://riverbankcomputing.com/software/pyqt/) `version 5.8.1`
 * [libVLC](http://www.videolan.org/vlc/libvlc.html) `version 2.2.5.1`
 * [vlc.py](https://wiki.videolan.org/Python_bindings/) `build Mon Mar 20 11:04:27 2017`

### Running
`$ helper/OnCue (Compile and Run).bat`  
*or*  
`$ source/OnCue.py`


### Building
*Ensure PyQt and PyWin32 are present on your system*

```
$ cd source  
$ python setup.py build
```
Executable will be found in *build/OnCue*

### Packaging the Installer
`$ helper/package.bat`


## License
OnCue Projector is licensed under the GNU General Public License v3.0.  
You are free to  redistribute it and/or modify it under the terms of the license.  
*For more details see the [LICENSE](https://raw.githubusercontent.com/bearbear12345/OnCue/master/LICENSE) file*
