
# Installation on Mac
brew install kubectl

# Installation on Linux

# Access service
http://192.168.0.12:8001/api/v1/proxy/namespaces/default/services/hello-minikube:8080/

# Commands on Linux
[Getting started](https://kubernetes.io/docs/getting-started-guides/minikube/)

Start minikube (takes a minute or so)

´´´
minikube start --logtostderr --vm-driver kvm 
minikube status

kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl expose deployment hello-minikube --type=NodePort

kubectl get pod
K8S_ADDR=192.168.0.12
K8S_NAME=hello-minikube
PORT=$(kubectl get svc $K8S_NAME -o json | jq .spec.ports[0].nodePort)
INSTANCE_URL="$K8S_ADDR:$PORT"
echo $INSTANCE_URL

minikube dashboard
kubectl proxy --address='0.0.0.0' --port=8001 --accept-hosts='^*$'

curl localhost:8080/api/v1/nodes

kubectl config set-cluster minikube --server=http://$K8S_ADDR:8001
kubectl config set-context tester --cluster=minikube --namespace=default --user=test
kubectl config use-context tester
kubectl config view



´´´

minikube --get-k8s-version
minikube docker-env
minikube dashboard
minikube ssh

minikube service hello-minikube --url
minikube stop

kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl expose deployment hello-minikube  --type=NodePort
kubectl get pod

curl $(minikube service hello-minikube --url)
kubectl delete deployment hello-minikube 

echo $DOCKER_TLS_VERIFY 
echo $DOCKER_HOST 



docker ps
eval $(

docker ps

kubectl get pods
kubectl get pods --context=minikube
kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl get pod
kubectl run hello-magnus --image=tutum/hello-world --port=80

kubectl expose deployment hello-magnus --type=NodePort


kubectl 
kubectl li
kubectl list
kubectl get pod
kubectl stop
kubectl top
kubectl top pod
kubectl delete deployment hello-minikube
kubectl delete deployment hello-magnus 

# Set up local docker registroy
```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

# Script to start docker from Kubejenkins


```
GERRIT_CHANGE_NUMBER=$(head -c 500 /dev/urandom | tr -dc 'a-z0-9' | fold -w 10 | head -n 1)
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

#update_consul "$INSTANCE_URL"
```


# Troubleshooting
### server gave HTTP response to HTTPS client
https://github.com/moby/moby/issues/28321
https://forums.docker.com/t/how-to-configure-docker-for-mac-in-configuration-files/25172/2


