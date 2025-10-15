 CI/CD Pipeline for a Simple Web Application

 Project Overview
We built a CI/CD pipeline using Jenkins to automate the deployment of a Python Flask web application inside a Docker container. We learned how to use version control, automated testing, containerization, and continuous integration and deployment.

 Objective
We aimed to set up a CI/CD pipeline with automated testing and deployment using Jenkins, Docker, and GitHub.

Tools Used
We used Git, GitHub, Jenkins, Docker, Python, and Flask throughout the project.

Time Estimate
We completed the project in one week including setup, coding, testing, and pipeline configuration.

Deliverables
We submitted a GitHub repository containing app.py, test_app.py, Dockerfile, Jenkinsfile, and README.md. We also delivered a working Jenkins pipeline that deployed the Flask app automatically.

Steps and Process
We first created a GitHub repository and initialized it with a README and a Python .gitignore file.  
We cloned the repository to our local system for development.  
We created a simple Flask application file named app.py to display a basic message.  
We added a requirements.txt file to specify necessary Python dependencies.  
We wrote test_app.py to perform unit testing on our Flask route.  
We created a Dockerfile to containerize the application and ensure consistent deployment environments.  
We set up Jenkins using Docker and installed required plugins such as Git, Docker, and Pipeline.  
We created a Jenkinsfile that defined different stages for checkout, testing, building the Docker image, and deployment.  
We connected Jenkins to our GitHub repository and configured it to trigger the pipeline automatically when new code was pushed.  
We tested the entire pipeline and verified successful deployment by visiting the running Flask app on the local host.  
Finally, we documented all steps clearly in this README file for easy understanding and reproduction.

Outcomes
We successfully implemented an automated CI/CD pipeline that builds, tests, and deploys a simple Flask application using Jenkins and Docker. This project helped us understand the complete DevOps workflow and the importance of automation in modern software development.


