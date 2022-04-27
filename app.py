from flask import render_template, request, Flask, redirect
app=Flask(__name__)
@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
    if request.method=='GET':
        return render_template("str2.html")
    if request.method=='POST':
        print(request.form)
        return render_template("str2.html")
@app.route('/mypage/me')
def first():
    return render_template("strona.html")
if __name__=="__main__":
    app.run(debug=True)
