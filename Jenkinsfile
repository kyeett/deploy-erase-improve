pipeline {
  agent any
  environment {
    DISABLE_AUTH    = 'true'
    DB_ENGINE       = 'sqlite'
    K8S_PORT        = "8001"
    K8S_ADDR        = "192.168.0.12"
    PROJECT         = "webreview"
    DOCKER_REGISTRY = "192.168.0.11:5000"
  }
  stages {
    stage("Checkout") {
        steps {
            checkout scm
            sh """
            pwd
            ls -l
            env
            """
        }
    }
    stage("Build") {
        steps {
            sh '''#!/bin/bash
set -xe
DOCKER_IMAGE=$DOCKER_REGISTRY/$PROJECT:$GIT_COMMIT
env

echo "Image: $DOCKER_IMAGE"
echo "Start instance for trial"
docker build -t $DOCKER_IMAGE .
docker push $DOCKER_IMAGE
docker rmi -f $DOCKER_IMAGE | true

'''
        }
    }
    stage("Deploy") {
        steps {
            sh '''#!/bin/bash
                set -xe

                GERRIT_CHANGE_NUMBER=$(head -c 500 /dev/urandom | tr -dc 'a-z0-9' | head -c12)

                K8S_NAME=$PROJECT-$GIT_COMMIT
                K8S_URL="http://$K8S_ADDR:$K8S_PORT"
                DOCKER_IMAGE=$DOCKER_REGISTRY/$PROJECT:$GIT_COMMIT

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
