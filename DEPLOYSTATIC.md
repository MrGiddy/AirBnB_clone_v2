# 0x03. AirBnB clone - Deploy static

# Concept - CI/CD
The lean/agile methodology (See: [Twelve Principles of Agile Software](https://agilemanifesto.org/principles.html)) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

* code
* ship your code
* measure the impact
* learn from it
* fix or improve it
* start over

As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).

Applied to software engineering, [CI/CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/) (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

* Shipping the code:
    * Capistrano, Fabric
* Encapsulating the code
    * Docker, Packer
* Testing the code
    * Jenkins, CircleCi, Travis
* Measuring the code
    * Datadog, Newrelic, Wavefront

# Background Context
Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your ```web_static``` work. You will use ```Fabric``` (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via ```sudo```) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

Before starting, please fork the repository ```AirBnB_clone_v2``` from your partner if you don’t have it

Resources
**Read or watch**:

* [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
* [How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)
* [Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html)
* [Nginx configuration for beginners](https://nginx.org/en/docs/beginners_guide.html)
* [Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)
* [Fabric for Python 3](https://github.com/mathiasertl/fabric)
* [Fabric Documentation](https://www.fabfile.org/)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What is Fabric
* How to deploy code to a server easily
* What is a tgz archive
* How to execute Fabric command locally
* How to execute Fabric command remotely
* How to transfer files with Fabric
* How to manage Nginx configuration
* What is the difference between root and alias in a Nginx configuration

## Requirements
## Python Scripts
Allowed editors: ```vi```, ```vim```, ```emacs```
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.0)
All your files should end with a new line
The first line of all your files should be exactly ```#!/usr/bin/python3```
A ```README.md``` file at the root of the folder of the project is mandatory
Your code should use the ```PEP 8``` style (version ```1.7.*```)
Your Fabric file must work with ```Fabric 3``` version ```1.14.post1``` (installation instruction below)
All your files must be executable
The length of your files will be tested using ```wc```
All your functions (inside and outside a class) should have documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## Bash Scripts
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A ```README.md``` file at the root of the folder of the project is mandatory
* All your Bash script files must be executable
* Your Bash script must pass ```Shellcheck``` (version ```0.3.3-1~ubuntu20.04.1``` via ```apt-get```) without any errors
* The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
* The second line of all your Bash scripts should be a comment explaining what is the script doing


# More Info
## Install Fabric for Python 3 - version 1.14.post1
```
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```

# Tasks
## 0. Prepare your web servers
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

* Install Nginx if it not already installed
* Create the folder ```/data/``` if it doesn’t already exist
* Create the folder ```/data/web_static/``` if it doesn’t already exist
* Create the folder ```/data/web_static/releases/``` if it doesn’t already exist
* Create the folder ```/data/web_static/shared/``` if it doesn’t already exist
* Create the folder ```/data/web_static/releases/test/``` if it doesn’t already exist
* Create a fake HTML file ```/data/web_static/releases/test/index.html``` (with simple content, to test your Nginx configuration)
* Create a symbolic link ```/data/web_static/current``` linked to the ```/data/web_static/releases/test/``` folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
* Give ownership of the ```/data/``` folder to the ```ubuntu``` user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
* Update the Nginx configuration to serve the content of ```/data/web_static/current/``` to ```hbnb_static``` (ex: ```https://mydomainname.tech/hbnb_static```). Don’t forget to restart Nginx after updating the configuration:
    * Use ```alias``` inside your Nginx configuration
    * [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

Your program should always exit successfully. **Don’t forget to run your script on both of your web servers**.

In optional, you will redo this task but by using Puppet
```
ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
ubuntu@89-web-01:~/$ echo $?
0
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$
```

# 1. Compress before sending
Write a Fabric script that generates a [.tgz](https://en.wikipedia.org/wiki/Tar_%28computing%29) archive from the contents of the ```web_static``` folder of your AirBnB Clone repo, using the function ```do_pack```.

* Prototype: ```def do_pack():```
* All files in the folder ```web_static``` must be added to the final archive
* All archives must be stored in the folder ```versions``` (your function should create this folder if it doesn’t exist)
* The name of the archive created must be ```web_static_<year><month><day><hour><minute><second>.tgz```
* The function ```do_pack``` must return the archive path if the archive has been correctly generated. Otherwise, it should return ```None```
```
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
Packing web_static to versions/web_static_20170314233357.tgz
[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
web_static/
web_static/.DS_Store
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170314233357.tgz -> 21283Bytes

Done.
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
-rw-rw-r-- 1 guillaume guillaume 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$
```
