import tensorflow as tf

train_dataset=tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224,224),
    label_mode='categorical'
    #batch_size=1 덩어리를 묶는 기준 (1개씩 묶기)
)

data = train_dataset.take(1) #data set을 큰덩어리 하나로 가져옴
for images, labels in data:
    print(images, labels)

print(train_dataset.class_names)