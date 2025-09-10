pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install required Python packages
                bat 'pip install selenium pandas'
            }
        }

        stage('Run Python Files') {
            steps {
                // Run your Python scripts
                bat 'python NestedframeFunc1.py'
                bat 'python NestedframeFunc2.py'
            }
        }
    }
}
