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
VPC with 2 public subnets✅ Done4 
Security Groups✅ Done
EC2 Placement Groups (Cluster + Spread)✅ Done
ECR Repositories (webapp + batch-worker)✅ Done
Flask Web Application✅ Done
Batch Worker Python App✅ Done
GitHub Repository with code✅ Done
IAM Roles and GitHub Actions user✅ Done
EC2 Instances with proper roles✅ Done
SQS Queue + Dead Letter Queue✅ Done
S3 Results Bucket✅ Done
GitHub Actions Pipeline (5 jobs)✅ Done
Application Load Balancer✅ Done
Batch Worker processing SQS jobs✅ Done
CloudWatch Logs + Dashboard✅ Done
CloudWatch Alarms (CPU, ALB, SQS)✅ Done
SNS Email Notifications✅ Done
End to End testing✅ Done
