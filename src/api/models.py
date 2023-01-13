from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_pedido = db.Column(db.Integer, unique=True, nullable=False)
    fecha = db.Column(db.Integer, unique=False, nullable=False)
    cliente = db.Column(db.String, unique=False, nullable=False)
    productos = db.Column(db.String, nullable=False)
    precio_total = db.Column(db.Integer, nullable=False)
    estado_de_pago = db.Column(db.String, nullable=False)
    estado_de_preparacion = db.Column(db.String, nullable=False)
    forma_de_entrega = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<Pedidos {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "numero_pedido": self.numero_pedido,
            "fecha": self.fecha,
            "cliente": self.cliente,
            "productos": self.productos,
            "precio_total": self.precio_total,
            "estado_de_pago": self.estado_de_pago,
            "estado_de_preparacion": self.estado_de_preparacion,
            "forma_de_entrega": self.forma_de_entrega,

            
            # do not serialize the password, its a security breach
        }

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=False, nullable=False)
    descripcion = db.Column(db.String, unique=False, nullable=False)
    coleccion = db.Column(db.String, unique=False, nullable=False)
    etiqueta = db.Column(db.String, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    estado_de_uso = db.Column(db.String, nullable=False)
    marca = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    cantidad = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Productos {self.id}>'

    def serialize(self):
        return {
            "id" : self.id, 
            "nombre": self.nombre,
            "descripcion" : self.descripcion, 
            "coleccion"  : self.coleccion,
            "etiqueta"  : self.etiqueta,
            "precio"  : self.precio, 
            "estado_de_uso"  : self.estado_de_uso, 
            "marca"  : self.marca, 
            "color"  : self.color, 
            "cantidad"  : self.cantidad, 

            
            # do not serialize the password, its a security breach
        }


class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    direccion = db.Column(db.String, unique=False, nullable=False)
    postal_code= db.Column(db.Integer, nullable=False)
    notas = db.Column(db.Integer, nullable=False)
    numero_telefono = db.Column(db.Integer, unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=False)
    numero_pedidos = db.Column(db.Integer, nullable=False)
    monto_gastado = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Clientes {self.id}>'

    def serialize(self):
        return {
            "id" : self.id, 
            "nombre_completo": self.nombre_completo,
            "email" : self.email, 
            "direccion"  : self.direccion,
            "postal_code"  : self.postal_code,
            "notas"  : self.notas, 
            "numero_telefono"  : self.numero_telefono, 
            "fecha_nacimiento"  : self.fecha_nacimiento, 
            "password"  : self.password, 
            "numero_pedidos"  : self.numero_pedidos, 
            "monto_gastado"  : self.monto_gastado, 

            
            # do not serialize the password, its a security breach
        }

    

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String, unique=True, nullable=False)
    nombre = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tipo_de_usuario = db.Column(db.Boolean, nullable=False)
    

    def __repr__(self):
        return f'<Usuarios {self.id}>'

    def serialize(self):
        return {
            "id" : self.id, 
            "nombre_usuario": self.nombre_usuario,
            "nombre": self.nombre,
            "email" : self.email, 
            "password"  : self.password, 
            "tipo_de_usuario"  : self.tipo_de_usuario, 

            
            # do not serialize the password, its a security breach
        }

    
class Colecciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=False, nullable=False)
    descripcion= db.Column(db.String, unique=True, nullable=False)
    productos = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Colecciones {self.id}>'

    def serialize(self):
        return {
            "id" : self.id, 
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "productos" : self.productos, 
            

            
            # do not serialize the password, its a security breach
        }

    
