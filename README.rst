====================
FTB Modpack Info API
====================

A small Python module for getting current information about Feed The Beast
modpacks.

I wrote this module to help keep the modpacks on my FTB server up to date. 
Included in the returned information is the modpack name, description, current
version, and server download URL. Also included are URLs to a modpack icon, 
splash image, and sometimes a large panel image. I would like to use these in 
making a nifty server management web portal in the future. For other details you
can just look at the code. It's very brief.

The only external package needed is ``requests``.
