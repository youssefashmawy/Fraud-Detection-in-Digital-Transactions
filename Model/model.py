# # This Python 3 environment comes with many helpful analytics libraries installed
# # It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# # For example, here's several helpful packages to load

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# # Input data files are available in the read-only "../input/" directory
# # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

# import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# # You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

 
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense, Input, Dropout
from sklearn.metrics import confusion_matrix
from tensorflow.keras import layers
import joblib
from IPython.display import clear_output
# from google.colab import files

# Uncomment the next 2 cells if you want to use google colab

 
# from google.colab import files
# files.upload()
# clear_output(wait=True)


 
# !mkdir -p ~/.kaggle
# !mv kaggle.json ~/.kaggle/
# !chmod 600 ~/.kaggle/kaggle.json


 
!kaggle datasets download -d mlg-ulb/creditcardfraud
!unzip -o creditcardfraud.zip
!rm -rf creditcardfraud.zip

 
df = pd.read_csv('/kaggle/input/creditcardfraud/creditcard.csv')

X = df.drop(columns=['Class'])
y = df['Class']



 
df.head()

 
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1, shuffle=True)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_test, X_val , y_test, y_val = train_test_split(X_test, y_test, train_size=0.5, random_state=1, shuffle=True)

 
joblib.dump(scaler, 'scaler.pkl')

 
y_train = y_train.values
y_test = y_test.values
y_val = y_val.values

 
# TPU configuration
try:
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    tf.config.experimental_connect_to_cluster(tpu)
    tf.tpu.experimental.initialize_tpu_system(tpu)
    strategy = tf.distribute.TPUStrategy(tpu)
    print("Running on TPU")
except ValueError:
    print("TPU not found, using CPU/GPU instead")
    strategy = tf.distribute.get_strategy()

 
with strategy.scope():
    model = Sequential([
        Input(shape=(X_train.shape[1],)),
        Dense(128, activation='relu'),
        Dropout(0.6),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',  # Keep the loss suitable for binary classification
        metrics=[
            tf.keras.metrics.Recall(),  # Prioritize recall
            tf.keras.metrics.Precision(),  # Optionally track precision as well
            'accuracy'  # Still track accuracy for reference
        ]
    )


early_stopping = EarlyStopping(monitor='val_recall', patience=10, mode='max', restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, verbose=1)

# Class weights to priotrize class 1
class_weight = {0: 1., 1: 16}

 
batch_size = 32
history = model.fit(X_train, y_train,
                    epochs=20,
                    batch_size=batch_size,
                    validation_data=(X_val, y_val),
                    verbose=1,
                    callbacks=[early_stopping, reduce_lr],
                    class_weight=class_weight)


 
results = model.evaluate(X_test, y_test, verbose=1)

 
def print_scores(y_true, y_pred, model_name):
    print(f"{model_name} Precision: {precision_score(y_true, y_pred):0.2f}")
    print(f"{model_name} Recall: {recall_score(y_true, y_pred):0.2f}")
    print(f"{model_name} F1-Score: {f1_score(y_true, y_pred):0.2f}")

 
y_train_pred_ = model.predict(X_train)

 
y_val_pred_ = model.predict(X_val)

 
thresholds = [0.3,0.4,0.48,0.5 ,0.55,0.56,0.59, 0.6,0.7]
for threshold in thresholds:
    y_val_pred = (y_val_pred_ > threshold).astype(int).flatten()
    print(f'threshold: {threshold}')
    print_scores(y_val, y_val_pred, 'Neural Network (Validation)')
threshold = 0.55

 
y_train_pred = (y_train_pred_ > threshold).astype(int).flatten()
print(f'threshold: {threshold}')
print_scores(y_train, y_train_pred, 'Neural Network (Train)')

 
y_pred_ = (model.predict(X_test))

 
print(f'threshold: {threshold}')
y_pred = (y_pred_ > threshold).astype("int32")
print_scores(y_test, y_pred, 'Neural Network (Test)')

 
model.save('neural_network_model_pca_80.keras')

 
import tensorflow as tf
import keras

print(f'TensorFlow version: {tf.__version__}')
print(f'Keras version: {keras.__version__}')


