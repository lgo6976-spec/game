# 밤놀자

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Flgo6976-spec%2Fgame)

QR 기반 실시간 펜션 파티게임 웹앱입니다. 앱 설치 없이 휴대폰 브라우저에서 방을 만들고, QR/초대 링크로 친구들이 참가해 각자 다른 역할·미션을 받습니다.

## 주요 기능
- 게임 10종: 현상금 사냥, 펜션의 밤, 비밀 지령, 폭탄 돌리기, 감염, 다른 질문, 금지된 행동, 배신자 계약, 익명 폭로전, 마지막 선택
- 역할·타깃·미션·질문·스토리 랜덤화 및 최근 콘텐츠 중복 회피
- 초 단위 타이머, 자동 라운드 진행, 사건/반전, 상대 성공 확인
- 효과음·배경 긴장음·진동
- 새로고침/재접속 복귀, 방장 승계, 한 판 더, 다른 게임 즉시 전환
- 공용 TV/태블릿 화면(비밀정보 미노출)
- 플레이어 인증 토큰과 공개 ID 분리

## 가장 쉬운 배포
위 **Deploy to Render** 버튼을 누른 뒤 Render 로그인/가입 → 표시되는 서비스를 확인 → 배포를 승인합니다. 저장소 루트의 `render.yaml`이 자동으로 사용됩니다.

배포가 끝나면 생성된 `*.onrender.com` HTTPS 주소를 휴대폰으로 열고 방을 만들면 됩니다. `/api/health`가 `ok: true`를 반환하면 서버가 정상입니다.

## 수동 Render Blueprint 배포
1. Render에서 **New → Blueprint**
2. GitHub 저장소 `lgo6976-spec/game` 연결
3. `render.yaml` 감지 확인
4. Blueprint 배포
5. 배포된 HTTPS 주소에서 방 만들기

## 상태 보존형 배포
실사용 안정성이 더 중요하면 `render-persistent.yaml` 구성을 사용합니다. Starter Web Service와 `/var/data` Persistent Disk에 방 상태를 저장하도록 구성되어 있습니다.

## 실행 구조
대화 환경의 GitHub 업로드 제약 때문에 큰 소스는 `source_parts/` 아래 여러 텍스트 파일로 분리되어 있습니다. `server.py`와 `content_pack_v3.py`가 실행 시 자동으로 원본 소스를 조립해 사용합니다. 동작 결과는 일반 단일 파일 배포와 동일합니다.

## 로컬 서버 시작
```bash
pip install -r requirements.txt
python server.py
```

기본 포트는 `8765`이며, Render에서는 `PORT` 환경변수를 자동 사용합니다.
