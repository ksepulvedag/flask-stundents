from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion

app=Flask(__name__)
cors = CORS(app)
miControladorEstudiante=ControladorEstudiante()
miControladorMateria=ControladorMateria()
miControladorDepartamento=ControladorDepartamento()
miControladorInscripcion=ControladorInscripcion()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

########################### Estudiantes ######################################
@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    return jsonify(json)

@app.route("/estudiantes/cedula/<string:cc>",methods=['GET'])
def cedulaEstudiante(cc):
    json=miControladorEstudiante.cedula(cc)
    return jsonify(json)

######################### Departamentos ################################################

@app.route("/departamento",methods=['GET'])
def getdepartamento():
    json=miControladorDepartamento.index()
    return jsonify(json)

@app.route("/departamento",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    return jsonify(json)

@app.route("/departamento/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    return jsonify(json)

@app.route("/departamento/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    return jsonify(json)

@app.route("/departamento/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
    return jsonify(json)

@app.route("/departamento/cedula/<string:cc>",methods=['GET'])
def cedulaDepartamento(cc):
    json=miControladorDepartamento.cedula(cc)
    return jsonify(json)

##################### Materia #############################################
@app.route("/materia",methods=['GET'])
def getmateria():
    json=miControladorMateria.index()
    return jsonify(json)

@app.route("/materia",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    return jsonify(json)

@app.route("/materia/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    return jsonify(json)

@app.route("/materia/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorMateria.update(id,data)
    return jsonify(json)

@app.route("/materia/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorMateria.delete(id)
    return jsonify(json)

@app.route("/materia/cedula/<string:cc>",methods=['GET'])
def cedulaMateria(cc):
    json=miControladorMateria.cedula(cc)
    return jsonify(json)

@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    json=miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(json)

##################### Inscripcion #############################################

@app.route("/inscripcion",methods=['GET'])
def getinscripcion():
    json=miControladorInscripcion.index()
    return jsonify(json)

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripcion/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripcion/<string:id>",methods=['DELETE'])
def eliminarInscripcion(id):
    json=miControladorInscripcion.delete(id)
    return jsonify(json)

@app.route("/inscripcion/cedula/<string:cc>",methods=['GET'])
def cedulaInscripcion(cc):
    json=miControladorInscripcion.cedula(cc)
    return jsonify(json)

@app.route("/inscripciones/materia/<string:id_materia>",methods=['GET'])
def inscritosEnMateria(id_materia):
    json=miControladorInscripcion.listarInscritosEnMateria(id_materia)
    return jsonify(json)

@app.route("/inscripciones/notas_mayores",methods=['GET'])
def getNotasMayores():
    json=miControladorInscripcion.notasMasAltasPorCurso()
    return jsonify(json)

@app.route("/inscripciones/promedio_notas/materia/<string:id_materia>",methods=['GET'])
def getPromedioNotasEnMateria(id_materia):
    json=miControladorInscripcion.promedioNotasEnMateria(id_materia)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])