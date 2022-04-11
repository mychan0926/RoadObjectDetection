import tensorflow as tf
import os #폴더 생성용

model=tf.keras.applications.MobileNet(
    input_shape=(224,224,3),
    include_top=False, #마지막 분류기준을 없에겠다.
    weights='imagenet' #가중치 값은 imagenet을 사용한다.
)

model.trainable=False
#인공신경망 합성곱계층
model=tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(), #7 7을 평균 내는것
    tf.keras.layers.Dense(9), #1024개가 9개로 바뀜. #완전연결 신경망
    tf.keras.layers.Softmax() # 전체의 합으로 배열을 나누어, 전체의 합을 1로 만든다. 비율 유지하면서 총 합만 그대로 유지
])

if not os.path.exists("../models"): #폴더가 그위치에 없다면,
    os.mkdir("../models") #만들기
model.save("../models/mymodel.h5")