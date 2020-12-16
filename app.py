from flask import Flask, request, render_template
from nutritionix import Nutritionix
import pandas as pd
nix = Nutritionix(app_id="10a7e7f0", api_key="3e5a3b8e656539288316aa1a839cccbb")
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    # processed_text = text.upper()

    results = nix.search(query=text).nxql(

        filters={
            
    #         "nf_calories": {
    #             "from": 100,
    #             "to": 500
    #             #"lte": 5000
    #         }
        },
        fields=["item_name", "nf_calories"]
    ).json()

    results = results['hits']
    rl = []
    for x in results:
        f = x["fields"]
        rl.append(f)
    df = pd.DataFrame(rl)

    df=df.to_html()
    return render_template("my-form.html", df=df)
if __name__ == "__main__":
   app.run()