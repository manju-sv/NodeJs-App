Official Node.js Image: Used an official Node.js image from Docker Hub as the base image. In this case, we're using Node.js version 14, which is a Long-Term Support (LTS) version.

Set Working Directory: We set the working directory inside the container to /app to keep the code and application-related files organized.

Copy Package Files: We copy the package.json and package-lock.json files into the container separately. This allows Docker to cache the dependencies installation step separately from the application code, which is more efficient.

Install Dependencies: We run npm install --production to install the application dependencies. The --production flag ensures that only production dependencies are installed, which reduces the image size and potential security risks.

Copy Application Code: We copy the rest of the application code into the container. This includes all the application files and source code.

Expose Port: We use the EXPOSE instruction to document that the container listens on port 5000. This is the port that the Node.js application typically runs on.

Define CMD: We define the command that will be executed when the container starts. In this case, it's npm start, which is a common command to start a Node.js application.

To build a Docker image from this Dockerfile, navigate to the directory containing the Dockerfile and run the following command:

docker build -t node-js-getting-started .

This command will build a Docker image named "node-js-getting-started" based on the Dockerfile. You can then run a container from the image using docker run

=========================================================================================

Here's an explanation of this docker-compose.yml file:

Node.js Application (nodejs-app):

It builds the Node.js application from the ./node-js-getting-started directory.
Forwards port 5000 from the container to the host for accessing the Node.js app.
Depends on the Loki service for log collection.
Uses the Loki driver for logging and specifies the Loki URL for log forwarding.
Loki (loki):

Uses the official Grafana Loki image.
Exposes port 3100 for accessing Loki's web interface.
Mounts a local directory (./loki-config) containing Loki configuration files.
Specifies the command to use a custom configuration file.
Promtail (promtail):

Uses the official Grafana Promtail image.
Mounts a local directory (./promtail-config) containing Promtail configuration files.
Specifies the command to use a custom configuration file.
Grafana (grafana):

Uses the official Grafana image.
Exposes port 3000 for accessing Grafana's web interface.
Depends on the Loki service for log data.
Sets environment variables to install the Grafana Loki datasource plugin.
Mounts a local directory (./grafana-config) containing Grafana configuration files.
Before running this Docker Compose setup, make sure you have the following directory structure:

- Project_Directory/
  - docker-compose.yml
  - node-js-getting-started/ (Node.js application code and Dockerfile)
  - loki-config/ (Loki configuration files)
  - promtail-config/ (Promtail configuration files)
  - grafana-config/ (Grafana configuration files)

To start the services, navigate to your project directory and run:


docker-compose up

Once the services are running, you can access the Node.js application at 
http://localhost:5000, 
Loki : http://localhost:3100, 
Grafana : http://localhost:3000.  
need to configure Grafana with Loki as a data source to visualize the logs collected by Promtail and stored in Loki.

=====================================================================================
This script will print numbers from 0 to 100, and when it reaches a multiple of 10, it will print the wordy version of that number.

Output is as folows.

 % python3 num.py
0
1
2
3
4
5
6
7
8
9
ten
11
12
13
14
15
16
17
18
19
twenty
21
22
23
24
25
26
27
28
29
thirty
31
32
33
34
35
36
37
38
39
forty
41
42
43
44
45
46
47
48
49
fifty
51
52
53
54
55
56
57
58
59
sixty
61
62
63
64
65
66
67
68
69
seventy
71
72
73
74
75
76
77
78
79
eighty
81
82
83
84
85
86
87
88
89
ninety
91
92
93
94
95
96
97
98
99
one hundred















