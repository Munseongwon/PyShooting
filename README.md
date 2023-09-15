# PyShooting
### Mini 1945 Game
<img src="GameStart.png" alt="Intro Screen" width="200px" height="400px"><img src="Playing.png" alt="playing Screen" width="200px" height="400px"><img src="playing.png" alt="Intro Screen" width="200px" height="400px"><img src="exploring.png" alt="Exploring Screen" width="200px" height="400px">

## 프로젝트 요약
![Langauge:Python](https://img.shields.io/badge/Language-Python-purple) ![platform:PyGame](https://img.shields.io/badge/Platform-PyGame-pink)
> 2022.01.11 - 2022.01.16
 
> **Python 팀 프로젝트(화면,아이템 디자인1 게임 개발1)**
* Python 기본 강의를 익히고 난 뒤에 진행한 사이드 게임 프로젝트
* 포토샵으로 게임 배경, 아이템(미사일, 암석)을 만들고 이를 png로 변환시키는 작업을 진행
* PyGame Package를 활용하여 제작하였습니다.
<br>

> **게임 로직 설명**
* 파이참의 파이게임 라이브러리 설치
* 화면창의 크기:480 * 640
* RGB 값 각각 BLACK, WHITE, YELLOW, RED를 주었음
* 게임 1프레임당 60초의 간격을 주었음
* 우주선, 운석, 미사일 클래스 생성
* 우주선은 화면 창에서 벗어나지 않도록 설정, 운석에 부딪히면 즉시 종료, 미사일을 우주선 정중앙에서 나오도록 함
* 돌은 맞혀지는 즉시 파괴, 우주선이 격추한 운석의 개수에 따라 떨어지는 속도를 달리함
* 미사일은 눌리는 키보드에 따라 위치를 달리해서 나오게끔 설정
  * 상, 하, 좌, 우 움직임을 구현
* 파괴 음악, 배경음악, 운석이 폭파하는 음 역시 효과를 랜덤하게 줌
* 운석 역시 30개를 게임창에 랜덤하게 떨어지게끔 설정하여 게임할 시 지루함을 덜했음
<br>

## 시연영상
https://youtu.be/yaYZuceEbYs
