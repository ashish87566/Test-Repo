pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ashish87566/Test-Repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create and activate virtual environment
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate '
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the Python script within the virtual environment
                    sh '. venv/bin/activate && python3 input_script.py'
                }
            }
        }
    }
}
