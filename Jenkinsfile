pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source Code Checkout'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                   ansible-playbook \
                   -i inventory/hosts.ini \
                   playbooks/deploy.yml
                '''
            }
        }

    }

}
