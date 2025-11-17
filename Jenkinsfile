pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub
                git 'https://github.com/your-username/your-repository.git'
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
                sh 'python3 run_tests.py'
            }
        }
    }
}
