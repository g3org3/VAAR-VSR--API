from flask import Flask, request, jsonify
import subprocess
import sys
import json
import os

PORT = 5000
CLI_PATH = '/cli/cli.py'

if os.environ.get('PORT'):
  try:
    p = int(os.environ.get('PORT'))
    print("> chaning port to :", p)
    PORT = p
  except:
    PORT = 5000

if os.environ.get('CLI_PATH'):
  CLI_PATH = str(os.environ.get('CLI_PATH'))

def res_send(content):
  if "text/html" in request.headers.get('Accept'): return "<pre>"+content+"</pre>"
  return content

app = Flask(__name__)
def shell(line):
  try:
    output = subprocess.check_output(line.split(' '), stderr=subprocess.STDOUT)
    return output.strip()
  except subprocess.CalledProcessError as exc:
    return exc.output

"""------------------------------------
  READ DATA
------------------------------------"""
@app.route("/api/output.smt")
def getOutputSmt():
  content = "empty"
  try:
    content = file('output/output.smt2').read()
  except:
    print("empty")
  return res_send(content)

@app.route("/api/output.json")
def getOutputJSON():
  content = "empty"
  try:
    content = file('output/output.json').read()
    content = json.loads(content)
    return jsonify(content)
  except:
    print("empty")
  return content

@app.route("/api/maindata.json")
def getMaindataJSON():
  content = "empty"
  try:
    content = file('output/maindata.json').read()
    maindata = json.loads(content)
    maindata["blob"] = None
    return jsonify(maindata)
  except:
    print("empty")
  return content

@app.route("/api/config")
def getConf():
  content = file('files/config').read()
  return res_send(content)

@app.route("/api/tosca-conf")
def getToscaConf():
  content = file('files/tosca-conf.yml').read()
  return res_send(content)

@app.route("/api/rules")
def getRules():
  content = file('files/rules.smt').read()
  return res_send(content)

@app.route("/api/")
def getIndex():
  content = "\n".join(['/api/config', '/api/tosca-conf', '/api/rules'])
  return res_send(content)

@app.route("/api/version")
def getVersion():
  return res_send(jsonify({ "epav": "1.0.1", "epav-api": "1.1.0" }))

"""------------------------------------
  WRITE DATA
------------------------------------"""
@app.route("/api/config", methods=["POST"])
def setConf():
  data = request.get_json()['data']
  f = open("files/config", "w")
  f.write(data)
  f.close()
  return jsonify({ "message": "success" })

@app.route("/api/tosca-conf", methods=["POST"])
def setToscaConf():
  data = request.get_json()['data']
  f = open("files/tosca-conf.yml", "w")
  f.write(data)
  f.close()
  return jsonify({ "message": "success" })

@app.route("/api/rules", methods=["POST"])
def setRules():
  data = request.get_json()['data']
  f = open("files/rules.smt", "w")
  f.write(data)
  f.close()
  return jsonify({ "message": "success" })

"""------------------------------------
  CORE EXEC
------------------------------------"""
@app.route("/api/run")
def run():
  content = shell("python "+ CLI_PATH +" -t files/rules.smt -c files/tosca-conf.yml -k files/config")
  content = content.replace("[4m", "")
  content = content.replace("[0m", "")
  return res_send(content)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=PORT)
