FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

WORKDIR /app

ADD stable-diffusion-v1-4 /app/stable-diffusion-v1-4
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD code.py /app/code.py

CMD [ "python", "code.py" ]
