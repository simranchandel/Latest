from flask import Flask, render_template,request
app = Flask(__name__)
import mysql.connector
import socket, configparser


mydb = mysql.connector.connect(host= 'localhost',user='root',password='root@123',database='SampleDB')
#conn = MySQLdb.connect("Host Name","db username","password","dbname" )

@app.route("/", methods=['GET'])
def EmployeeDetails():
	mycursor = mydb.cursor()
	#def getDBData():
	mycursor.execute("select * from Employee")
	mydata = mycursor.fetchall() 
	EmpID = request.args.get('EmpID')
	EmpName = request.args.get('EmpName')
	EmpCity = request.args.get('EmpCity')
	
	#Employee_Data = []
	#or data in mydata:
	#	Employee_Data = {'EmpID' : data[0], 'EmpName' : data[1], 'EmpCity' : data[2] }
		#return Employee_Data
		#return response
	return render_template("index.html",Employee_Data=mydata)
		 
	  #return jsonify({'message' : 'It works'})

	mydb.close()

@app.route("/ipadd", methods=['GET'])
def get_Host_name_IP(): 
	
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name) 
		#print(host_name)
		
		return render_template("ipadd.html",host_name=host_name,host_ip=host_ip)


if __name__ == "__main__":
    app.run(port= 8090)


