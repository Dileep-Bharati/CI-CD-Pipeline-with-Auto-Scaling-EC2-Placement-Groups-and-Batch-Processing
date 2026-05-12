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
EC2 | ECR | Docker | GitHub Actions | SQS | S3 | CloudWatch | IAM | ALB | ASG

## CI/CD Flow
1. Developer pushes code to GitHub main branch
2. GitHub Actions triggers automatically
3. Runs Python tests (pytest)
4. Builds Docker image
5. Pushes to AWS ECR
6. Deploys to EC2 via SSM
7. SNS notification on success/failure

## Project Structure
