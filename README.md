# 🤖 Inspection_Turtlebot4

TurtleBot4를 이용한 공장 자동 점검 로봇 프로젝트입니다.  
ROS 2 Humble과 Webots 시뮬레이터를 활용하여, 사전 정의된 경로를 따라 자동으로 순찰, 장애물 회피, 촬영, 데이터 저장 및 복귀를 수행합니다.

---

## 📂 프로젝트 구조
 ### Version 1.0.0
 ros2_ws/
├── src/
│ └── factory_inspection_bot/ ← ROS 2 Python 패키지
├── data/ ← 사진 및 메타데이터 저장 폴더 (자동 생성됨)
├── install/, build/, log/ ← colcon 빌드 아티팩트 (자동 생성됨)
└── .gitignore, README.md

---

## ⚙️ 개발 환경

- Ubuntu 22.04
- ROS 2 Humble

---

## 📦 설치 방법

### 1️⃣ `dev` 브랜치 기준으로 프로젝트 클론

```bash
git clone -b dev https://github.com/JACKSON-KIM-JAEHO/Inspection_Turtlebot4.git
cd Inspection_Turtlebot4


