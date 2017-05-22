from flask import Flask, render_template,request,redirect,url_for,send_from_directory,current_app,make_response
import sys
import random
import json

app = Flask(__name__)

@app.route('/')
def loadFile():
    f =open('/home/ubuntu/flaskapp/static/data2.csv', 'a')
    with open('/home/ubuntu/output5/part-00000', 'rb') as csvfile:
        f.write("word1,word2,count")
        for row in csvfile:
            f.write(row)
#      jsonList = []
#      for row in csvfile:
#          line=row.split('\t')
#          wordDict={}
#          word,count=line[0].split(',',1)
#          wordDict['letter']=word
#          wordDict['frequency']=int(count)
#          jsonList.append(wordDict)
#    with open('/home/ubuntu/flaskapp/static/data.json', 'w+') as var:
#          var.write(json.dumps(jsonList))
    return render_template("index.html")
 
@app.route('/bar', methods=['GET','POST'])
def drawbar():
    return render_template("barChart.html")

@app.route('/scatter', methods=['GET','POST'])
def drawscatter():
    return render_template("scatterPlot.html") 
             
#      for line in data:
#          ulist.append(line.strip())

##login page
#@app.route('/')
#def login():
#    out=''
#    return render_template("login.html", contents=out)
#
##logout
#@app.route('/logoutUser', methods=['POST'])
#def logoutUser():
#    out=''
#    return render_template("login.html", contents=out)    
#
##create new user
#@app.route('/create',methods=["POST"])
#def create():
#    newuser = request.form['newuser']
#    ulist=[]
#    with open('/home/ubuntu/flaskapp/authenticate.txt', 'a+') as data:
#      for line in data:
#          ulist.append(line.strip())
#      if newuser.strip() in ulist:
#          out = "User exists. Please login to continue"
#          return render_template("login.html",contents=out)
#      else:
#          data.write('\n'+newuser)      
#          out = "User created. Please login to continue"
#          return render_template("login.html",contents=out)
#
##after successful login
#@app.route('/userlogin', methods=['GET','POST'])
#def Hello():
#    username = request.form['uname']
#    ulist=[]
#    with open('/home/ubuntu/flaskapp/authenticate.txt', 'r+') as data:
#      for line in data:
#          ulist.append(line.strip())
#    if username in ulist:
#        return redirect(url_for('Back'))
#    out = "User not authenticated"    
#    return render_template("login.html", contents=out)
#
##back button
#@app.route('/back',methods=['GET', 'POST'])
#def Back():
#    file_list=[]
#    for files in bucket.get_all_keys():
#        file_list.append(files.key)
#    return render_template("index.html",nlist=file_list)        
#
##upload a new file
#@app.route('/upload',methods=['GET', 'POST'])
#def Upload():
#    upload_file = request.files['file']
#    file_name = upload_file.filename
#    file_contents = upload_file.read()
#    k = bucket.new_key(bucket_name)
#    k.key = file_name
#    k.set_contents_from_string(file_contents)
#    out = "success"
#    return render_template("uploadfile.html",contents=out)
#
##list all files
#@app.route('/list',methods=['POST'])
#def List():
#    dlist=[]
#    for files in bucket.get_all_keys():
#        file_name = files.key
#        size = files.size
#        last_modified = files.last_modified
#        dvar={}
#        dvar['file_name']=file_name
#        dvar['size']=size
#        dvar['last_modified']=last_modified
#        dlist.append(dvar)
#    return render_template("list.html",lists=dlist)               
#
##download a file
#@app.route('/download', methods=['GET','POST'])
#def download():
#    s3 = boto3.resource('s3',aws_access_key_id, aws_secret_access_key , region_name= 'us-west-2')
#    bucket = s3.Bucket(bucket_name)
#    file_selected=request.form['filename']
#    for files in bucket.objects.all():
#        if file_selected == files.key:
#            file_contents = files.get()['Body'].read()
#            response = make_response(file_contents)
#            response.headers["Content-Disposition"] = "attachment; filename=" + file_selected
#    return response
#
##delete a file
#@app.route('/delete', methods=['GET','POST'])
#def delete():
#    file_selected = request.form['filedelete']  
#    for files in bucket.get_all_keys():
#        if files.key == file_selected:
#            files.delete()
#            out = "file deleted"
#    return render_template("uploadfile.html",contents=out)
#    
if __name__ == '__main__':
    app.run()