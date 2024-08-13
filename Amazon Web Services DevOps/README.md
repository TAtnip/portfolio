# Amazon Web Services DevOps Project

## Introduction
This project is an exercise in use of Amazon Web Services for production of an application. I seek to move a small XML Parser program written in python on a Linux EC2 instance to a Windows instance, each hosted on AWS, then move this program through Jenkins to create a build on my Sonatype Nexus repository.

## Architecture
![Architecturediagram](https://github.com/user-attachments/assets/3b4351fd-6f50-4966-905e-b13331ba2fa7)

## Technology Used
1. AWS
  - RedHat instance
  - Windows instance
3. Redhat Package Manager (RPM) to create a package with the build environment and configurations
4. PuTTY SSH client to access instances
5. Cygwin64 to compile my C++ program on the Windows instance
5. Jenkins to create my build and send to the Sonatype Nexus Repository
6. Sonatype Nexus Repository
7. GitHub

## AWS setup
![ec2instances](https://github.com/user-attachments/assets/f433736a-46e4-4587-a238-1d5882c02871)

This project involved the setup of both Linux and Windows EC2 instances. There was not necessarily a specific reason to do this besides for my own personal learning of how this might be done. For my configurations, I created both public and private routing tables, subnets, and a VPC. I had to research methods of connecting to my Linux unit especially, for which I found PuTTY. PuTTY is a very lightweight client that can be used to manage your keys and access instances. After connecting, I installed GCC to be able to create and test my XMLParser which was written in C++ and takes advantage of the Apache Xerces library: [XML Parser](https://github.com/TAtnip/portfolio/blob/b58f54633d42c99b53c6001a127cccd28fdc4eda/Amazon%20Web%20Services%20DevOps/test.cpp)

![linuxgcc](https://github.com/user-attachments/assets/6765bd9b-6bc6-4395-8c39-9b7a5dc968ed)

My files were moved between instances to the Windows machine using PuTTY's Secure Copy. I installed GCC and Cygwin64, a open-source Unix environment which can be run on Windows environments. On my windows machine, I then took advantage of Jenkins to create my build. Jenkins was configured to confirm with my GitHub repository on which I had uploaded the build commands and program for updates, then compile the program and create the build using Cygwin64 and lastly upload this to my Nexus repository. 

Notably, during this time, I ran into many issues due to storage space. I had initially configured my windows machine with ~15GB of space and minimal RAM. This proved to be far too little, as with all of the packages required my instance would consistently crash when attempting to create my build. I thus had to increase both storage and RAM. I also found it beneficial to access Jenkins on the Windows instance using my own personal computer by managing my security rules to create access. This helped work with the limited memory I had given myself. 

![jenkins build](https://github.com/user-attachments/assets/147fdc3a-11b0-423f-802a-e6475d7d2533)

![nexus repository](https://github.com/user-attachments/assets/c202b9a1-c714-4c61-a6d2-a66784ed55e7)






