# RoadObjectDetection


*[자료 조사 & 탐구 동기]
=============

*[탐구 동기]
-------------
현재 테슬라, 그 외 다른 자동차 회사들이 개발하고 있는 자율 주행 기술이 어떤 식으로 작동되는지, 그리고,
AI, 즉, 인공지능이 어떻게 물체를 인식하고, 작동하는지에 대해, 궁금증이 들어, 프로젝트에 참여하게 되었다.

#자율 주행 기술의 등장 배경


자율주행의 개념은 1960년에 벤츠를 중심으로 제안되었고,
70년대 중후반부터 초보적인 연구가 시작되었다.
초기에는 장애물에 대한 인식과 대처 기능을
고려하지 않은 상태로 주행 시험장에서 중앙선이나
차선을 넘지 않는 수준의 기능을 개발하였고,
90년대부터는 비전 기술과 기계학습 기술이
접목되면서 장애물 인식을 적용한 자율주행 기술이
본격적으로 연구되기 시작하였다.
우리나라 도로교통공단 2015년 통계를 보면, 교통사고 전체 원인의 95%
이상이 운전자의 부주의로 인한 과실이다. 이에
따라 운전자의 과실을 최소화해, 교통사고로 인한
인명 손실을 줄이기 위해 자동차 선진국에서는
90년도 초반부터 많은 예산을 투입해 자율주행차 기술의 개발을 지원하고 있다. 

#4차 산업 혁명

빅 데이터 분석, 인공지능, 로봇공학, 사물인터넷을 중심으로 한 기술 혁신이다.

#컴퓨터 비전



#자율 주행을 위해 필요한 기능


#Object Detection 을 활용한 프로젝트



---------------------------------------
##2022-01-19

자율주행 기술 개념 파악 및 이미지 처리기술을 탐구했다.
Object Detection을 활용하여, 객체를 구분 할 수 있게 하는 것이 최종 목표이다.

##2022-01-24

깃허브와 파이참을 이용해, 파일소스를 깃허브에 올리는 방법을 습득 및 계정 생성.
이미지 인식을 하기위해 필요한 json 파일 해석 알고리즘을 배워보았다.
json파일 내에는 이미지 안의 물체들에 대한 정보가 배열과 사전으로 정리되어있어, 그 물체에 대한 정보를 불러오는 방법을 공부했다.
cv2를 이용해, cv2내의 cv2.imshow() 함수를 통해, 경로를 넣어, 이미지를 출력시킬수 있는 알고리즘을 제작하였다.
+예제 이미지 다운

##2022-01-26

24일보다 심화된 해석 알고리즘을 통해, key값과 리스트의 값을 출력했다.
또한, 차와 모터등 여러 정보값이 들어있는 json 파일을 기초로,
사각형을 그릴수 있는 알고리즘을 만들었다.
사각형을 그릴때에도, cv2를 이용하였으며, 내부함수중 cv2.rectangle() 함수를 통해, 사각형을, cv2.putText 함수를 이용해

   
   
![noname01](https://user-images.githubusercontent.com/98321404/153199877-33cbebf2-a660-479d-b922-dab9c8070ba1.jpg)

##2022-02-07

앞서 사각형을 그린 부분을 잘라서 다른 jpg파일로 저장함.
이때, os.listdir을 통해 이미지 파일들을 불러오고, os.path.exists를 통하여 파일 유뮤를,
cv2.imwrite를 통해 이미지 형식으로 저장하였다.   
   
   
![noname02](https://user-images.githubusercontent.com/98321404/153199888-9ec72d85-75f2-49a6-aee1-6b5fefc75b4e.jpg)

