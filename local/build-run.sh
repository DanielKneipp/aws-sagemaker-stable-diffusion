set -e

tar -ch . | docker build -t stable-difusion:latest -f Dockerfile -
docker run --gpus=all -v "$(pwd)/output:/app/output" stable-difusion:latest
