#!/usr/bin/env bash
# exit on error
set -o errexit

# 필요 도구 설치
python -m pip install --upgrade pip

# 의존성 설치
pip install -r requirements.txt

# 정적 파일 수집
python manage.py collectstatic --noinput

# 마이그레이션 적용
python manage.py migrate
