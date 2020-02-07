from flask import Flask, render_template, request
from file_proc 

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href='/home'>Hi!</a>"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = 7442457)
  
@app.route('/params')
def params():
  return request.args

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 5222, threaded = True, debug = True)


# a - Will append to the end of the file
# w - Will overwrite any existing content
​
file_name = 'data.txt'
​
  # with open(file_name, 'w') as f:       
  #     f.write(line)
def rewrite_file(lines):
  f = open(file_name, 'w')
  for line in lines:        
      f.write(line)
  f.close()
​
def write_file(param):
  f = open(file_name, 'a')
  f.write(param + '\n')
  f.close()
​
def read_file():
  f = open(file_name, 'r')
  if f.mode == 'r':
    contents = f.read()
  else:
    contents = f"Couldn't read from file {file_name}"
​
  return contents
    
def read_lines():
  with open(file_name) as f:
    lines_array = f.readlines()
  return lines_array


  