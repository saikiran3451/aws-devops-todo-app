# AWS DevOps To-Do Application

This project demonstrates a real-world AWS DevOps use case using:

- EC2
- Application Load Balancer (ALB)
- Nginx + Gunicorn
- Python Flask application
- Amazon RDS (MySQL)
- AWS Systems Manager Parameter Store
- IAM Roles
- Docker (containerization)

## Architecture Flow

Browser → ALB → Nginx → Gunicorn → Flask → RDS  
                                     ↳ SSM Parameter Store (secrets)

## Features

- Secure DB credentials via SSM
- No secrets in code
- Production-style deployment
- Ready for ECS/EKS migration

## Future Improvements

- Docker image pushed to ECR
- ECS Fargate deployment
- CI/CD pipeline
