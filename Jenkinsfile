pipeline {
    agent any

    environment {
        // Define the list of names to test
        NAMES_TO_TEST = "Sidd,John,Parth"  // Add or modify names as needed
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment and install dependencies (if any)
                    sh 'python3 -m venv venv'  // Create a Python virtual environment
                    sh '. venv/bin/activate && pip install -r requirements.txt'  // Install dependencies from requirements.txt
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Split the names into a list
                    def names = NAMES_TO_TEST.split(',')

                    // Loop through each name and run Test.py
                    names.each { name ->
                        // Run the Test.py script for each name
                        sh ". venv/bin/activate && python3 Test.py ${name}"
                    }
                }
            }
        }
    }
}
