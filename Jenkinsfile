pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub
                git 'https://github.com/ashish87566/Test-Repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any required dependencies, e.g., Python packages
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
