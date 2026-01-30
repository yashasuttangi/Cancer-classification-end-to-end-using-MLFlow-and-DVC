# Cancer-classification-end-to-end-using-MLFlow-and-DVC
End to End ML project with deployment on AWS using ML Flow and DVC.

## Workflows 
1. Update config.yaml file
2. Update secrets.yaml file 
3. Update params.yaml file
4. Update the entity 
5. Update the configuration manager in src config 
6. Update the components 
7. Update the pipeline 
8. Update the main.py 
9. Update the dvc.yaml file 


## AWS CI/CD Deployment with GitHub Actions 

### Overall flow of deployment:
- Build docker img of the src code 
- push your docker image to ECR 
- Launch your EC2 
- Pull your image from ECR in EC2  
- Launch the docker image in EC2

### Step 1: 
1. Login to AWS Console 
2. Create IAM User for deployment 
    Access policy for the user: 
        - AmazonEC2ContainerRegistryFullAccess
        - AmazonEC2FullAccess

### Step 2:
Create ECR repo to store/save docker image 

### Step 3: 
Create EC2 Machine (Ubuntu)

### Step 4:
Open EC2 and install Docker in EC2 machine
```
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

### Step 5:
Open EC2 and install docker in EC2 machine. 

#### Configure EC2 as self-hosted runner 
```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

### Finally, setup github secrets
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```
