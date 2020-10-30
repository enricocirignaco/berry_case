FROM berrycaseapp:nocmd
#FROM ubuntu:latest

RUN apt update -y; apt upgrade -y
RUN apt install gcc-arm-none-eabi -y
RUN apt install make cmake -y
WORKDIR /project
CMD [ "make" ]
