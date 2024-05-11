from flask import Flask,render_template,request
import requests
app = Flask(__name__)
base_url = "https://api.github.com/users/"
@app.route('/',methods =["GET","POST"])
def index():

    if request.method == "POST":
        github_name = request.form.get("github_name")
        response_user = requests.get(base_url + github_name) # comes with json format
        response_repo = requests.get(base_url+github_name+"/repos")# comes with json list format
        user_information = response_user.json()# to json
        user_reops = response_repo.json()
        

        if "message" in user_information: # handel error
            return render_template("index.html",error="User Not Found")
        else:
          return render_template("index.html",profile=user_information,repos=user_reops)
    else:
        return render_template("index.html") # Get request just show the index page



















if __name__ == "__main__":
    app.run(debug=True)