from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from core.settings import BASE_DIR

# base_path = os.path.join(BASE_DIR, 'apps/ml/data/')

class PreProcesamientoView(APIView):
    def get(self, request, format=None):
        path = os.path.join(BASE_DIR, 'apps/ml/data/preprocesamiento/Data.csv')
        dataset = pd.read_csv(path)
        x = dataset.iloc[:,17:-1].values
        y = dataset.iloc[:,-1].values

        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        imputer.fit(x[:,1:3])
        x[:,1:3] = imputer.transform(x[:,1:3])

        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import OneHotEncoder
        ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder="passthrough") 
        X = np.array(ct.fit_transform(x))
        # print(X)

        # Codificacion de la variable dependiente
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        Y = le.fit_transform(y)
        # print(Y)

        # Dividir el conjunto de datos en conjunto de entrenamiento y conjunto de prueba
        from sklearn.model_selection import train_test_split
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

        # Escala de caracteristicas
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
        X_test[:, 3:] = sc.transform(X_test[:, 3:])
        print(X_train)
        print(X_test)


        return Response({'data':'serializer.data'}, status=status.HTTP_200_OK)
