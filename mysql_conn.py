import mysql.connector
from mysql.connector import Error

def conectar_bbdd(nombre_host='localhost',nombre_user='root',password_usuario='',nombre_db='taller'):
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host=nombre_host,
            user=nombre_user,
            password=password_usuario,
            db=nombre_db
        )
    except Error as ex:
        print("Error durante la conexion:",ex)
    return conexion
def ejecutar_query(conexion,query):
    cursor = conexion.cursor()
    cursor = conexion.cursor(buffered=True)
    try:
        cursor.execute(query)
        conexion.commit()
        print('Consulta exitosa')
    except Error as err:
        print(f"Error: '{err}'")

def insertar_productos(producto):
    SQL_SCRIPT = f"""
    INSERT INTO producto
    (slugProducto,SUPERMERCADO_idSUPERMERCADO, marcaProducto,disponibilidad,precioProducto, precioOriginal,tipoPromocionProducto,tituloProducto,imagenProducto,enlaceProducto)VALUES
    ("{producto.slug_producto}",{2},"{producto.marca_producto}",{producto.disponible_producto},"{producto.precio_producto}","{producto.precio_original_producto}","{producto.tipo_promocion_producto}","{producto.titulo_producto}","{producto.imagen_producto}","{producto.enlace_producto}")
    ON DUPLICATE KEY UPDATE
	precioProducto="{producto.precio_producto}",
    precioOriginal="{producto.precio_original_producto}",
    tipoPromocionProducto="{producto.tipo_promocion_producto}"  
    """
    return SQL_SCRIPT

def insertar_precio_historico(producto):
    SQL_SCRIPT = f"""
    INSERT into precio_historico (PRODUCTO_idPRODUCTO,Fecha_inicio,precio)
    VALUES
    ((SELECT producto.idPRODUCTO FROM producto WHERE producto.slugProducto="{producto.slug_producto}"),NOW(),ExtractNumber("{producto.precio_producto}")) 
    """
    return SQL_SCRIPT