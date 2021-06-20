from flask import Flask, app, render_template, request, redirect, url_for
import pandas as pd
#import seaborn as sns, matplotlib.pyplot as plt, numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

data_diri = []
data_kondisi = []
tabel = ['usia','gender','komp','inet','mandiri','gap'
                ,'kerjasekolah','bantuan','rumahsubsidi']
tabel_kondisi = ['anxiety','depresi','obessive','mood_swing'
                ,'gangguan_kecemasan','compulsive','mudah_lelah','susah_konsentrasi','kerja_parttime']
@app.route("/",methods=['POST','GET'])
def index():
    if request.method == "POST":
        for i in tabel:
            data_diri.append(int(request.form[i]))
        return render_template('data_diri.html',data=data_diri)
    return render_template('form.html')

@app.route("/save_profile",methods=['POST','GET'])
def save_profile():
    if request.method == "POST":
        return render_template('result.html')
    return "data gagal disimpan"

@app.route("/data_kondisi",methods=['POST','GET'])
def data_kondisi():
    if request.method == "POST":
        for i in tabel_kondisi:
            data_kondisi.append(int(request.form[i]))
        return render_template('data_kondisi.html',data=data_kondisi)
    return render_template('form_kondisi.html')

def diagnose():
    df = pd.read_csv("mental_illness.csv", sep=',')
    # encode atribut
    encode = LabelEncoder()
    df['pendidikan'] = encode.fit_transform(df['pendidikan'])
    df['usia'] = encode.fit_transform(df['usia'])
    df['gender'] = encode.fit_transform(df['gender'])
    # shuffle data
    df = df.sample(frac=1)
    # independent variable
    x = df.drop(["mental_illness","pendidikan","memiliki_komputer",
                "disable","akses_internet_memadai","tinggal_dengan_ortu",
                "pernah_gapyear","lama_gapyear","bekerja_dan_sekolah",
                "menerima_bantuan_sosial","tingal_di_rumah_subsidi",
                "banyak_dirawat_karena_mental_illness","usia","gender"], axis = 1)
    x.head()
    # dependent variable
    y = df["mental_illness"]
    y.head()
    # split data train dan data test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state = 123)
    # memanggil naive bayes classifier
    nb = GaussianNB()
    # menginputkan data training
    nb_train = nb.fit(x_train, y_train)
    # Menentukan hasil prediksi dari x_test
    y_pred = nb_train.predict(x_test)
    y_pred

if __name__ == '__main__':
    app.run(debug=True)