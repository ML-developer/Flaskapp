from flask import Flask, jsonify


app = Flask(__name__)
models = []
@app.route('/loadModel')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    #    n = int(input "Enter the number\n")
    sum = 0
    order = len(str(n))
    copy_n = n 
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")    
        return "True"
    else:
        print(f"{copy_n} is not an armstrong number")
        return "False"

if __name__ == "__main__":
     app.run(debug=True)  