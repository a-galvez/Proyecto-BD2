CREATE TABLE DimTiempo (
    IdTiempo DATE PRIMARY KEY,
    Dia INT,
    Mes INT,
    NombreMes VARCHAR(20),
    Trimestre INT,
    Anio INT
);

CREATE TABLE DimPais (
    IdPais VARCHAR(2) PRIMARY KEY,
    NombrePais VARCHAR(100)
);

CREATE TABLE DimProvincia (
    IdProvincia INT PRIMARY KEY,
    NombreProvincia VARCHAR(100),
    IdPais VARCHAR(2),
    FOREIGN KEY (IdPais) REFERENCES DimPais(IdPais)
);

CREATE TABLE DimCliente (
    IdCliente INT PRIMARY KEY,
    NombreCliente VARCHAR(150),
    IdProvincia INT,
    FOREIGN KEY (IdProvincia) REFERENCES DimProvincia(IdProvincia)
);

CREATE TABLE DimCategoriaProducto (
    IdCategoria INT PRIMARY KEY,
    NombreCategoria VARCHAR(100)
);

CREATE TABLE DimSubcategoriaProducto (
    IdSubcategoria INT PRIMARY KEY,
    NombreSubcategoria VARCHAR(100),
    IdCategoria INT,
    FOREIGN KEY (IdCategoria) REFERENCES DimCategoriaProducto(IdCategoria)
);

CREATE TABLE DimProducto (
    IdProducto INT PRIMARY KEY,
    NombreProducto VARCHAR(100),
    PrecioUnitario DECIMAL(10,2),
    IdSubcategoria INT,
    FOREIGN KEY (IdSubcategoria) REFERENCES DimSubcategoriaProducto(IdSubcategoria)
);

CREATE TABLE DimVendedor (
    IdVendedor INT PRIMARY KEY,
    NombreVendedor VARCHAR(150),
);

CREATE TABLE DimMetodoEnvio (
    IdMetodoEnvio INT PRIMARY KEY,
    NombreMetodo VARCHAR(100)
);

CREATE TABLE DimCanalVenta (
    IdCanal INT PRIMARY KEY IDENTITY(1,1),
    Canal VARCHAR(50) 
);

CREATE TABLE HechosVentas (
    IdVenta INT PRIMARY KEY,
    IdTiempo DATE,
    IdCliente INT,
    IdProducto INT,
    IdVendedor INT,
    IdMetodoEnvio INT,
    IdCanal INT,
    MontoVenta DECIMAL(18,2),
    CantidadVendida INT,

    FOREIGN KEY (IdTiempo) REFERENCES DimTiempo(IdTiempo),
    FOREIGN KEY (IdCliente) REFERENCES DimCliente(IdCliente),
    FOREIGN KEY (IdProducto) REFERENCES DimProducto(IdProducto),
    FOREIGN KEY (IdVendedor) REFERENCES DimVendedor(IdVendedor),
    FOREIGN KEY (IdMetodoEnvio) REFERENCES DimMetodoEnvio(IdMetodoEnvio),
    FOREIGN KEY (IdCanal) REFERENCES DimCanalVenta(IdCanal)
);
