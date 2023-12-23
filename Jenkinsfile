pipeline {
    agent {
      dockerfile {
        filename 'Dockerfile'
      }
    }
    parameters {
        choice choices: ['hoge', 'fuga'], description: 'ログインするユーザーID', name: 'USERNAME'
    }
    stages {
      stage('Generate OTP'){
        steps {
          script {
            sh "echo ${USERNAME}"
            withCredentials([
                string(
                  credentialsId: "2FA_${USERNAME}", 
                  variable: 'secret')]) {
              def result = sh script: 'python totp_gen.py ${secret} || echo error', returnStdout: true
              currentBuild.displayName = "${result} : ${USERNAME}"
            }
          }
        }
      }
    }
}
