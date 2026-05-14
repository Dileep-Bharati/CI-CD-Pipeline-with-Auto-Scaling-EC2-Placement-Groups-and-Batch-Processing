# Project 2 — CI/CD Pipeline with Docker, GitHub Actions, ECR & SQS

## Architecture
- Flask Web App containerized with Docker
- GitHub Actions CI/CD pipeline
- Docker images pushed to AWS ECR
- EC2 instances in Cluster Placement Group
- SQS queue for batch job processing
- Batch Worker in Spread Placement Group
- CloudWatch monitoring and logging

## Services Used
EC2 | ECR | Docker | GitHub Actions | SQS | S3 | CloudWatch | IAM | ALB | ASM | SSM

## CI/CD Flow
1. Developer pushes code to GitHub main branch
2. GitHub Actions triggers automatically
3. Runs Python tests (pytest)
4. Builds Docker image
5. Pushes to AWS ECR
6. Deploys to EC2 via SSM
7. SNS notification on success/failure

## Project Structure
project2/
├── webapp/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
├── batch-worker/
│   ├── batch_worker.py
│   ├── requirements.txt
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md

## Key Features
- Zero downtime rolling deployment
- EC2 Placement Groups for optimized instance placement
- SQS batch processing with Dead Letter Queue
- CloudWatch monitoring with automated alarms
- IAM least-privilege security throughout

## What I Learned
- Built complete CI/CD pipeline from scratch
- Containerized Python application with Docker
- Managed Docker images in AWS ECR
- Configured EC2 Placement Groups for performance
- Implemented SQS batch processing with DLQ
- Automated deployment via GitHub Actions and SSM

##What We built in Project 2:
ComponentStatusVPC with 2 public subnets✅ Done4 Security Groups✅ DoneEC2 Placement Groups (Cluster + Spread)✅ DoneECR Repositories (webapp + batch-worker)✅ DoneFlask Web Application✅ DoneBatch Worker Python App✅ DoneGitHub Repository with code✅ DoneIAM Roles and GitHub Actions user✅ Done3 EC2 Instances with proper roles✅ DoneSQS Queue + Dead Letter Queue✅ DoneS3 Results Bucket✅ DoneGitHub Actions Pipeline (5 jobs)✅ DoneApplication Load Balancer✅ DoneBatch Worker processing SQS jobs✅ DoneCloudWatch Logs + Dashboard✅ DoneCloudWatch Alarms (CPU, ALB, SQS)✅ DoneSNS Email Notifications✅ DoneEnd to End testing
