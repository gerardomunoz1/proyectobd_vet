-- MySQL dump 10.19  Distrib 10.3.32-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: veterinaria
-- ------------------------------------------------------
-- Server version	10.3.32-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `causa`
--

DROP TABLE IF EXISTS `causa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `causa` (
  `id_diag` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL,
  `observaciones` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_diag`,`id_servicio`),
  KEY `causa_ibfk_2` (`id_servicio`),
  CONSTRAINT `causa_ibfk_1` FOREIGN KEY (`id_diag`) REFERENCES `diagnostico` (`id_diag`),
  CONSTRAINT `causa_ibfk_2` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `causa`
--

LOCK TABLES `causa` WRITE;
/*!40000 ALTER TABLE `causa` DISABLE KEYS */;
INSERT INTO `causa` VALUES (1,2,'no camina'),(1,54,'cojea'),(1,55,'camina lento');
/*!40000 ALTER TABLE `causa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnostico`
--

DROP TABLE IF EXISTS `diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnostico` (
  `id_diag` int(11) NOT NULL AUTO_INCREMENT,
  `nom_diag` varchar(200) NOT NULL,
  PRIMARY KEY (`id_diag`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnostico`
--

LOCK TABLES `diagnostico` WRITE;
/*!40000 ALTER TABLE `diagnostico` DISABLE KEYS */;
INSERT INTO `diagnostico` VALUES (1,'no camina');
/*!40000 ALTER TABLE `diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dueno`
--

DROP TABLE IF EXISTS `dueno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dueno` (
  `id_dueno` int(11) NOT NULL AUTO_INCREMENT,
  `nom_due` varchar(100) NOT NULL,
  `telefono` int(11) NOT NULL,
  `ape_due` varchar(100) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id_dueno`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dueno`
--

LOCK TABLES `dueno` WRITE;
/*!40000 ALTER TABLE `dueno` DISABLE KEYS */;
INSERT INTO `dueno` VALUES (1,'Arturo',3413545,'Soto','mi casa','as@yo.com'),(4,'jose',12345678,'ramirez','su casa','asd@boric1.cl'),(5,'Marcianeke',13131313,'Del corte','El estrellato #1','Marcianeke@trap.cl'),(6,'Pia',93905364,'Medrano','10 sur #3170','pmedrano@gmail.com');
/*!40000 ALTER TABLE `dueno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especie`
--

DROP TABLE IF EXISTS `especie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `especie` (
  `id_especie` int(11) NOT NULL AUTO_INCREMENT,
  `nom_esp` char(50) NOT NULL,
  PRIMARY KEY (`id_especie`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especie`
--

LOCK TABLES `especie` WRITE;
/*!40000 ALTER TABLE `especie` DISABLE KEYS */;
INSERT INTO `especie` VALUES (1,'Perro'),(2,'Gato');
/*!40000 ALTER TABLE `especie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospedaje`
--

DROP TABLE IF EXISTS `hospedaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hospedaje` (
  `dias` int(11) NOT NULL,
  `feha_ing` date NOT NULL,
  `id_servicio` int(11) NOT NULL,
  `id_jaula` int(11) NOT NULL,
  PRIMARY KEY (`id_servicio`,`id_jaula`),
  KEY `hospedaje_ibfk_2` (`id_jaula`),
  CONSTRAINT `hospedaje_ibfk_1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `hospedaje_ibfk_2` FOREIGN KEY (`id_jaula`) REFERENCES `jaula` (`id_jaula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospedaje`
--

LOCK TABLES `hospedaje` WRITE;
/*!40000 ALTER TABLE `hospedaje` DISABLE KEYS */;
INSERT INTO `hospedaje` VALUES (1,'2020-09-09',2,3);
/*!40000 ALTER TABLE `hospedaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jaula`
--

DROP TABLE IF EXISTS `jaula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jaula` (
  `id_jaula` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(200) NOT NULL,
  PRIMARY KEY (`id_jaula`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jaula`
--

LOCK TABLES `jaula` WRITE;
/*!40000 ALTER TABLE `jaula` DISABLE KEYS */;
INSERT INTO `jaula` VALUES (3,'grande'),(4,'jjkn0'),(5,'jjkn0');
/*!40000 ALTER TABLE `jaula` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`vet`@`localhost`*/ /*!50003 TRIGGER tgValidInsertCausa BEFORE INSERT ON jaula
FOR EACH ROW
BEGIN
IF (NEW.descripcion = 'jamon') THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fecha de defunción no puede ser menor a la fecha de nacimiento';
END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `mascota`
--

DROP TABLE IF EXISTS `mascota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mascota` (
  `id_mascota` int(11) NOT NULL AUTO_INCREMENT,
  `nom_masc` varchar(50) NOT NULL,
  `descrip_masc` varchar(200) NOT NULL,
  `id_dueno` int(11) NOT NULL,
  `id_especie` int(11) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  PRIMARY KEY (`id_mascota`),
  KEY `mascota_ibfk_2` (`id_especie`),
  KEY `mascota_ibfk_1` (`id_dueno`),
  CONSTRAINT `mascota_ibfk_1` FOREIGN KEY (`id_dueno`) REFERENCES `dueno` (`id_dueno`),
  CONSTRAINT `mascota_ibfk_2` FOREIGN KEY (`id_especie`) REFERENCES `especie` (`id_especie`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mascota`
--

LOCK TABLES `mascota` WRITE;
/*!40000 ALTER TABLE `mascota` DISABLE KEYS */;
INSERT INTO `mascota` VALUES (3,'jaon','asd',1,2,'2000-02-02'),(9,'gato','jaja',1,1,'2015-02-22'),(13,'fgj','fghj',1,1,'2020-02-02'),(14,'gatuneke','fghj',4,2,'2020-02-02'),(15,'jhamon','jamon',4,2,'2520-02-02'),(16,'gatuneke','gato del corte',1,2,'2010-01-01'),(17,'mascota1','qwe',4,1,'2010-12-23'),(18,'nueva','asd',4,2,'1999-12-15'),(19,'Oddy','blaco, maltes pequinez',6,1,'2017-03-21');
/*!40000 ALTER TABLE `mascota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medico`
--

DROP TABLE IF EXISTS `medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medico` (
  `id_medico` int(11) NOT NULL AUTO_INCREMENT,
  `nom_med` varchar(50) NOT NULL,
  `ape_med` varchar(20) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  PRIMARY KEY (`id_medico`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico`
--

LOCK TABLES `medico` WRITE;
/*!40000 ALTER TABLE `medico` DISABLE KEYS */;
INSERT INTO `medico` VALUES (1,'juna ','junas','1200-02-20'),(3,'juan3','junan','2000-11-11'),(8,'wqe','wqe','2000-02-09'),(9,'sad','wer','2000-03-03');
/*!40000 ALTER TABLE `medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pabellon`
--

DROP TABLE IF EXISTS `pabellon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pabellon` (
  `descripcion` varchar(200) NOT NULL,
  `id_pabellon` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_pabellon`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pabellon`
--

LOCK TABLES `pabellon` WRITE;
/*!40000 ALTER TABLE `pabellon` DISABLE KEYS */;
INSERT INTO `pabellon` VALUES ('Cirugia mayor de animales pequeños',2),('ambulatorio',4);
/*!40000 ALTER TABLE `pabellon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `realizado_por`
--

DROP TABLE IF EXISTS `realizado_por`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `realizado_por` (
  `id_servicio` int(11) NOT NULL,
  `id_medico` int(11) NOT NULL,
  PRIMARY KEY (`id_servicio`,`id_medico`),
  KEY `realizado_por_ibfk_2` (`id_medico`),
  CONSTRAINT `realizado_por_ibfk_1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `realizado_por_ibfk_2` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id_medico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `realizado_por`
--

LOCK TABLES `realizado_por` WRITE;
/*!40000 ALTER TABLE `realizado_por` DISABLE KEYS */;
INSERT INTO `realizado_por` VALUES (2,1),(53,1),(54,1),(55,3);
/*!40000 ALTER TABLE `realizado_por` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `se_realiza_en_`
--

DROP TABLE IF EXISTS `se_realiza_en_`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `se_realiza_en_` (
  `fecha` date NOT NULL,
  `id_servicio` int(11) NOT NULL,
  `id_pabellon` int(11) NOT NULL,
  PRIMARY KEY (`id_servicio`,`id_pabellon`),
  KEY `se_realiza_en__ibfk_2` (`id_pabellon`),
  CONSTRAINT `se_realiza_en__ibfk_1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `se_realiza_en__ibfk_2` FOREIGN KEY (`id_pabellon`) REFERENCES `pabellon` (`id_pabellon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `se_realiza_en_`
--

LOCK TABLES `se_realiza_en_` WRITE;
/*!40000 ALTER TABLE `se_realiza_en_` DISABLE KEYS */;
INSERT INTO `se_realiza_en_` VALUES ('2020-09-09',2,2);
/*!40000 ALTER TABLE `se_realiza_en_` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio`
--

DROP TABLE IF EXISTS `servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio` (
  `id_servicio` int(11) NOT NULL AUTO_INCREMENT,
  `hora` datetime NOT NULL,
  `id_mascota` int(11) DEFAULT NULL,
  `peso` float NOT NULL,
  PRIMARY KEY (`id_servicio`),
  KEY `servicio_ibfk_1` (`id_mascota`),
  CONSTRAINT `servicio_ibfk_1` FOREIGN KEY (`id_mascota`) REFERENCES `mascota` (`id_mascota`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio`
--

LOCK TABLES `servicio` WRITE;
/*!40000 ALTER TABLE `servicio` DISABLE KEYS */;
INSERT INTO `servicio` VALUES (2,'2015-09-09 04:24:00',3,5.5),(3,'2010-02-06 10:20:20',16,3.2),(4,'2021-12-13 19:13:23',16,3.2),(5,'2021-12-13 19:14:23',16,3.2),(6,'2021-12-14 09:55:38',16,3.2),(7,'2021-12-14 12:50:49',14,85),(8,'2021-12-14 12:50:50',14,85),(9,'2021-12-14 12:50:51',14,85),(10,'2021-12-14 12:50:51',14,85),(11,'2021-12-14 12:50:52',14,85),(12,'2021-12-14 12:50:52',14,85),(13,'2021-12-14 12:50:52',14,85),(14,'2021-12-14 12:50:52',14,85),(15,'2021-12-14 12:50:52',14,85),(16,'2021-12-14 12:50:53',14,85),(17,'2021-12-14 12:50:53',14,85),(18,'2021-12-14 12:50:53',14,85),(19,'2021-12-14 12:50:53',14,85),(20,'2021-12-14 12:50:53',14,85),(21,'2021-12-14 12:50:54',14,85),(22,'2021-12-14 12:50:54',14,85),(23,'2021-12-14 12:50:54',14,85),(24,'2021-12-14 12:50:54',14,85),(25,'2021-12-14 12:50:54',14,85),(26,'2021-12-14 12:50:54',14,85),(27,'2021-12-14 12:50:55',14,85),(28,'2021-12-14 12:50:55',14,85),(29,'2021-12-14 12:50:55',14,85),(30,'2021-12-14 12:50:55',14,85),(31,'2021-12-14 12:50:57',14,85),(32,'2021-12-14 12:50:57',14,85),(33,'2021-12-14 12:50:57',14,85),(34,'2021-12-14 12:51:01',14,85),(35,'2021-12-14 12:51:01',14,85),(36,'2021-12-14 12:51:01',14,85),(37,'2021-12-14 12:51:01',14,85),(38,'2021-12-14 12:51:02',14,85),(39,'2021-12-14 12:51:02',14,85),(40,'2021-12-14 12:51:02',14,85),(41,'2021-12-14 12:51:02',14,85),(42,'2021-12-14 12:51:02',14,85),(43,'2021-12-14 12:51:03',14,85),(44,'2021-12-14 12:51:03',14,85),(45,'2021-12-14 12:51:03',14,85),(46,'2021-12-14 12:51:03',14,85),(47,'2021-12-14 12:58:31',9,89),(48,'2021-12-14 14:00:02',13,2.5),(49,'2021-12-14 14:01:17',13,8.2),(50,'2021-12-14 14:03:25',9,8.22),(51,'2021-12-14 14:08:29',14,645),(52,'2021-12-14 14:11:01',13,645),(53,'2021-12-14 14:11:32',9,5),(54,'2021-12-14 15:06:23',14,50),(55,'2021-12-14 15:13:50',13,85);
/*!40000 ALTER TABLE `servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'veterinaria'
--
/*!50003 DROP PROCEDURE IF EXISTS `pr_insert_realizado` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`vet`@`localhost` PROCEDURE `pr_insert_realizado`(id_med int, id_dia int, obs varchar(50))
begin
    declare id_ser int;
    set id_ser = (select max(servicio.id_servicio) from servicio);
    insert into realizado_por(id_servicio, id_medico) VALUES (id_ser, id_med);
    insert into causa(id_diag, id_servicio, observaciones) VALUES (id_dia, id_ser, obs);
end ;;
DELIMITER ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-14 15:25:56
