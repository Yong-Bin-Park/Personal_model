import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
import os
import numpy as np
import PIL
import dataset

np.set_printoptions(linewidth=1000)
def save_model(h5_path, model_path):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(10, activation='softmax', input_shape=[784]))
    
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['acc'])    
    
    # mnist = input_data.read_data_sets('mnist')
    skin = dataset.trainset
    model.fit(dataset.images, dataset.labels,
              validation_data=[dataset.valid_images, dataset.valid_labels],
              epochs=15, batch_size=128, verbose=0)
    # 케라스 모델과 변수 모두 저장
    model.save('/skin.h5')
    # -------------------------------------- #
    # 저장한 파일로부터 모델 변환 후 다시 저장
    converter = tf.lite.TFLiteConverter.from_keras_model_file('/skin.h5')
    flat_data = converter.convert()
    
    with open('/skin.h5', 'wb') as f:
        f.write(flat_data)
        
save_model('./skin.h5', './skin.tflite')
