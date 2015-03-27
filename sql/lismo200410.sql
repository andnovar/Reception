-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 20-04-2010 a las 18:35:10
-- Versión del servidor: 5.1.37
-- Versión de PHP: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `lismo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `department`
--

CREATE TABLE IF NOT EXISTS `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alias` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias` (`alias`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `department`
--

INSERT INTO `department` (`id`, `alias`, `name`, `description`) VALUES
(1, 'FIEC', 'Facultad de Ingenieria en Electricidad y Computación', 'Ofrece carreras de Ingeniería principalmente las que tienen que ver con el desarrollo de Tecnologías nuevas.'),
(2, 'FIMCP', 'Facultad de Ingeniería en Mecánica y Ciencias de la Producción', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `keyword`
--

CREATE TABLE IF NOT EXISTS `keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(30) NOT NULL,
  `level` int(11) DEFAULT NULL,
  `cont` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Volcar la base de datos para la tabla `keyword`
--

INSERT INTO `keyword` (`id`, `word`, `level`,`cont`) VALUES
(1, 'interactive', 2),
(2, 'whiteboard', 2),
(3, 'wiimote', 2),
(4, 'gesture recognition', 2),
(5, 'vision', 2),
(6, 'impaired', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `keywordset`
--

CREATE TABLE IF NOT EXISTS `keywordset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword_id` int(11) NOT NULL,
  `photo_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `researcharea_id` int(11) DEFAULT NULL,
  `publication_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `keywordset_FI_1` (`keyword_id`),
  KEY `keywordset_FI_2` (`photo_id`),
  KEY `keywordset_FI_3` (`person_id`),
  KEY `keywordset_FI_4` (`researcharea_id`),
  KEY `keywordset_FI_5` (`publication_id`),
  KEY `keywordset_FI_6` (`project_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Volcar la base de datos para la tabla `keywordset`
--

INSERT INTO `keywordset` (`id`, `keyword_id`, `photo_id`, `person_id`, `researcharea_id`, `publication_id`, `project_id`) VALUES
(1, 1, NULL, NULL, NULL, 1, NULL),
(2, 2, NULL, NULL, NULL, 1, NULL),
(3, 3, NULL, NULL, NULL, 1, NULL),
(4, 4, NULL, NULL, NULL, 2, NULL),
(5, 5, NULL, NULL, NULL, 2, NULL),
(6, 6, NULL, NULL, NULL, 2, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `members`
--

CREATE TABLE IF NOT EXISTS `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `publication_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `members_FI_1` (`person_id`),
  KEY `members_FI_2` (`publication_id`),
  KEY `members_FI_3` (`project_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Volcar la base de datos para la tabla `members`
--

INSERT INTO `members` (`id`, `person_id`, `publication_id`, `project_id`) VALUES
(1, 1, 1, NULL),
(2, 2, 1, NULL),
(3, 3, 1, NULL),
(4, 1, NULL, 1),
(5, 4, NULL, 1),
(6, 1, 2, NULL),
(7, 5, 2, NULL),
(8, 6, 2, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `person`
--

CREATE TABLE IF NOT EXISTS `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `last` varchar(100) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `researcharea_id` int(11) DEFAULT NULL,
  `ubication_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_U_1` (`email`),
  KEY `person_FI_1` (`researcharea_id`),
  KEY `person_FI_2` (`ubication_id`),
  KEY `person_FI_3` (`department_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Volcar la base de datos para la tabla `person`
--

INSERT INTO `person` (`id`, `name`, `last`, `email`, `position`, `researcharea_id`, `ubication_id`, `department_id`) VALUES
(1, 'Katherine Malena', 'Chiluiza', 'kchilui@gmail.com', 'Directora Programa TCT', 1, 1, 1),
(2, 'Cristina', 'Guerrero Flores', 'cguerrero@cti.espol.edu.ec', 'Ayudante de Investigación', 1, 1, 1),
(3, 'Javier', 'Tibau', 'jtibau@cti.espol.edu.ec', 'Ayudante de Investigación', 1, 1, 1),
(4, 'Andrés', 'Vargas González', 'avargas@cti.espol.edu.ec', 'Ayudante de Investigación', 1, 1, 1),
(5, 'Alejandro', 'Moreno', 'amoreno@cti.espol.edu.ec', 'Ayudante de Investigación', 1, 1, 1),
(6, 'José', 'Oramas', 'joramas@cti.espol.edu.ec', 'Ayudante de Investigación', 1, 1, 1),
(8, 'Enrique', 'Peláez', 'epelaez@cti.espol.edu.ec', 'Director CTI', NULL, 1, 1),
(9, 'Sixto', 'García', 'sgarcia@cti.espol.edu,ec', 'Director TAI Group', 2, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `photo`
--

CREATE TABLE IF NOT EXISTS `photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Volcar la base de datos para la tabla `photo`
--

INSERT INTO `photo` (`id`, `name`, `address`) VALUES
(1, 'Enrique Peláez', 'enriquepelaez.jpg'),
(2, 'Katherine Chiluiza', 'katherinechiluiza.jpg'),
(3, 'Sixto García', 'sixtogarcia.jpg'),
(4, 'Xavier Ochoa', 'xavierochoa.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `photoset`
--

CREATE TABLE IF NOT EXISTS `photoset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `photoset_FI_1` (`photo_id`),
  KEY `photoset_FI_2` (`person_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `photoset`
--

INSERT INTO `photoset` (`id`, `photo_id`, `person_id`) VALUES
(1, 1, 8),
(2, 2, 1),
(3, 3, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `project`
--

CREATE TABLE IF NOT EXISTS `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `project`
--

INSERT INTO `project` (`id`, `name`, `description`) VALUES
(1, 'Sistema Multimedia Interactivo de Busqueda de Info', 'Búsqueda de información por medio de una pantalla multitouch de bajo costo, principalmente la búsqueda se la realiza por palabras de interés.'),
(2, 'Scheduler', 'Generación automática de Horarios de los estudiantes de ESPOL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publication`
--

CREATE TABLE IF NOT EXISTS `publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `year` varchar(4) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Volcar la base de datos para la tabla `publication`
--

INSERT INTO `publication` (`id`, `name`, `year`, `description`) VALUES
(1, 'Issues to Solve for Making an Effective Wiimote Interactive Whiteboard: Evaluation of a Wiimote Schema for Regular ', '2009', 'This paper describes the results of implementing an interactive whiteboard, through the use of infrared tools, as a potential low-cost solution for regular classrooms in Third-World countries. It also shows results observed through the evaluation of the presented technology and a lecture support tool, among regular users. The proposed tool encourages hand-written annotations. The findings reveal some drawbacks of the technology, which should be taken into account for further work on this kind of interfaces.'),
(2, 'A Hand Gestures recognition algorithm based on Xstroke’s Algorithm and an enriched set of rules.', '2009', 'In this paper a novel rule-based approach for hand gestures recognition is proposed. The proposed solution is the use of a modified version of the Grid algorithm employed in Xstroke for the hand gestures recognition problem. In addition to this, the solution is powered by an enriched set of rules, providing an algorithm that is fast enough for real time interaction, is able to recognize gestures from different users and scalable for systems with a wide set of gestures. A sign language recognition system based on this algorithm was built and tested on six hearing-impaired teachers in Ecuador. The validity and effectiveness of this approach is presented.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `research_area`
--

CREATE TABLE IF NOT EXISTS `research_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` varchar(250) DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `research_area`
--

INSERT INTO `research_area` (`id`, `name`, `description`, `alias`) VALUES
(1, 'Trabajo, Colaboración y Telepresencia', 'Estudia el intercambio de información entre las personas y los computadores', 'TCT'),
(2, 'Tecnología como Asistente Inteligente', 'Simula el comportamiento Humano en un computador', 'TAI'),
(3, 'Desarrollo Web', 'Implementación de Aplicaciones Web y Tecnologías actuales de Internet', 'TAWS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubication`
--

CREATE TABLE IF NOT EXISTS `ubication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `latitud` varchar(25) NOT NULL,
  `longitud` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcar la base de datos para la tabla `ubication`
--

INSERT INTO `ubication` (`id`, `name`, `latitud`, `longitud`) VALUES
(1, 'Edificio #37', '34', '54');

--
-- Filtros para las tablas descargadas (dump)
--

--
-- Filtros para la tabla `keywordset`
--
ALTER TABLE `keywordset`
  ADD CONSTRAINT `keywordset_FK_1` FOREIGN KEY (`keyword_id`) REFERENCES `keyword` (`id`),
  ADD CONSTRAINT `keywordset_FK_2` FOREIGN KEY (`photo_id`) REFERENCES `photo` (`id`),
  ADD CONSTRAINT `keywordset_FK_3` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  ADD CONSTRAINT `keywordset_FK_4` FOREIGN KEY (`researcharea_id`) REFERENCES `research_area` (`id`),
  ADD CONSTRAINT `keywordset_FK_5` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`id`),
  ADD CONSTRAINT `keywordset_FK_6` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`);

--
-- Filtros para la tabla `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `members_FK_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  ADD CONSTRAINT `members_FK_2` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`id`),
  ADD CONSTRAINT `members_FK_3` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`);

--
-- Filtros para la tabla `person`
--
ALTER TABLE `person`
  ADD CONSTRAINT `person_FK_1` FOREIGN KEY (`researcharea_id`) REFERENCES `research_area` (`id`),
  ADD CONSTRAINT `person_FK_2` FOREIGN KEY (`ubication_id`) REFERENCES `ubication` (`id`),
  ADD CONSTRAINT `person_FK_3` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);

--
-- Filtros para la tabla `photoset`
--
ALTER TABLE `photoset`
  ADD CONSTRAINT `photoset_FK_1` FOREIGN KEY (`photo_id`) REFERENCES `photo` (`id`),
  ADD CONSTRAINT `photoset_FK_2` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
