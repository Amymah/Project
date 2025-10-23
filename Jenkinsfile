pipeline {
agent any

```
stages {
    stage('Check Python') {
        steps {
            bat 'python --version'
        }
    }

    stage('Install Dependencies') {
        steps {
            // Install all required Python packages
            bat 'pip install -U selenium pandas webdriver-manager'
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
```

}
