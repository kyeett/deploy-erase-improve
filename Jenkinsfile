pipeline {
  agent any
  stages {
    stage("Checkout") {
        steps {
            checkout scm
            sh """
            pwd
            ls -l
            """
        }
        steps {
            echo "Another step"
        }
    }
    stage("Build") {
        steps {
            sh '''#!/bin/bash
            set -xe
            env

            echo "Number: $GERRIT_CHANGE_NUMBER"
            echo "Event: $GERRIT_EVENT_TYPE"

            '''
        }
    }
    stage('Stuff completed') {
      steps {
        echo 'All done'
      }
    }
  }
  triggers {
    pollSCM('*/2 * * * *')
  }
}
