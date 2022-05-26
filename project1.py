# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:17:32 2021

@author: Mansi Gaikwad
"""

from flask import *
import pymysql as pm
import requests
from bs4 import BeautifulSoup
import data1

#creating connection
db=pm.connect(host='localhost',user='root',password="",database='project1',port=3306)

#creating cursor
cursor=db.cursor()

app = Flask(__name__)
#initializing flask app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/allpatient")
def allpatient():
    #creating Query
    qr="SELECT * FROM patient_info"
    cursor.execute(qr)
    result=cursor.fetchall()
    return render_template("allpatient.html",data=result)
    
@app.route("/addpatient",methods=['POST'])
def addpatient():
    pname=request.form['pname']
    age=request.form['age']
    contact=request.form['contact']
    dis=request.form['dis']
    dr=request.form['dr']
    insq="INSERT INTO patient_info (pname,age,contact,dis,dr) VALUES('{}','{}','{}','{}','{}')".format(pname,age,contact,dis,dr)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("allpatient"))
    except:
        db.rollback
        return "Error In Query!"

@app.route("/delete")
def delete():
    id=request.args['id']
    delq="DELETE FROM patient_info WHERE id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("allpatient"))
    except:
        db.rollback()
        return "Error In Query!"
     
@app.route("/edit")
def edit():
    id=request.args['id']
    singleqr="SELECT * FROM patient_info WHERE id={}".format(id)
    cursor.execute(singleqr)
    singleres=cursor.fetchone()
    return render_template("edit.html",singlepatient=singleres)

@app.route("/update",methods=['POST'])
def update():
    pname=request.form['pname']
    age=request.form['age']
    contact=request.form['contact']
    dis=request.form['dis']
    dr=request.form['dr']
    uid=request.form['uid']
    upq="UPDATE patient_info SET pname='{}',age='{}',contact='{}',dis='{}',dr='{}' WHERE id='{}'".format(pname,age,contact,dis,dr,uid)
    try:
        cursor.execute(upq)
        db.commit()
        return redirect(url_for("allpatient"))
    except:
        db.rollback()
        return "Error in Query!"

@app.route("/login")
def login():
    return render_template('login.html')
     
@app.route("/check",methods=['POST'])
def check():
    uname=request.form['uname']
    pwd=request.form['pwd']
    if uname=='mkghospital' and pwd=='mkg@123':
        return redirect(url_for("allpatient"))
    else:
        return "Login Failed!"
    
@app.route("/logout")
def logout():
    if 'uname' in session:
        session.pop('uname')
        return redirect(url_for("login"))
    
@app.route("/awareness")
def awareness():
    return render_template('awareness.html')

@app.route("/m_sclerosis")
def m_sclerosis():
    ms_data=data1.ms()
    return render_template('m_sclerosis.html',ms_info=ms_data)

@app.route("/anxiety")
def anxiety():
    anxiety_info=data1.anx()
    return render_template('anxiety.html',anxiety_data=anxiety_info)
    
    
if __name__=="__main__":
    app.run(debug=True)