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
    stage("Deploy") {
        steps {
            sh '''#!/bin/bash

                GERRIT_CHANGE_NUMBER=$(head -c 500 /dev/urandom | tr -dc 'a-z0-9' | fold -w 10 | head -n 1)
                PROJECT=webreview
                K8S_NAME=$PROJECT-$GERRIT_CHANGE_NUMBER
                K8S_PORT=8001
                K8S_ADDR=192.168.0.12
                K8S_URL="http://$K8S_ADDR:$K8S_PORT"
                DOCKER_IMAGE=gcr.io/google_containers/echoserver:1.4

                echo "Set up connection with minikube cluster"
                kubectl config set-cluster minikube --server=$K8S_URL

                echo "Start deploy to kubernetes"
                kubectl run $K8S_NAME --image-pull-policy="Always" --image=$DOCKER_IMAGE --port=8080
                kubectl expose deploy $K8S_NAME --type=NodePort
                SERVICE_URL=$K8S_URL/api/v1/proxy/namespaces/default/services/$K8S_NAME:8080/

                echo "please access $SERVICE_URL"

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
