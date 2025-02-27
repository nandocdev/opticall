-- cxinsighr.acc_perfiles definition

CREATE TABLE `acc_perfiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.acc_roles definition

CREATE TABLE `acc_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.emp_funcionarios definition

CREATE TABLE `emp_funcionarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `cedula` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `genero` enum('MASCULINO','FEMENINO','OTRO') NOT NULL,
  `estado_civil` enum('SOLTERO','CASADO','DIVORCIADO') NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_cargos_estructura definition

CREATE TABLE `sys_cargos_estructura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_cargos_funcion definition

CREATE TABLE `sys_cargos_funcion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_provincias definition

CREATE TABLE `sys_provincias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_regiones definition

CREATE TABLE `sys_regiones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_secciones_departamentos definition

CREATE TABLE `sys_secciones_departamentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_tipos_unidades definition

CREATE TABLE `sys_tipos_unidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_unidades_ejecutoras definition

CREATE TABLE `sys_unidades_ejecutoras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.acc_permisos definition

CREATE TABLE `acc_permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_perfil` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_permisos_perfil` (`id_perfil`),
  KEY `idx_permisos_rol` (`id_rol`),
  CONSTRAINT `acc_permisos_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `acc_perfiles` (`id`) ON DELETE CASCADE,
  CONSTRAINT `acc_permisos_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `acc_roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.acc_usuarios definition

CREATE TABLE `acc_usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `usuario` varchar(64) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id_perfil` int(11) NOT NULL,
  `activo` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`),
  KEY `id_perfil` (`id_perfil`),
  KEY `idx_usuarios_email` (`usuario`),
  KEY `acc_usuarios_emp_funcionarios_FK` (`id_funcionario`),
  CONSTRAINT `acc_usuarios_emp_funcionarios_FK` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`),
  CONSTRAINT `acc_usuarios_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `acc_perfiles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.emp_informacion_adicional definition

CREATE TABLE `emp_informacion_adicional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `pensionado` tinyint(1) DEFAULT 0,
  `tutor_familiar_discapacitado` tinyint(1) DEFAULT 0,
  `parentesco` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  CONSTRAINT `emp_informacion_adicional_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.emp_informacion_laboral definition

CREATE TABLE `emp_informacion_laboral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `id_unidad_ejecutora` int(11) NOT NULL,
  `id_tipo_unidad` int(11) NOT NULL,
  `id_region` int(11) NOT NULL,
  `id_seccion_departamento` int(11) NOT NULL,
  `id_cargo_estructura` int(11) NOT NULL,
  `id_cargo_funcion` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `salario` decimal(10,2) NOT NULL,
  `ultimo_cambio_etapa` date DEFAULT NULL,
  `proximo_cambio_etapa` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  KEY `id_unidad_ejecutora` (`id_unidad_ejecutora`),
  KEY `id_tipo_unidad` (`id_tipo_unidad`),
  KEY `id_region` (`id_region`),
  KEY `id_seccion_departamento` (`id_seccion_departamento`),
  KEY `id_cargo_estructura` (`id_cargo_estructura`),
  KEY `id_cargo_funcion` (`id_cargo_funcion`),
  CONSTRAINT `emp_informacion_laboral_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_2` FOREIGN KEY (`id_unidad_ejecutora`) REFERENCES `sys_unidades_ejecutoras` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_3` FOREIGN KEY (`id_tipo_unidad`) REFERENCES `sys_tipos_unidades` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_4` FOREIGN KEY (`id_region`) REFERENCES `sys_regiones` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_5` FOREIGN KEY (`id_seccion_departamento`) REFERENCES `sys_secciones_departamentos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_6` FOREIGN KEY (`id_cargo_estructura`) REFERENCES `sys_cargos_estructura` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_informacion_laboral_ibfk_7` FOREIGN KEY (`id_cargo_funcion`) REFERENCES `sys_cargos_funcion` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.emp_informacion_medica definition

CREATE TABLE `emp_informacion_medica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `tipo_sangre` enum('O+','O-','A+','A-','B+','B-','AB+','AB-') NOT NULL,
  `discapacidad` tinyint(1) DEFAULT 0,
  `tipo_discapacidad` varchar(256) DEFAULT NULL,
  `enfermedad_cronica` tinyint(1) DEFAULT 0,
  `tipo_enfermedad` varchar(256) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  CONSTRAINT `emp_informacion_medica_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_distritos definition

CREATE TABLE `sys_distritos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_provincia` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `id_provincia` (`id_provincia`),
  CONSTRAINT `sys_distritos_ibfk_1` FOREIGN KEY (`id_provincia`) REFERENCES `sys_provincias` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_logs definition

CREATE TABLE `sys_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  `nivel` enum('DEBUG','INFO','WARN','ERROR') NOT NULL DEFAULT 'INFO',
  `mensaje` text NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `tipo_log` enum('ACCESO','SISTEMA') NOT NULL DEFAULT 'SISTEMA',
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `sys_logs_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `acc_usuarios` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.acc_logs definition

CREATE TABLE `acc_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `accion` varchar(255) NOT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `acc_logs_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `acc_usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.sys_corregimientos definition

CREATE TABLE `sys_corregimientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_distrito` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `id_distrito` (`id_distrito`),
  CONSTRAINT `sys_corregimientos_ibfk_1` FOREIGN KEY (`id_distrito`) REFERENCES `sys_distritos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- cxinsighr.emp_direcciones definition

CREATE TABLE `emp_direcciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcionario` int(11) NOT NULL,
  `id_corregimiento` int(11) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `id_funcionario` (`id_funcionario`),
  KEY `id_corregimiento` (`id_corregimiento`),
  CONSTRAINT `emp_direcciones_ibfk_1` FOREIGN KEY (`id_funcionario`) REFERENCES `emp_funcionarios` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emp_direcciones_ibfk_4` FOREIGN KEY (`id_corregimiento`) REFERENCES `sys_corregimientos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;