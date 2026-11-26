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
                ssh -o StrictHostKeyChecking=no root@devops-controller "
                cd /root/devops-project &&
                ansible-playbook -e release_version=${BUILD_NUMBER} -i /root/devops-lab/hosts.ini playbooks/deploy.yml
                "
                '''
            }
        }
    }
}
