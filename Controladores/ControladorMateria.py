from Modelos.Materia import Materia
from Modelos.Departamento import Departamento
from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento

class ControladorMateria():

    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioMateria.findAll()

    def create(self,infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self,id):
        elMateria = Materia(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update (self,id,infoMateria):
        MateriaActual = Materia(self.repositorioMateria.findById(id))
        MateriaActual.creditos = infoMateria["creditos"]
        MateriaActual.nombre = infoMateria["nombre"]
        return self.repositorioMateria.save(MateriaActual)

    def delete (self,id):
        return self.repositorioMateria.delete(id)

    def cedula(self,cedula):
        query = {"cedula":{ "$eq" : cedula}}
        return self.repositorioMateria.query(query)

    """
    Relación departamento y materia
    """

    def asignarDepartamento (self,id,id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)