# Understanding Linux Mechanism in Practice on Ubuntu Linux on Docker

## What's this repository?
[［試して理解］Linuxのしくみ～実験と図解で学ぶOSとハードウェアの基礎知識](https://gihyo.jp/book/2018/978-4-7741-9607-7) requires a Linux environment.  
I provide a Dockerfile to invoke commands and scripts in the book, even though the author **doesn't recommend** trying on virtual environments.  
This repository contains the following.
 - a Dockerfile to invoke commands in the book
 - scripts and summaries for each chapter
   - The author's repository is [here](https://github.com/satoru-takeuchi/linux-in-practice/).
   - visualization codes by Python
   - summaries including some console logs and figures

## Requirements
- a Docker environment
- Python, matplotlib, seaborn and pandas

## Setup
```bash
$ cd linux-mechanism-on-ubuntu-on-docker

# Build an image from a Dockerfile
$ docker image build -t linux-mechanism-on-ubuntu .

# Confirm linux-mechanism-on-ubuntu image's IMAGE ID
$ docker images

# To use strace, set "--cap-add SYS_PTRACE --security-opt seccomp:unconfined"
$ docker run -it --name linux-mechanism-on-ubuntu --cap-add SYS_PTRACE --security-opt seccomp:unconfined <IMAGE ID>

# Confirm the running container and send scripts in it
$ docker ps
$ docker cp scripts <CONTAINER ID>:/home

# Enter into the container
$ docker attach <CONTAINER ID>
```

## References
- [［試して理解］Linuxのしくみ～実験と図解で学ぶOSとハードウェアの基礎知識](https://gihyo.jp/book/2018/978-4-7741-9607-7)
- [Docker Tutorial](http://docs.docker.jp/get-started/toc.html)