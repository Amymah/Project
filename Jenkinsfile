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
                bat 'NestedframeFunc1.py'
                bat 'NestedframeFunc2.py'
                bat 'SwitchingWindows.py'
            }
        }
    }
}
