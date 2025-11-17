pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub on the correct branch
                git branch: 'main', url: 'https://github.com/ashish87566/Test-Repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any required dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run the Python script
                sh 'python3 input_script.py'
            }
        }
    }
}
