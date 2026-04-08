from flask import Flask,request,render_template
from model import predict_marks

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    r=None
    if request.method=='POST':
        hours=int(request.form.get('sh'))
        atten=int(request.form.get('at'))
        sleep=int(request.form.get('slh'))

        r=predict_marks(hours,atten,sleep)
        # print(r)
        # return  "hello"
        
    return render_template('index.html',r=r)

if __name__=='__main__':
    app.run(debug=True)
