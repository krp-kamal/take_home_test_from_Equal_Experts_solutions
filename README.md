# Equal Experts - Home_Test - Solution

## Submission guidelines
Do

Provide a README file in text or markdown format that provides a concise way to setup and run the provided solution.

Take the time to read any applicable API or service docs, it may save you significant effort

Make your solution simple and clear. We aren't looking for overly complex ways to solve the problem since in our experience simple, clear solutions to problems are also generally the most maintainable and extensible solutions.

Provide your solution in a zip or compressed tar archive.

## Exercises

## $\colorbox{white}{{\color{blue}{Mini\ Kube}}}$

Write a simple hello world application in any one of these languages: Python, Ruby, Go. Build the application within a Docker container and then load balance the application within Minikube. You are not required to automate the installation of Minikube on the host machine.


### Build sample application using Python Flask

The "Hello World" application gives output with content "Hello World from <<IP>> The main objective is to demonstrate the load balance functionality using service manifest. The page output will display and change IP of the pod for each page refresh.

## Docker Registry

To have public access to docker image, created public repository in [DockerHub](https://hub.docker.com/repository/docker/kamalperumal/hello_world/general)

## Docker command to build and push the image.
```docker build -t kamalperumal/hello_world:v0.0.1 .```

```docker run   -p 8080:8080 kamalperumal/hello_world:v0.0.2``` 

```docker push kamalperumal/hello_world:v0.0.1```

## Docker Scan

### Actual command executed to scan the docker image
```docker run --rm -v $HOME/Library/Caches:/root/.cache/ -v /Users/kamalperumal/Documents/project_2023/equal_experts/silaco_sample/take_home_test_from_Equal_Experts_solutions/docker_scan:/scan aquasec/trivy:0.18.3 image --format template --template "@contrib/html.tpl" -o /scan/report.html kamalperumal/hello_world:v0.0.2```

Sample output attached ./take_home_test_from_Equal_Experts_solutions/docker_scan/report.html

### PATH needs to be changed in scan command 
```docker run --rm -v $HOME/Library/Caches:/root/.cache/ -v <<specify user path>>:/scan aquasec/trivy:0.18.3 image --format template --template "@contrib/html.tpl" -o /scan/report.html kamalperumal/hello_world:v0.0.2```

## Minikube Setup

Please use the below link to setup minikube based on the OS [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### Command to start minikube
```minikube start ee_hometest_001```

### Command to start minikube
### Command to deploy application in default namespace 
```kubectl create -f deployment.yaml```

### Command to deploy Service in default namespace 

The service deployment takes care of both load balance of the pods and expose application locally

```kubectl create -f service.yaml```

### Command to display Services list in minikube```minikube service --all```

Sample output of the services

"exampleservice" URL can be used to expose the sample "Hello world" application
URL: http://127.0.0.1:50431 

| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | ee-helloworld  |        8080 | http://192.168.49.2:30002 |
| default   | kubernetes |             | No node port |
😿  service default/kubernetes has no node port
🏃  Starting tunnel for service ee-helloworld.
🏃  Starting tunnel for service kubernetes.
<br/>

| NAMESPACE |      NAME      | TARGET PORT |          URL           |
|-----------|----------------|-------------|------------------------|
| default   | ee-helloworld  |             | http://127.0.0.1:50431 |
| default   | kubernetes     |             | http://127.0.0.1:50433 |
