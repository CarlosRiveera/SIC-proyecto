-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2021 at 03:39 PM
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `siscontable`
--

-- --------------------------------------------------------

--
-- Table structure for table `actualizacioninventario_actualizacioninventario`
--

CREATE TABLE IF NOT EXISTS `actualizacioninventario_actualizacioninventario` (
`idActualzacion` int(11) NOT NULL,
  `existencias` int(11) NOT NULL,
  `costoUnitario` double NOT NULL,
  `costoTotal` double NOT NULL,
  `kardex_id` int(11) NOT NULL,
  `transaccionInventario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
`id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
`id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
`id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=81 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add modulo', 6, 'add_modulo'),
(22, 'Can change modulo', 6, 'change_modulo'),
(23, 'Can delete modulo', 6, 'delete_modulo'),
(24, 'Can view modulo', 6, 'view_modulo'),
(25, 'Can add permiso', 7, 'add_permiso'),
(26, 'Can change permiso', 7, 'change_permiso'),
(27, 'Can delete permiso', 7, 'delete_permiso'),
(28, 'Can view permiso', 7, 'view_permiso'),
(29, 'Can add usuario', 8, 'add_usuario'),
(30, 'Can change usuario', 8, 'change_usuario'),
(31, 'Can delete usuario', 8, 'delete_usuario'),
(32, 'Can view usuario', 8, 'view_usuario'),
(33, 'Can add cuenta', 9, 'add_cuenta'),
(34, 'Can change cuenta', 9, 'change_cuenta'),
(35, 'Can delete cuenta', 9, 'delete_cuenta'),
(36, 'Can view cuenta', 9, 'view_cuenta'),
(37, 'Can add valor inicial', 10, 'add_valorinicial'),
(38, 'Can change valor inicial', 10, 'change_valorinicial'),
(39, 'Can delete valor inicial', 10, 'delete_valorinicial'),
(40, 'Can view valor inicial', 10, 'view_valorinicial'),
(41, 'Can add marca', 11, 'add_marca'),
(42, 'Can change marca', 11, 'change_marca'),
(43, 'Can delete marca', 11, 'delete_marca'),
(44, 'Can view marca', 11, 'view_marca'),
(45, 'Can add categoria producto', 12, 'add_categoriaproducto'),
(46, 'Can change categoria producto', 12, 'change_categoriaproducto'),
(47, 'Can delete categoria producto', 12, 'delete_categoriaproducto'),
(48, 'Can view categoria producto', 12, 'view_categoriaproducto'),
(49, 'Can add producto', 13, 'add_producto'),
(50, 'Can change producto', 13, 'change_producto'),
(51, 'Can delete producto', 13, 'delete_producto'),
(52, 'Can view producto', 13, 'view_producto'),
(53, 'Can add kardex', 14, 'add_kardex'),
(54, 'Can change kardex', 14, 'change_kardex'),
(55, 'Can delete kardex', 14, 'delete_kardex'),
(56, 'Can view kardex', 14, 'view_kardex'),
(57, 'Can add periodo', 15, 'add_periodo'),
(58, 'Can change periodo', 15, 'change_periodo'),
(59, 'Can delete periodo', 15, 'delete_periodo'),
(60, 'Can view periodo', 15, 'view_periodo'),
(61, 'Can add linea periodo', 16, 'add_lineaperiodo'),
(62, 'Can change linea periodo', 16, 'change_lineaperiodo'),
(63, 'Can delete linea periodo', 16, 'delete_lineaperiodo'),
(64, 'Can view linea periodo', 16, 'view_lineaperiodo'),
(65, 'Can add transaccion inventario', 17, 'add_transaccioninventario'),
(66, 'Can change transaccion inventario', 17, 'change_transaccioninventario'),
(67, 'Can delete transaccion inventario', 17, 'delete_transaccioninventario'),
(68, 'Can view transaccion inventario', 17, 'view_transaccioninventario'),
(69, 'Can add empresa', 18, 'add_empresa'),
(70, 'Can change empresa', 18, 'change_empresa'),
(71, 'Can delete empresa', 18, 'delete_empresa'),
(72, 'Can view empresa', 18, 'view_empresa'),
(73, 'Can add transaccion', 19, 'add_transaccion'),
(74, 'Can change transaccion', 19, 'change_transaccion'),
(75, 'Can delete transaccion', 19, 'delete_transaccion'),
(76, 'Can view transaccion', 19, 'view_transaccion'),
(77, 'Can add actualizacion inventario', 20, 'add_actualizacioninventario'),
(78, 'Can change actualizacion inventario', 20, 'change_actualizacioninventario'),
(79, 'Can delete actualizacion inventario', 20, 'delete_actualizacioninventario'),
(80, 'Can view actualizacion inventario', 20, 'view_actualizacioninventario');

-- --------------------------------------------------------

--
-- Table structure for table `categoriaproducto_categoriaproducto`
--

CREATE TABLE IF NOT EXISTS `categoriaproducto_categoriaproducto` (
`idCategoria` int(11) NOT NULL,
  `nombreCategoria` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(1) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `cuenta_cuenta`
--

CREATE TABLE IF NOT EXISTS `cuenta_cuenta` (
`idCuenta` int(11) NOT NULL,
  `codigoCuenta` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `saldo` double NOT NULL,
  `modificaInventario` tinyint(1) NOT NULL,
  `estadoCuenta` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `tipo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `cuentaPadre_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
`id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
`id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=21 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(20, 'actualizacionInventario', 'actualizacioninventario'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(12, 'categoriaProducto', 'categoriaproducto'),
(4, 'contenttypes', 'contenttype'),
(9, 'cuenta', 'cuenta'),
(18, 'empresa', 'empresa'),
(14, 'kardex', 'kardex'),
(16, 'kardex', 'lineaperiodo'),
(15, 'kardex', 'periodo'),
(11, 'marca', 'marca'),
(6, 'modulo', 'modulo'),
(7, 'permiso', 'permiso'),
(13, 'producto', 'producto'),
(5, 'sessions', 'session'),
(19, 'transaccion', 'transaccion'),
(17, 'transaccionInventario', 'transaccioninventario'),
(8, 'usuario', 'usuario'),
(10, 'valorInicial', 'valorinicial');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
`id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=32 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'producto', '0001_initial', '2021-10-22 02:39:14.462555'),
(2, 'transaccionInventario', '0001_initial', '2021-10-22 02:39:14.619547'),
(3, 'kardex', '0001_initial', '2021-10-22 02:39:15.125552'),
(4, 'actualizacionInventario', '0001_initial', '2021-10-22 02:39:15.354551'),
(5, 'modulo', '0001_initial', '2021-10-22 02:39:15.403547'),
(6, 'permiso', '0001_initial', '2021-10-22 02:39:15.765547'),
(7, 'usuario', '0001_initial', '2021-10-22 02:39:15.905551'),
(8, 'contenttypes', '0001_initial', '2021-10-22 02:39:15.988548'),
(9, 'admin', '0001_initial', '2021-10-22 02:39:16.204550'),
(10, 'admin', '0002_logentry_remove_auto_add', '2021-10-22 02:39:16.215556'),
(11, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-22 02:39:16.226547'),
(12, 'contenttypes', '0002_remove_content_type_name', '2021-10-22 02:39:16.373548'),
(13, 'auth', '0001_initial', '2021-10-22 02:39:16.915552'),
(14, 'auth', '0002_alter_permission_name_max_length', '2021-10-22 02:39:16.998555'),
(15, 'auth', '0003_alter_user_email_max_length', '2021-10-22 02:39:17.009548'),
(16, 'auth', '0004_alter_user_username_opts', '2021-10-22 02:39:17.021551'),
(17, 'auth', '0005_alter_user_last_login_null', '2021-10-22 02:39:17.033547'),
(18, 'auth', '0006_require_contenttypes_0002', '2021-10-22 02:39:17.039547'),
(19, 'auth', '0007_alter_validators_add_error_messages', '2021-10-22 02:39:17.049553'),
(20, 'auth', '0008_alter_user_username_max_length', '2021-10-22 02:39:17.061556'),
(21, 'auth', '0009_alter_user_last_name_max_length', '2021-10-22 02:39:17.074552'),
(22, 'auth', '0010_alter_group_name_max_length', '2021-10-22 02:39:17.159555'),
(23, 'auth', '0011_update_proxy_permissions', '2021-10-22 02:39:17.181566'),
(24, 'auth', '0012_alter_user_first_name_max_length', '2021-10-22 02:39:17.193551'),
(25, 'categoriaProducto', '0001_initial', '2021-10-22 02:39:17.255550'),
(26, 'cuenta', '0001_initial', '2021-10-22 02:39:17.403551'),
(27, 'empresa', '0001_initial', '2021-10-22 02:39:17.466547'),
(28, 'marca', '0001_initial', '2021-10-22 02:39:17.520551'),
(29, 'sessions', '0001_initial', '2021-10-22 02:39:17.602554'),
(30, 'transaccion', '0001_initial', '2021-10-22 02:39:17.802554'),
(31, 'valorInicial', '0001_initial', '2021-10-22 02:39:17.938547');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('r9pxs10wecnltc4xq4flttyu6mijzz2u', '.eJxVjssOgjAQRf-la0N4lVJWxr1fYAyZaQeoUmpacWP8d1tDjC7v6-Q-WQ_rferXQL43mnWsYLtfD0FdaUmBvsAyuky55e4NZqmSbWnIjk7TfNi6f4AJwhTXUqimaatCq5o41lxEwWkYUCgpQSjKh4q05ght3ZRY5jUWkgOIUiJUEiI03St2bHEWPUWkAj-7EAOyYOav4c2DyIMU-zH58bCNnRt5a4L7EKzTa1p2p_PrDXibVK4:1mdkjn:eijyJkMQEP4_KSb60_qp6cqlyPFFjgsi0iTZkREzEZc', '2021-11-05 02:56:55.660581');

-- --------------------------------------------------------

--
-- Table structure for table `empresa_empresa`
--

CREATE TABLE IF NOT EXISTS `empresa_empresa` (
`idEmpresa` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nombreContribuyente` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nit` varchar(17) COLLATE utf8_unicode_ci NOT NULL,
  `nrc` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `giro` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kardex_kardex`
--

CREATE TABLE IF NOT EXISTS `kardex_kardex` (
`idKardex` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kardex_lineaperiodo`
--

CREATE TABLE IF NOT EXISTS `kardex_lineaperiodo` (
`idLineaPeriodo` int(11) NOT NULL,
  `factura` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `fecha` date NOT NULL,
  `tipoTransaccion` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `valorUnitario` double NOT NULL,
  `cantidadEntrada` int(11) NOT NULL,
  `valorEntrada` double NOT NULL,
  `cantidadSalida` int(11) NOT NULL,
  `valorSalida` double NOT NULL,
  `cantidadExistencia` int(11) NOT NULL,
  `valorExistencia` double NOT NULL,
  `comprobacion` double NOT NULL,
  `cantidadSobrante` int(11) NOT NULL,
  `compraAsociada` int(11) NOT NULL,
  `periodo_id` int(11) NOT NULL,
  `transaccionInvAsociada_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `kardex_periodo`
--

CREATE TABLE IF NOT EXISTS `kardex_periodo` (
`idPeriodo` int(11) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFinal` date DEFAULT NULL,
  `existenciaFinal` int(11) NOT NULL,
  `saldoFinal` double NOT NULL,
  `kardex_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `marca_marca`
--

CREATE TABLE IF NOT EXISTS `marca_marca` (
`idMarca` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(1) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `modulo_modulo`
--

CREATE TABLE IF NOT EXISTS `modulo_modulo` (
`idModulo` int(11) NOT NULL,
  `nombre` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `permiso_permiso`
--

CREATE TABLE IF NOT EXISTS `permiso_permiso` (
`idPermiso` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `permiso_permiso`
--

INSERT INTO `permiso_permiso` (`idPermiso`, `nombre`) VALUES
(1, 'SU');

-- --------------------------------------------------------

--
-- Table structure for table `permiso_permiso_modulo`
--

CREATE TABLE IF NOT EXISTS `permiso_permiso_modulo` (
`id` int(11) NOT NULL,
  `permiso_id` int(11) NOT NULL,
  `modulo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `producto_producto`
--

CREATE TABLE IF NOT EXISTS `producto_producto` (
`idProducto` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `existencias` int(11) NOT NULL,
  `stockMinimo` int(11) NOT NULL,
  `stockMaximo` int(11) NOT NULL,
  `marca` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `categoria` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `transaccioninventario_transaccioninventario`
--

CREATE TABLE IF NOT EXISTS `transaccioninventario_transaccioninventario` (
`idTransaccionInv` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cantidadTransaccion` int(11) NOT NULL,
  `valorUnitario` double NOT NULL,
  `factura` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `tipo` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `producto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `transaccion_transaccion`
--

CREATE TABLE IF NOT EXISTS `transaccion_transaccion` (
`idTransaccion` int(11) NOT NULL,
  `detalle` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `monto` double NOT NULL,
  `fecha` date NOT NULL,
  `saldoParcial` double DEFAULT NULL,
  `tipo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `cuenta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `usuario_usuario`
--

CREATE TABLE IF NOT EXISTS `usuario_usuario` (
`id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(240) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(240) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `permiso_id` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `usuario_usuario`
--

INSERT INTO `usuario_usuario` (`id`, `password`, `nombre`, `email`, `last_login`, `permiso_id`) VALUES
(1, 'pbkdf2_sha256$260000$LCArciOOVjHcRbyhH3NlJT$ZkcXt6wM1eF+wizRrVTru1zwwHmOfc2q53aPMcBg2RI=', 'carlos', 'carlosriveera97@gmail.com', '2021-10-22 02:56:55.652580', 1);

-- --------------------------------------------------------

--
-- Table structure for table `valorinicial_valorinicial`
--

CREATE TABLE IF NOT EXISTS `valorinicial_valorinicial` (
`idValor` int(11) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFinal` date NOT NULL,
  `saldo` double DEFAULT NULL,
  `estadoCuenta` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `cuenta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1 ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actualizacioninventario_actualizacioninventario`
--
ALTER TABLE `actualizacioninventario_actualizacioninventario`
 ADD PRIMARY KEY (`idActualzacion`), ADD KEY `actualizacionInventa_kardex_id_bc8912d8_fk_kardex_ka` (`kardex_id`), ADD KEY `actualizacionInventa_transaccionInventari_2fe343fa_fk_transacci` (`transaccionInventario_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`), ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `categoriaproducto_categoriaproducto`
--
ALTER TABLE `categoriaproducto_categoriaproducto`
 ADD PRIMARY KEY (`idCategoria`);

--
-- Indexes for table `cuenta_cuenta`
--
ALTER TABLE `cuenta_cuenta`
 ADD PRIMARY KEY (`idCuenta`), ADD UNIQUE KEY `codigoCuenta` (`codigoCuenta`), ADD UNIQUE KEY `nombre` (`nombre`), ADD KEY `cuenta_cuenta_cuentaPadre_id_fd4d066f_fk_cuenta_cuenta_idCuenta` (`cuentaPadre_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
 ADD PRIMARY KEY (`id`), ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`), ADD KEY `django_admin_log_user_id_c564eba6_fk_usuario_usuario_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
 ADD PRIMARY KEY (`session_key`), ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `empresa_empresa`
--
ALTER TABLE `empresa_empresa`
 ADD PRIMARY KEY (`idEmpresa`);

--
-- Indexes for table `kardex_kardex`
--
ALTER TABLE `kardex_kardex`
 ADD PRIMARY KEY (`idKardex`), ADD KEY `kardex_kardex_producto_id_fe81f755_fk_producto_` (`producto_id`);

--
-- Indexes for table `kardex_lineaperiodo`
--
ALTER TABLE `kardex_lineaperiodo`
 ADD PRIMARY KEY (`idLineaPeriodo`), ADD KEY `kardex_lineaperiodo_periodo_id_97257683_fk_kardex_pe` (`periodo_id`), ADD KEY `kardex_lineaperiodo_transaccionInvAsocia_630cfceb_fk_transacci` (`transaccionInvAsociada_id`);

--
-- Indexes for table `kardex_periodo`
--
ALTER TABLE `kardex_periodo`
 ADD PRIMARY KEY (`idPeriodo`), ADD KEY `kardex_periodo_kardex_id_a5a66494_fk_kardex_kardex_idKardex` (`kardex_id`);

--
-- Indexes for table `marca_marca`
--
ALTER TABLE `marca_marca`
 ADD PRIMARY KEY (`idMarca`);

--
-- Indexes for table `modulo_modulo`
--
ALTER TABLE `modulo_modulo`
 ADD PRIMARY KEY (`idModulo`);

--
-- Indexes for table `permiso_permiso`
--
ALTER TABLE `permiso_permiso`
 ADD PRIMARY KEY (`idPermiso`);

--
-- Indexes for table `permiso_permiso_modulo`
--
ALTER TABLE `permiso_permiso_modulo`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `permiso_permiso_modulo_permiso_id_modulo_id_a2c73774_uniq` (`permiso_id`,`modulo_id`), ADD KEY `permiso_permiso_modu_modulo_id_c4633bc4_fk_modulo_mo` (`modulo_id`);

--
-- Indexes for table `producto_producto`
--
ALTER TABLE `producto_producto`
 ADD PRIMARY KEY (`idProducto`);

--
-- Indexes for table `transaccioninventario_transaccioninventario`
--
ALTER TABLE `transaccioninventario_transaccioninventario`
 ADD PRIMARY KEY (`idTransaccionInv`), ADD KEY `transaccionInventari_producto_id_5eacd3b8_fk_producto_` (`producto_id`);

--
-- Indexes for table `transaccion_transaccion`
--
ALTER TABLE `transaccion_transaccion`
 ADD PRIMARY KEY (`idTransaccion`), ADD KEY `transaccion_transacc_cuenta_id_b1e65862_fk_cuenta_cu` (`cuenta_id`);

--
-- Indexes for table `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `email` (`email`), ADD KEY `usuario_usuario_permiso_id_e9b9c1b1_fk_permiso_permiso_idPermiso` (`permiso_id`);

--
-- Indexes for table `valorinicial_valorinicial`
--
ALTER TABLE `valorinicial_valorinicial`
 ADD PRIMARY KEY (`idValor`), ADD KEY `valorInicial_valorin_cuenta_id_91a06165_fk_cuenta_cu` (`cuenta_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actualizacioninventario_actualizacioninventario`
--
ALTER TABLE `actualizacioninventario_actualizacioninventario`
MODIFY `idActualzacion` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=81;
--
-- AUTO_INCREMENT for table `categoriaproducto_categoriaproducto`
--
ALTER TABLE `categoriaproducto_categoriaproducto`
MODIFY `idCategoria` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `cuenta_cuenta`
--
ALTER TABLE `cuenta_cuenta`
MODIFY `idCuenta` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `empresa_empresa`
--
ALTER TABLE `empresa_empresa`
MODIFY `idEmpresa` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `kardex_kardex`
--
ALTER TABLE `kardex_kardex`
MODIFY `idKardex` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `kardex_lineaperiodo`
--
ALTER TABLE `kardex_lineaperiodo`
MODIFY `idLineaPeriodo` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `kardex_periodo`
--
ALTER TABLE `kardex_periodo`
MODIFY `idPeriodo` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `marca_marca`
--
ALTER TABLE `marca_marca`
MODIFY `idMarca` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `modulo_modulo`
--
ALTER TABLE `modulo_modulo`
MODIFY `idModulo` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `permiso_permiso`
--
ALTER TABLE `permiso_permiso`
MODIFY `idPermiso` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `permiso_permiso_modulo`
--
ALTER TABLE `permiso_permiso_modulo`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `producto_producto`
--
ALTER TABLE `producto_producto`
MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `transaccioninventario_transaccioninventario`
--
ALTER TABLE `transaccioninventario_transaccioninventario`
MODIFY `idTransaccionInv` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `transaccion_transaccion`
--
ALTER TABLE `transaccion_transaccion`
MODIFY `idTransaccion` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `valorinicial_valorinicial`
--
ALTER TABLE `valorinicial_valorinicial`
MODIFY `idValor` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `actualizacioninventario_actualizacioninventario`
--
ALTER TABLE `actualizacioninventario_actualizacioninventario`
ADD CONSTRAINT `actualizacionInventa_kardex_id_bc8912d8_fk_kardex_ka` FOREIGN KEY (`kardex_id`) REFERENCES `kardex_kardex` (`idKardex`),
ADD CONSTRAINT `actualizacionInventa_transaccionInventari_2fe343fa_fk_transacci` FOREIGN KEY (`transaccionInventario_id`) REFERENCES `transaccioninventario_transaccioninventario` (`idTransaccionInv`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `cuenta_cuenta`
--
ALTER TABLE `cuenta_cuenta`
ADD CONSTRAINT `cuenta_cuenta_cuentaPadre_id_fd4d066f_fk_cuenta_cuenta_idCuenta` FOREIGN KEY (`cuentaPadre_id`) REFERENCES `cuenta_cuenta` (`idCuenta`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuario_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario_usuario` (`id`);

--
-- Constraints for table `kardex_kardex`
--
ALTER TABLE `kardex_kardex`
ADD CONSTRAINT `kardex_kardex_producto_id_fe81f755_fk_producto_` FOREIGN KEY (`producto_id`) REFERENCES `producto_producto` (`idProducto`);

--
-- Constraints for table `kardex_lineaperiodo`
--
ALTER TABLE `kardex_lineaperiodo`
ADD CONSTRAINT `kardex_lineaperiodo_periodo_id_97257683_fk_kardex_pe` FOREIGN KEY (`periodo_id`) REFERENCES `kardex_periodo` (`idPeriodo`),
ADD CONSTRAINT `kardex_lineaperiodo_transaccionInvAsocia_630cfceb_fk_transacci` FOREIGN KEY (`transaccionInvAsociada_id`) REFERENCES `transaccioninventario_transaccioninventario` (`idTransaccionInv`);

--
-- Constraints for table `kardex_periodo`
--
ALTER TABLE `kardex_periodo`
ADD CONSTRAINT `kardex_periodo_kardex_id_a5a66494_fk_kardex_kardex_idKardex` FOREIGN KEY (`kardex_id`) REFERENCES `kardex_kardex` (`idKardex`);

--
-- Constraints for table `permiso_permiso_modulo`
--
ALTER TABLE `permiso_permiso_modulo`
ADD CONSTRAINT `permiso_permiso_modu_modulo_id_c4633bc4_fk_modulo_mo` FOREIGN KEY (`modulo_id`) REFERENCES `modulo_modulo` (`idModulo`),
ADD CONSTRAINT `permiso_permiso_modu_permiso_id_12a7aaed_fk_permiso_p` FOREIGN KEY (`permiso_id`) REFERENCES `permiso_permiso` (`idPermiso`);

--
-- Constraints for table `transaccioninventario_transaccioninventario`
--
ALTER TABLE `transaccioninventario_transaccioninventario`
ADD CONSTRAINT `transaccionInventari_producto_id_5eacd3b8_fk_producto_` FOREIGN KEY (`producto_id`) REFERENCES `producto_producto` (`idProducto`);

--
-- Constraints for table `transaccion_transaccion`
--
ALTER TABLE `transaccion_transaccion`
ADD CONSTRAINT `transaccion_transacc_cuenta_id_b1e65862_fk_cuenta_cu` FOREIGN KEY (`cuenta_id`) REFERENCES `cuenta_cuenta` (`idCuenta`);

--
-- Constraints for table `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
ADD CONSTRAINT `usuario_usuario_permiso_id_e9b9c1b1_fk_permiso_permiso_idPermiso` FOREIGN KEY (`permiso_id`) REFERENCES `permiso_permiso` (`idPermiso`);

--
-- Constraints for table `valorinicial_valorinicial`
--
ALTER TABLE `valorinicial_valorinicial`
ADD CONSTRAINT `valorInicial_valorin_cuenta_id_91a06165_fk_cuenta_cu` FOREIGN KEY (`cuenta_id`) REFERENCES `cuenta_cuenta` (`idCuenta`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
