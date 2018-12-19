# flask_app
#Pre-Requisite 
  1. ssh to a linux box with git client setup
  2. yum install -y docker
  3. usermod -a -G docker ec2-user # add ec2-user to docker group

#Steps to deploy the application
1. Download the source code zip file
2. Build the image with
 ``` 
 docker build -t my-flask-app .
 ```
 3. Start the container with
 ```
 docker run -d -p 5000:5000 my-flask-app
 ```
