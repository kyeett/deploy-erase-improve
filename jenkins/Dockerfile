FROM jenkinsci/blueocean:latest

ENV HOME=/config

USER root

# Install kubectl
# Note: Latest version may be found on:
# https://aur.archlinux.org/packages/kubectl-bin/
ADD https://storage.googleapis.com/kubernetes-release/release/v1.6.4/bin/linux/amd64/kubectl /usr/local/bin/kubectl

RUN set -x && \
    apk add --no-cache curl ca-certificates && \
    chmod +x /usr/local/bin/kubectl && \
    \
    # Create non-root user (with a randomly chosen UID/GUI).
    adduser kubectl -Du 2342 -h /config && \
    \
    # Basic check it works.
    kubectl version --client

RUN kubectl config set-context tester --cluster=minikube --namespace=default --user=test
RUN kubectl config use-context tester
RUN kubectl config view
RUN chmod 777 -R $HOME/

# Install jq and docker
RUN apk update \
 && apk add jq \
# && apk add docker \
 && apk add openrc \
 && apk add curl \
 && apk add alpine-sdk \
 && rm -rf /var/cache/apk/*

#RUN rc-update add docker boot

# https://forums.docker.com/t/how-can-i-run-docker-command-inside-a-docker-container/337/7
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz && \
            tar --strip-components=1 -xvzf docker-17.03.1-ce.tgz -C /usr/local/bin

RUN chown -R jenkins:jenkins /var/run/docker.sock

#RUN sleep 10
#RUN service docker start#
#RUN sleep 10
#RUN docker ps

USER jenkins
