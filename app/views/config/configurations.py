from app import app, render_template



@app.route("/configurations")
def configs():
    return render_template("conf/config.html")