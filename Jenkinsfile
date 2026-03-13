pipeline {
    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install pandas pytest
                '''
            }
        }

        stage('AI Test Prioritization') {
            steps {
                sh '''
                source venv/bin/activate
                python ai_prioritize.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest tests/
                '''
            }
        }
    }
}
