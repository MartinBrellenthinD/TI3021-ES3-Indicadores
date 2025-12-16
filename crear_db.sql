-- Creación de la tabla de usuarios del sistema
-- Esta tabla almacena las credenciales de acceso de forma segura
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,          -- Identificador único del usuario
    username TEXT UNIQUE NOT NULL,   -- Nombre de usuario, no se puede repetir
    password_hash TEXT NOT NULL,     -- Hash de la contraseña (no se guarda en texto plano)
    salt BLOB NOT NULL               -- Salt utilizada para generar el hash de la contraseña
);

-- Creación de la tabla de indicadores económicos
-- Aquí se registran los datos obtenidos desde la API externa
CREATE TABLE indicadores (
    id INTEGER PRIMARY KEY,          -- Identificador único del registro
    nombre TEXT NOT NULL,            -- Nombre del indicador (UF, IPC, UTM, etc.)
    fecha_indicador TEXT NOT NULL,   -- Fecha correspondiente al valor del indicador
    valor REAL NOT NULL,             -- Valor numérico del indicador económico
    fecha_consulta TEXT NOT NULL,    -- Fecha en que el usuario realizó la consulta
    usuario TEXT NOT NULL,           -- Usuario que realizó la consulta
    proveedor TEXT NOT NULL          -- Fuente que provee el indicador (API utilizada)
);
