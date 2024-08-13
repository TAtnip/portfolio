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
5. Jenkins
6. Sonatype Nexus Repository
7. GitHub

## AWS setup
![ec2instances](https://github.com/user-attachments/assets/f433736a-46e4-4587-a238-1d5882c02871)

This project involved the setup of both Linux and Windows EC2 instances. There was not necessarily a specific reason to do this besides for my own personal learning of how this might be done. I had to research methods of connecting to my Linux unit especially, for which I found PuTTY. PuTTY is a very lightweight client that can be used to manage your keys and access instances. After connecting, I installed GCC to be able to create and test my XMLParser which was written in Python.

![linuxgcc](https://github.com/user-attachments/assets/6765bd9b-6bc6-4395-8c39-9b7a5dc968ed)



