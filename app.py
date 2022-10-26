from flask import Flask, render_template
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'data analyst',
    'location':'benagaluru',
    'salary':'10,00,000'
    
  },
  {
    'id':2,
    'title':'data scientist',
    'location':'delhi',
    'salary':'10,00,000'
  }
  {
    'id':3,
    'title':'frontend engg.',
    'location':'mumbai',
    'salary':'10,00,000'
  }
  
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)
print(__name__)
if __name__=="__main__":
  app.run('0.0.0.0',debug=True)
 