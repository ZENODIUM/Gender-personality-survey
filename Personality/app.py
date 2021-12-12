from flask import Flask, render_template,request,session, redirect, url_for
app = Flask(__name__)

app.secret_key="123"
@app.route("/")
def mainpage():
    return render_template('mainpage.html')
@app.route('/page1',methods=["GET","POST"])
def page1():
    if request.method=='POST':
        Dict = {"Never":0,"Sometimes":10,"Maybe":20,"Mostly":30,"Always":40}
        Q1 = request.form.get("scale1")
        Q2 = request.form.get("scale2")
        Q3 = request.form.get("scale3")
        Q4= request.form.get("scale4")
        Q5 = request.form.get("scale5")
        Q6 = request.form.get("scale6")
        Q7 = request.form.get("scale7")
        Q8 = request.form.get("scale8")
        Q9 = request.form.get("scale9")
        Q10= request.form.get("scale10")
        Q11 = request.form.get("scale11")
        Q12 = request.form.get("scale12")
        Q13 = request.form.get("scale13")
        Q14 = request.form.get("scale14")
        Q15 = request.form.get("scale15")
        Q16 = request.form.get("scale16")
        Q17 = request.form.get("scale17")
        Q18 = request.form.get("scale18")
        Q19 = request.form.get("scale19")
        Q20 = request.form.get("scale20")
        Q21 = request.form.get("scale21")
        Q22 = request.form.get("scale22")

        Male = 0
        Female = 0
        Male += ((Dict[Q1] + Dict[Q3] + Dict[Q4]+ Dict[Q6]+ Dict[Q10]+ Dict[Q13]+ Dict[Q15]+ Dict[Q17]+ Dict[Q19]+ Dict[Q22])/4)
        Female += ((Dict[Q2] + Dict[Q5] + Dict[Q8]+ Dict[Q7]+ Dict[Q11]+ Dict[Q12]+ Dict[Q16]+ Dict[Q18]+ Dict[Q20]+ Dict[Q21])/4)
        return render_template('result.html',Result = Male,Result1 = Female)
    return render_template('page1.html')


if __name__ == '__main__':
    app.run(debug=True)


