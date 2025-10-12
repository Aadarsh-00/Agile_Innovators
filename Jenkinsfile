pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'mywebapp:v1'   // Docker image name
        REGISTRY = ''                  // Add your Docker registry if needed
    }

    stages {

        stage('Checkout') {
            steps {
                // Checkout code from Git
                git branch: 'main', url: 'https://github.com/Aadarsh-00/Agile_Innovators'
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests inside a Python Docker container
                    docker.image('python:3.11').inside {
                        sh '''
                            pip install --upgrade pip
                            pip install flask
                            python -m unittest test_app.py
                        '''
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for your web app
                    docker.build(DOCKER_IMAGE, '.')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Optional: Run the image (for testing or deployment)
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
