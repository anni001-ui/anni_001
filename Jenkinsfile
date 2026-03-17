pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install pandas pytest
                '''
            }
        }

        stage('AI Test Prioritization') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python ai_prioritize.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests/
                '''
            }
        }
    }
}
