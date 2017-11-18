pipeline {
  agent any
  environment {
    DISABLE_AUTH = 'true'
    DB_ENGINE    = 'sqlite'
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
env
DOCKER_URL="armdocker.rnd.ericsson.se"
IMAGE_SHORTNAME="proj_btmoduleci/reviewaid"
IMAGE=$DOCKER_URL/$IMAGE_SHORTNAME:$GERRIT_CHANGE_NUMBER

echo "Event: $GERRIT_EVENT_TYPE"
echo "Image: $IMAGE"

if [ "$GERRIT_EVENT_TYPE" == "patchset-created" ]
then
    echo "Start instance for trial"
    docker build -t $IMAGE .
    docker push $IMAGE
elif [ "$GERRIT_EVENT_TYPE" == "change-merged" ]
then
    echo "merged"
    docker rmi -f $IMAGE
    echo "now build latest and submitted"
    LATEST_IMAGE=$DOCKER_URL/$IMAGE_SHORTNAME:latest
    docker build --no-cache --force-rm -t $LATEST_IMAGE .
    docker push $LATEST_IMAGE
    docker rmi -f $LATEST_IMAGE
else
    echo "Abort ? or others"
    docker rmi -f $IMAGE | true
fi
'''
        }
    }
    stage("Deploy") {
        steps {
            sh '''#!/bin/bash
                set -xe

                GERRIT_CHANGE_NUMBER=$(head -c 500 /dev/urandom | tr -dc 'a-z0-9' | head -c12)
                PROJECT=webreview
                K8S_NAME=$PROJECT-$GERRIT_CHANGE_NUMBER
                K8S_PORT=8001
                K8S_ADDR=192.168.0.12
                K8S_URL="http://$K8S_ADDR:$K8S_PORT"
                DOCKER_IMAGE=flask-trial
                DOCKER_REGISTRY=192.168.0.11:5000

                echo "Set up connection with minikube cluster"
                kubectl config set-cluster minikube --server=$K8S_URL

                echo "Start deploy to kubernetes"
                kubectl run $K8S_NAME --image-pull-policy="Always" --image=$DOCKER_REGISTRY/$DOCKER_IMAGE --port=8080
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
