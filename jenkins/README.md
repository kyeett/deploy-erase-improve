

# Commands used set up Jenkins with kubectl 
Build Jenkins + kubectl
```
> pwd
jenkins
> docker build -t kubejenkins .

```

Start Jenkins
```
export K8S_ADDR=192.168.0.12:8001

docker run  -p 49001:8080 \
            -v ~/jenkins_home/:/var/jenkins_home:z \
            -e K8S_ADDR=$K8S_ADDR \
            --name kubejenkins \
            -t kubejenkins:latest
```

For macOS
```
greadlink -f $(which kubectl)
```
For Linux
```
readlink -f $(which kubectl)
```

# Set up consul

### Create directory for persistent data

```
mkdir /var/db/consul/data 
```
(for example)

Might need to change persmissions for directory as well as add directory for docker mounting (see error msges).

```
docker run \
--rm \
-d \
-p 8500:8500 \
--name deploy-consul \
-v /private/var/db/consul/data:/consul/data \
consul agent -dev -client=0.0.0.0 -bind=0.0.0.0
```
