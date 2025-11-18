pipeline {
    agent any

    environment {
        // Define the list of names to test
        NAMES_TO_TEST = "Sidd,Sanket,Parth"  // Add or modify names as needed
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                checkout scm
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
                        sh "python3 Test.py ${name}"
                    }
                }
            }
        }
    }
}
