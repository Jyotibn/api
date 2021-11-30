from flask import Flask,request,jsonify

ag = Flask(__name__)

@ag.route('/fun_name', methods =['POST'])
def fun_detail():
    if (request.method == 'POST'):
        name= request.json['name']
        Class = int(request.json['Class'])
        result="my name is "+ name + " and  I study in " + str(Class) + "th class"
        return jsonify(result)
if __name__ =='__main__':
    ag.run()





