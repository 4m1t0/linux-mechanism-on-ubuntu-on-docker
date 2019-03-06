FROM ubuntu
RUN apt-get -qq update
RUN apt-get install -y binutils build-essential python3 strace sysstat vim
COPY scripts /home