import tensorflow as tf
import os
import numpy as np
from tensorflow.keras import models,layers
from tensorflow.keras.callbacks import EarlyStopping
import json
# -------------------------------------------------------------------
def model_make(path):
    batch=32
    image_size=256
    channel=3
    dataset_name = os.path.basename(path)
    print("-"*50,dataset_name)
    # train,test,val split 
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        path,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(256,256),
        batch_size=batch
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        path,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(256,256),
        batch_size=batch
    )
    # checking class names 
    class_name = train_ds.class_names
    print(class_name)
    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    # ---------------resize and rescale--------------
    image_size=224
    resize_and_rescale =tf.keras.Sequential(
        [layers.Resizing(image_size,image_size),
        layers.Rescaling(1./255)]
    )
    # --------------data argumentation----------------
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
    ])
    # ---------------------model--------------------
    model = tf.keras.Sequential([
        resize_and_rescale,
        data_augmentation,
        layers.Conv2D(32,kernel_size=(3,3),input_shape=(224,224,channel),activation='relu'),
        layers.MaxPool2D((2,2)),
        layers.Conv2D(64,kernel_size=(3,3),activation='relu'),
        layers.MaxPool2D((2,2)),
        layers.Conv2D(128,kernel_size=(3,3),activation='relu'),
        layers.MaxPool2D((2,2)),
        layers.Flatten(),
        layers.Dense(64,activation='relu'),
        layers.Dense(len(class_name), activation='softmax')
    ])
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy']
    )
    # early stopping 
    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=3,  
        restore_best_weights=True
    )
    
    # model training
    history = model.fit(
        train_ds,
        epochs=50, 
        validation_data=val_ds,
        callbacks = [early_stop]
    )
    # model evaluation
    print("-"*50)
    print(history.history['accuracy'])
    print(history.history['val_accuracy'])
    print("-"*50)
    model.evaluate(val_ds)   
    model.save(f"{dataset_name}.keras")  
    with open(f"{dataset_name}_classes.json", "w") as f:
        json.dump(class_name, f)  
    
 
if __name__=='__main__':
    potato="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/potato"
    tomato="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/tomato"
    banana="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/banana"
    grapes="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/grapes"
    strawberry="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/strawberry"
    mango="C:/Users/shiva/Desktop/crop classification and disease detection/crop disease classification/mango"
    
    crops=[potato,tomato,banana,grapes,strawberry,mango]
    for i in crops:
        print( )
        model_make(i)
        