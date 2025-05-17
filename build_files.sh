#!/bin/bash
# 빌드 스크립트: 정적 파일 수집 및 데이터베이스 마이그레이션

echo "Building the project..."
python manage.py collectstatic --no-input
python manage.py migrate

echo "Build completed!" 