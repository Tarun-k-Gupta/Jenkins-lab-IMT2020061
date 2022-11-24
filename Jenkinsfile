pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Tarun-k-Gupta/Jenkins-lab-IMT2020061.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x function.py"
                sh "./function.py"
            }
        }
     stage('Pass_Test Code') {
            steps {
                sh "chmod u+x pass.py"
                sh "./pass.py"
            }
        }
     stage('Fail_Test Code') {
            steps {
                sh "chmod u+x fail.py"
                sh "./fail.py"
            }
        }
    } 
}