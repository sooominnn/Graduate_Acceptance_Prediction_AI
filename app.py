
import pandas as pd

data = pd.read_csv('gpascore.csv')

# print(data.isnull().sum())
data = data.dropna()

y데이터 = data['admit'].values

x데이터 = []

# data라는 데이터프레임을 가로 한 줄씩 출력
for i, rows in data.iterrows():
  x데이터.append([rows['gre'], rows['gpa'], rows['rank']])


import numpy as np
import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Desnse(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x데이터), np.array(y데이터), epochs=10)
