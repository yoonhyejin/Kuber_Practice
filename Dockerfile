FROM python:3.8

# image의 메타데이터를 설정한다.
LABEL email="myemail@gmail.com"
LABEL name="me"

COPY . /repo

# working directory 설정
WORKDIR /repo

# requirements.txt 파일에서 flask 끌어와서 pip 설치
RUN pip install -r requirements.txt

CMD [ "python", "./FASTAPI/main.py" ]