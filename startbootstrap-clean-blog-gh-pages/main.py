from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
blog = requests.get(url).json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog/<int:ids>")
def read_post(ids):
    get_post = None
    for article in blog:
        if article['id'] == ids:
            get_post = article
    return render_template("post.html", posts=get_post)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get('username')
        email = request.form['email']
        phone = request.form.get('phone')
        message = request.form['message']
        my_email = "missbellumspython@gmail.com"
        password = "imfdmiuxqrsmondr"
        note = f"Subject: New Form\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message.encode('utf-8')}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=note)
        return render_template("contact.html", sent=True)
    return render_template("contact.html", sent=False)


if __name__ == "__main__":
    app.run(debug=True)
