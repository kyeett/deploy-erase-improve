node {
    stage("Checkout") {
        checkout scm
        sh """
        pwd
        ls -l
        """
    }
    stage("Build") {
        sh '''#!/bin/bash
set -xe
env
'''
    }
}
