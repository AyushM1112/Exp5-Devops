pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Stage 1: Pulling latest code...'
                checkout scm
            }
        }

        stage('Environment Setup') {
            steps {
                echo 'Stage 2: Installing Python dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Start Application') {
            steps {
                echo 'Stage 3: Starting Python application...'
                bat 'start /B python app.py'
                sleep 5
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Stage 4: Running Selenium tests...'
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        always {
            echo 'Python Selenium testing completed.'
        }

        success {
            echo 'All Selenium tests passed successfully!'
        }

        failure {
            echo 'Selenium tests failed.'
        }
    }
}