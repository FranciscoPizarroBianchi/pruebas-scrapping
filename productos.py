from slugify.slugify import slugify

class Producto:
    
    def __init__(self, titulo, precio, imagen, enlace, marca="NULL", precio_original="NULL", tipo_promocion="NULL", disponible=0):
        self.titulo_producto = titulo
        self.precio_producto = precio
        self.imagen_producto = imagen
        self.enlace_producto = enlace
        self.slug_producto = slugify(self.titulo_producto)
        self.marca_producto = marca
        self.precio_original_producto = precio_original
        self.tipo_promocion_producto = tipo_promocion
        self.disponible_producto = disponible
        self.esta_disponible()
        
    def __str__(self):
        return """\
            Nombre: {}
            Marca: {}
            Precio: {}
            Precio original: {}
            Promocion: {}
            Slug: {}
            Imagen: {}
            Enlace producto: {}
            Disponible: {}
            """.format(self.titulo_producto,self.marca_producto,self.precio_producto,self.precio_original_producto,self.tipo_promocion_producto,self.slug_producto,self.imagen_producto,self.enlace_producto,self.disponible_producto)

    def esta_disponible(self):
        if self.precio_producto!="":
            self.disponible_producto=1
        else:
            self.precio_producto="0"

    def precio_originalNULL(self):
        if self.precio_original_producto=='':
            self.precio_original_producto='NULL'
            
    def tipo_promocionNULL(self):
        if self.tipo_promocion_producto=='':
            self.tipo_promocion_producto='NULL'
            