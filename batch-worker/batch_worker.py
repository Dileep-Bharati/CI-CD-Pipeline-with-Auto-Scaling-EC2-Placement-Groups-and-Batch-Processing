import boto3
import json
import time
import logging
import os
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# AWS clients
sqs = boto3.client('sqs', region_name=os.getenv('AWS_REGION', 'us-east-1'))
s3 = boto3.client('s3', region_name=os.getenv('AWS_REGION', 'us-east-1'))

# Config from environment variables
QUEUE_URL = os.getenv('SQS_QUEUE_URL', '')
OUTPUT_BUCKET = os.getenv('S3_OUTPUT_BUCKET', '')

def process_job(message_body):
    """Process a single batch job"""
    try:
        job = json.loads(message_body)
        job_id = job.get('job_id', 'unknown')
        job_type = job.get('type', 'default')
        data = job.get('data', [])

        logger.info(f"Processing job: {job_id}, type: {job_type}")

        # Simulate processing
        time.sleep(2)

        result = {
            'job_id': job_id,
            'job_type': job_type,
            'status': 'completed',
            'input_count': len(data),
            'processed_count': len(data),
            'timestamp': time.time(),
            'worker_id': os.getenv('HOSTNAME', 'unknown')
        }

        # Save result to S3
        if OUTPUT_BUCKET:
            s3.put_object(
                Bucket=OUTPUT_BUCKET,
                Key=f'results/{job_id}.json',
                Body=json.dumps(result),
                ContentType='application/json'
            )
            logger.info(f"Result saved to S3: results/{job_id}.json")

        logger.info(f"Job {job_id} completed successfully")
        return True

    except Exception as e:
        logger.error(f"Error processing job: {e}")
        return False

def main():
    """Main polling loop"""
    logger.info("Batch worker started")
    logger.info(f"Queue URL: {QUEUE_URL}")
    logger.info(f"Output Bucket: {OUTPUT_BUCKET}")

    if not QUEUE_URL:
        logger.error("SQS_QUEUE_URL environment variable not set!")
        sys.exit(1)

    while True:
        try:
            # Poll SQS for messages
            response = sqs.receive_message(
                QueueUrl=QUEUE_URL,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20,
                MessageAttributeNames=['All']
            )

            messages = response.get('Messages', [])

            if not messages:
                logger.info("No messages in queue, waiting...")
                continue

            logger.info(f"Received {len(messages)} messages")

            for message in messages:
                success = process_job(message['Body'])

                if success:
                    # Delete message from queue after successful processing
                    sqs.delete_message(
                        QueueUrl=QUEUE_URL,
                        ReceiptHandle=message['ReceiptHandle']
                    )
                    logger.info("Message deleted from queue")
                else:
                    logger.warning("Job failed - message will return to queue")

        except KeyboardInterrupt:
            logger.info("Batch worker stopped")
            break
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()
