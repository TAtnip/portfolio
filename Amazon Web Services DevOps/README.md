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



