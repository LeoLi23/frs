-- MySQL dump 10.13  Distrib 8.0.22, for osx10.16 (x86_64)
--
-- Host: localhost    Database: frs
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `frs`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `frs2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE `frs2`;

--
-- Table structure for table `agent_purchase`
--

DROP TABLE IF EXISTS `agent_purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agent_purchase` (
  `agent_email` varchar(50) NOT NULL,
  `agent_id` varchar(30) NOT NULL,
  `ticket_id` varchar(30) NOT NULL,
  `customer_email` varchar(30) NOT NULL,
  `card_type` varchar(30) NOT NULL,
  `card_num` varchar(30) NOT NULL,
  `name_on_card` varchar(30) NOT NULL,
  `expire_at` datetime NOT NULL,
  `purchase_date` date NOT NULL,
  `purchase_time` time NOT NULL,
  PRIMARY KEY (`agent_email`,`agent_id`,`ticket_id`,`customer_email`),
  KEY `agent_purchase_customer_email_e2a96a13_fk_customer_email` (`customer_email`),
  KEY `agent_purchase_ticket_id_49a0d556_fk_ticket_ticket_id` (`ticket_id`),
  CONSTRAINT `agent_purchase_customer_email_e2a96a13_fk_customer_email` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`),
  CONSTRAINT `agent_purchase_ibfk_1` FOREIGN KEY (`agent_email`, `agent_id`) REFERENCES `booking_agent` (`agent_email`, `agent_id`),
  CONSTRAINT `agent_purchase_ticket_id_49a0d556_fk_ticket_ticket_id` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agent_purchase`
--

LOCK TABLES `agent_purchase` WRITE;
/*!40000 ALTER TABLE `agent_purchase` DISABLE KEYS */;
INSERT INTO `agent_purchase` VALUES ('agent1@gmail.com','A123','A002','cust2@gmail.com','Debit','2222-2222-3333-3333','Lucy','2024-01-01 00:00:00','2021-03-23','02:26:38'),('agent1@gmail.com','A123','D002','cust2@gmail.com','Credit','1111-2222-3333-4444','Lucy','2023-03-09 00:00:00','2021-03-01','02:40:27'),('agent1@gmail.com','A123','E401','cust3@gmail.com','Credit','1234-2342-5444','Johnson','2025-01-01 00:00:00','2021-04-20','14:24:31'),('agent1@gmail.com','A123','E403','cust2@gmail.com','credit','1435-2534-8788','Lucy','2023-11-01 00:00:00','2021-05-05','00:37:16');
/*!40000 ALTER TABLE `agent_purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airline`
--

DROP TABLE IF EXISTS `airline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airline` (
  `airline_name` varchar(255) NOT NULL,
  PRIMARY KEY (`airline_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airline`
--

LOCK TABLES `airline` WRITE;
/*!40000 ALTER TABLE `airline` DISABLE KEYS */;
INSERT INTO `airline` VALUES ('China Eastern'),('China Southern'),('Delta'),('Emirate');
/*!40000 ALTER TABLE `airline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airplane`
--

DROP TABLE IF EXISTS `airplane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airplane` (
  `ID` varchar(30) NOT NULL,
  `airline_name` varchar(30) NOT NULL,
  `seats` int NOT NULL,
  `capacity` int NOT NULL,
  PRIMARY KEY (`ID`,`airline_name`),
  KEY `airplane_airline_name_e8938dc7_fk_airline_airline_name` (`airline_name`),
  CONSTRAINT `airplane_airline_name_e8938dc7_fk_airline_airline_name` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airplane`
--

LOCK TABLES `airplane` WRITE;
/*!40000 ALTER TABLE `airplane` DISABLE KEYS */;
INSERT INTO `airplane` VALUES ('Boeing-300','China Eastern',500,500),('Boeing-777','Delta',300,300),('Em-777','Emirate',194,200),('Em-888','Emirate',350,350),('Em-921','Emirate',400,400),('Em-987','Emirate',444,444),('Model-123','China Eastern',900,900),('Model-1459','Delta',200,200),('Model-199','China Eastern',1100,1100),('Model-999','Delta',455,455);
/*!40000 ALTER TABLE `airplane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `name` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES ('CHN','Guangzhou'),('JFK','NYC'),('LAX','Los Angeles '),('PVG','Shanghai'),('SFO','San Francisco');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=169 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add airline',7,'add_airline'),(26,'Can change airline',7,'change_airline'),(27,'Can delete airline',7,'delete_airline'),(28,'Can view airline',7,'view_airline'),(29,'Can add airplane',8,'add_airplane'),(30,'Can change airplane',8,'change_airplane'),(31,'Can delete airplane',8,'delete_airplane'),(32,'Can view airplane',8,'view_airplane'),(33,'Can add airport',9,'add_airport'),(34,'Can change airport',9,'change_airport'),(35,'Can delete airport',9,'delete_airport'),(36,'Can view airport',9,'view_airport'),(37,'Can add booking agent',10,'add_bookingagent'),(38,'Can change booking agent',10,'change_bookingagent'),(39,'Can delete booking agent',10,'delete_bookingagent'),(40,'Can view booking agent',10,'view_bookingagent'),(41,'Can add customer',11,'add_customer'),(42,'Can change customer',11,'change_customer'),(43,'Can delete customer',11,'delete_customer'),(44,'Can view customer',11,'view_customer'),(45,'Can add staff',12,'add_staff'),(46,'Can change staff',12,'change_staff'),(47,'Can delete staff',12,'delete_staff'),(48,'Can view staff',12,'view_staff'),(49,'Can add ticket',13,'add_ticket'),(50,'Can change ticket',13,'change_ticket'),(51,'Can delete ticket',13,'delete_ticket'),(52,'Can view ticket',13,'view_ticket'),(53,'Can add agent purchase',14,'add_agentpurchase'),(54,'Can change agent purchase',14,'change_agentpurchase'),(55,'Can delete agent purchase',14,'delete_agentpurchase'),(56,'Can view agent purchase',14,'view_agentpurchase'),(57,'Can add customer purchase',15,'add_customerpurchase'),(58,'Can change customer purchase',15,'change_customerpurchase'),(59,'Can delete customer purchase',15,'delete_customerpurchase'),(60,'Can view customer purchase',15,'view_customerpurchase'),(61,'Can add flight',16,'add_flight'),(62,'Can change flight',16,'change_flight'),(63,'Can delete flight',16,'delete_flight'),(64,'Can view flight',16,'view_flight'),(65,'Can add phone num',17,'add_phonenum'),(66,'Can change phone num',17,'change_phonenum'),(67,'Can delete phone num',17,'delete_phonenum'),(68,'Can view phone num',17,'view_phonenum'),(69,'Can add rate',18,'add_rate'),(70,'Can change rate',18,'change_rate'),(71,'Can delete rate',18,'delete_rate'),(72,'Can view rate',18,'view_rate'),(73,'Can add airline',19,'add_airline'),(74,'Can change airline',19,'change_airline'),(75,'Can delete airline',19,'delete_airline'),(76,'Can view airline',19,'view_airline'),(77,'Can add airplane',20,'add_airplane'),(78,'Can change airplane',20,'change_airplane'),(79,'Can delete airplane',20,'delete_airplane'),(80,'Can view airplane',20,'view_airplane'),(81,'Can add airport',21,'add_airport'),(82,'Can change airport',21,'change_airport'),(83,'Can delete airport',21,'delete_airport'),(84,'Can view airport',21,'view_airport'),(85,'Can add booking agent',22,'add_bookingagent'),(86,'Can change booking agent',22,'change_bookingagent'),(87,'Can delete booking agent',22,'delete_bookingagent'),(88,'Can view booking agent',22,'view_bookingagent'),(89,'Can add customer',23,'add_customer'),(90,'Can change customer',23,'change_customer'),(91,'Can delete customer',23,'delete_customer'),(92,'Can view customer',23,'view_customer'),(93,'Can add staff',24,'add_staff'),(94,'Can change staff',24,'change_staff'),(95,'Can delete staff',24,'delete_staff'),(96,'Can view staff',24,'view_staff'),(97,'Can add ticket',25,'add_ticket'),(98,'Can change ticket',25,'change_ticket'),(99,'Can delete ticket',25,'delete_ticket'),(100,'Can view ticket',25,'view_ticket'),(101,'Can add agent purchase',26,'add_agentpurchase'),(102,'Can change agent purchase',26,'change_agentpurchase'),(103,'Can delete agent purchase',26,'delete_agentpurchase'),(104,'Can view agent purchase',26,'view_agentpurchase'),(105,'Can add customer purchase',27,'add_customerpurchase'),(106,'Can change customer purchase',27,'change_customerpurchase'),(107,'Can delete customer purchase',27,'delete_customerpurchase'),(108,'Can view customer purchase',27,'view_customerpurchase'),(109,'Can add flight',28,'add_flight'),(110,'Can change flight',28,'change_flight'),(111,'Can delete flight',28,'delete_flight'),(112,'Can view flight',28,'view_flight'),(113,'Can add phone num',29,'add_phonenum'),(114,'Can change phone num',29,'change_phonenum'),(115,'Can delete phone num',29,'delete_phonenum'),(116,'Can view phone num',29,'view_phonenum'),(117,'Can add rate',30,'add_rate'),(118,'Can change rate',30,'change_rate'),(119,'Can delete rate',30,'delete_rate'),(120,'Can view rate',30,'view_rate'),(121,'Can add ticket',35,'add_ticket'),(122,'Can change ticket',35,'change_ticket'),(123,'Can delete ticket',35,'delete_ticket'),(124,'Can view ticket',35,'view_ticket'),(125,'Can add airplane',36,'add_airplane'),(126,'Can change airplane',36,'change_airplane'),(127,'Can delete airplane',36,'delete_airplane'),(128,'Can view airplane',36,'view_airplane'),(129,'Can add phone num',37,'add_phonenum'),(130,'Can change phone num',37,'change_phonenum'),(131,'Can delete phone num',37,'delete_phonenum'),(132,'Can view phone num',37,'view_phonenum'),(133,'Can add airline',38,'add_airline'),(134,'Can change airline',38,'change_airline'),(135,'Can delete airline',38,'delete_airline'),(136,'Can view airline',38,'view_airline'),(137,'Can add booking agent',39,'add_bookingagent'),(138,'Can change booking agent',39,'change_bookingagent'),(139,'Can delete booking agent',39,'delete_bookingagent'),(140,'Can view booking agent',39,'view_bookingagent'),(141,'Can add customer purchase',40,'add_customerpurchase'),(142,'Can change customer purchase',40,'change_customerpurchase'),(143,'Can delete customer purchase',40,'delete_customerpurchase'),(144,'Can view customer purchase',40,'view_customerpurchase'),(145,'Can add staff',33,'add_staff'),(146,'Can change staff',33,'change_staff'),(147,'Can delete staff',33,'delete_staff'),(148,'Can view staff',33,'view_staff'),(149,'Can add rate',41,'add_rate'),(150,'Can change rate',41,'change_rate'),(151,'Can delete rate',41,'delete_rate'),(152,'Can view rate',41,'view_rate'),(153,'Can add agent purchase',42,'add_agentpurchase'),(154,'Can change agent purchase',42,'change_agentpurchase'),(155,'Can delete agent purchase',42,'delete_agentpurchase'),(156,'Can view agent purchase',42,'view_agentpurchase'),(157,'Can add airport',43,'add_airport'),(158,'Can change airport',43,'change_airport'),(159,'Can delete airport',43,'delete_airport'),(160,'Can view airport',43,'view_airport'),(161,'Can add customer',34,'add_customer'),(162,'Can change customer',34,'change_customer'),(163,'Can delete customer',34,'delete_customer'),(164,'Can view customer',34,'view_customer'),(165,'Can add flight',44,'add_flight'),(166,'Can change flight',44,'change_flight'),(167,'Can delete flight',44,'delete_flight'),(168,'Can view flight',44,'view_flight');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$216000$tpC7BCq9gSYO$mDXKZqJTuLrjFqrBCM35U/ovxTBiJlY2KHnKvtyrdbY=','2021-04-18 00:09:45.662108',1,'lianyang','','','lianyang617@gmail.com',1,1,'2021-04-07 00:29:33.401289');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_agent`
--

DROP TABLE IF EXISTS `booking_agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_agent` (
  `agent_email` varchar(50) NOT NULL,
  `agent_id` varchar(30) NOT NULL,
  `agent_password` varchar(255) NOT NULL,
  PRIMARY KEY (`agent_email`,`agent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_agent`
--

LOCK TABLES `booking_agent` WRITE;
/*!40000 ALTER TABLE `booking_agent` DISABLE KEYS */;
INSERT INTO `booking_agent` VALUES ('agent1@gmail.com','A123','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3'),('agent2@gmail.com','453d','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3');
/*!40000 ALTER TABLE `booking_agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `building_num` varchar(10) NOT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `phone_num` varchar(30) NOT NULL,
  `passport_num` varchar(20) NOT NULL,
  `passport_country` varchar(30) NOT NULL,
  `passport_expire` varchar(50) NOT NULL,
  `date_of_birth` datetime NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('cust1@gmail.com','John','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3','123','Jay Street','New York','NY','19348193','36712489','China','2024-01-01','2000-01-03 00:00:00'),('cust2@gmail.com','Lucy','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3','123','6 Metrotech','Miami','Florida','473828','273847','United States','2023-04-02','2000-01-13 00:00:00'),('cust3@gmail.com','Johnson','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3','455','xxx street','Bronx','NY','12345122','2738492','UK','2023-04-04','2002-03-04 00:00:00');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_purchase`
--

DROP TABLE IF EXISTS `customer_purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_purchase` (
  `customer_email` varchar(50) NOT NULL,
  `ticket_id` varchar(30) NOT NULL,
  `card_type` varchar(30) NOT NULL,
  `card_num` varchar(30) NOT NULL,
  `name_on_card` varchar(30) NOT NULL,
  `expire_at` datetime NOT NULL,
  `purchase_date` date NOT NULL,
  `purchase_time` time NOT NULL,
  PRIMARY KEY (`customer_email`,`ticket_id`),
  KEY `customer_purchase_ibfk_2` (`ticket_id`),
  CONSTRAINT `customer_purchase_customer_email_629523f8_fk_customer_email` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `customer_purchase_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_purchase`
--

LOCK TABLES `customer_purchase` WRITE;
/*!40000 ALTER TABLE `customer_purchase` DISABLE KEYS */;
INSERT INTO `customer_purchase` VALUES ('cust1@gmail.com','A001','Credit','1234-1234-1234-1234','John','2024-03-03 00:00:00','2020-10-10','02:04:02'),('cust1@gmail.com','D001','Debit','4444-1234-7899-6533','John','2024-01-01 00:00:00','2020-11-19','01:53:05'),('cust1@gmail.com','E001','Debit','12341435','John','2024-09-09 00:00:00','2021-02-04','17:21:30'),('cust1@gmail.com','E231','Credit','2312-4135','John','2025-04-12 00:00:00','2021-04-19','16:38:27'),('cust1@gmail.com','E402','debit','1234-2333-1111','John','2023-07-07 00:00:00','2021-05-05','00:31:49'),('cust2@gmail.com','E101','Credit','1111-2222-3333','Lucy','2026-03-03 00:00:00','2020-05-05','19:38:27'),('cust2@gmail.com','E232','Credit','1111-2222-3333','Lucy','2026-03-03 00:00:00','2021-04-13','21:00:35'),('cust2@gmail.com','E301','Credit','1111-2222-3333','Lucy','2026-03-03 00:00:00','2020-06-08','19:12:27'),('cust3@gmail.com','E233','Debit','2333-5432-1234','James','2024-03-04 00:00:00','2021-04-15','21:32:07'),('cust3@gmail.com','E302','Debit','2333-5432-1234','James','2024-03-04 00:00:00','2020-04-17','08:32:07');
/*!40000 ALTER TABLE `customer_purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(42,'App','agentpurchase'),(38,'App','airline'),(36,'App','airplane'),(43,'App','airport'),(39,'App','bookingagent'),(34,'App','customer'),(40,'App','customerpurchase'),(44,'App','flight'),(37,'App','phonenum'),(41,'App','rate'),(33,'App','staff'),(35,'App','ticket'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(14,'booking_system','agentpurchase'),(7,'booking_system','airline'),(8,'booking_system','airplane'),(9,'booking_system','airport'),(10,'booking_system','bookingagent'),(11,'booking_system','customer'),(15,'booking_system','customerpurchase'),(16,'booking_system','flight'),(17,'booking_system','phonenum'),(18,'booking_system','rate'),(12,'booking_system','staff'),(13,'booking_system','ticket'),(5,'contenttypes','contenttype'),(31,'Customer','airline'),(32,'Customer','staff'),(6,'sessions','session'),(26,'users','agentpurchase'),(19,'users','airline'),(20,'users','airplane'),(21,'users','airport'),(22,'users','bookingagent'),(23,'users','customer'),(27,'users','customerpurchase'),(28,'users','flight'),(29,'users','phonenum'),(30,'users','rate'),(24,'users','staff'),(25,'users','ticket');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-06 18:25:12.261941'),(2,'auth','0001_initial','2021-04-06 18:25:12.323235'),(3,'admin','0001_initial','2021-04-06 18:25:12.457045'),(4,'admin','0002_logentry_remove_auto_add','2021-04-06 18:25:12.497378'),(5,'admin','0003_logentry_add_action_flag_choices','2021-04-06 18:25:12.505359'),(6,'contenttypes','0002_remove_content_type_name','2021-04-06 18:25:12.549695'),(7,'auth','0002_alter_permission_name_max_length','2021-04-06 18:25:12.575203'),(8,'auth','0003_alter_user_email_max_length','2021-04-06 18:25:12.593005'),(9,'auth','0004_alter_user_username_opts','2021-04-06 18:25:12.600441'),(10,'auth','0005_alter_user_last_login_null','2021-04-06 18:25:12.627148'),(11,'auth','0006_require_contenttypes_0002','2021-04-06 18:25:12.629182'),(12,'auth','0007_alter_validators_add_error_messages','2021-04-06 18:25:12.637756'),(13,'auth','0008_alter_user_username_max_length','2021-04-06 18:25:12.665141'),(14,'auth','0009_alter_user_last_name_max_length','2021-04-06 18:25:12.691221'),(15,'auth','0010_alter_group_name_max_length','2021-04-06 18:25:12.707802'),(16,'auth','0011_update_proxy_permissions','2021-04-06 18:25:12.716709'),(17,'auth','0012_alter_user_first_name_max_length','2021-04-06 18:25:12.747217'),(18,'booking_system','0001_initial','2021-04-06 18:25:12.765138'),(19,'sessions','0001_initial','2021-04-06 18:25:12.806989'),(20,'booking_system','0002_auto_20210406_1829','2021-04-06 18:29:12.631985'),(21,'users','0001_initial','2021-04-06 23:24:19.227011'),(22,'users','0002_auto_20210406_1829','2021-04-06 23:24:19.263994'),(23,'App','0001_initial','2021-04-07 12:11:23.601188'),(24,'App','0002_auto_20210410_1753','2021-04-10 17:54:07.558269');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0dwyuhbp8rb600e6b7dv75ynrqdja8um','.eJxVjEsOwiAUAO_C2pDyB5fuewby-h5I1UBS2pXx7oakC93OTObNIhx7iUdPW1yJXZlkl1-2AD5THYIeUO-NY6v7ti58JPy0nc-N0ut2tn-DAr2MrcjKk0UvYUISQWiBQbjkpAoQnFbWkMqgbTISSOMERNlbpx0Yg9qzzxfOjzd7:1leBfu:8RpzezCkBMG6cUWnO7tc9l1td9AzibEnfXmVgLmb_7g','2021-05-19 15:10:26.649816'),('hvip3uxfndqijaek11iftx4gonx24k2r','.eJxVzjsOwjAQBNC7uEZW_LepED1niDa7dhzIR4qTCnF3YikFtDOjp3mzFvYtt3uJazsQuzLJLr9ZB_iKcy3oCXO_cFzmbR06Xif8bAt_LBTH-7n9AzKUXFmRlCeLXkKDJILQAoNw0UkVIDitrCGVQNtoJJDGBoiSt047MAa1P9DKHRLuZRO3foJhPM5M7PMFn0M_zw:1lVySC:eEuZN-Zcf6BerLa3x7qwBBW4Lvef7hwxnhrCWfvgt8M','2021-04-26 23:26:20.393075'),('rco54d77idqcjrngk43wxhpepulvbmdk','.eJxVzjsOwjAQBNC7uEZW_LepED1niDa7dhzIR4qTCnF3YikFtDOjp3mzFvYtt3uJazsQuzLJLr9ZB_iKcy3oCXO_cFzmbR06Xif8bAt_LBTH-7n9AzKUXFmRlCeLXkKDJILQAoNw0UkVIDitrCGVQNtoJJDGBoiSt047MAa1P9DKHRLuZRO3foJhPM5M7PMFn0M_zw:1lVDmI:j_rZnQRUrHwB_gylJCglgmVc_p0XvBLYBgHBda8RZ34','2021-04-24 21:35:58.510839');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `airline_name` varchar(30) NOT NULL,
  `flight_num` varchar(30) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  `arrival_date` date NOT NULL,
  `arrival_time` time NOT NULL,
  `airplane_id` varchar(30) NOT NULL,
  `base_price` varchar(11) NOT NULL,
  `status` varchar(11) NOT NULL,
  `arrive_airport_name` varchar(50) NOT NULL,
  `depart_airport_name` varchar(50) NOT NULL,
  PRIMARY KEY (`airline_name`,`flight_num`,`depart_date`,`depart_time`),
  KEY `flight_arrive_airport_name_c247e2f1_fk_airport_name` (`arrive_airport_name`),
  KEY `flight_depart_airport_name_4b15384d_fk_airport_name` (`depart_airport_name`),
  KEY `flight_ibfk_1` (`airplane_id`,`airline_name`),
  CONSTRAINT `flight_airline_name_71cf209f_fk_airline_airline_name` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_arrive_airport_name_c247e2f1_fk_airport_name` FOREIGN KEY (`arrive_airport_name`) REFERENCES `airport` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_depart_airport_name_4b15384d_fk_airport_name` FOREIGN KEY (`depart_airport_name`) REFERENCES `airport` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airplane_id`, `airline_name`) REFERENCES `airplane` (`ID`, `airline_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES ('China Eastern','CE123','2020-04-19','14:23:00','2020-04-20','10:00:00','Boeing-300','1000','delayed','PVG','JFK'),('Delta','D1233','2020-04-14','13:30:00','2020-04-15','16:40:00','Boeing-777','500','on-time','JFK','PVG'),('Delta','D1244','2020-04-06','13:30:00','2020-04-07','16:40:00','Boeing-777','500','delayed','JFK','PVG'),('Emirate','E0000','2021-05-27','17:17:00','2021-05-28','18:19:00','Em-987','211','delayed','JFK','LAX'),('Emirate','E0122','2020-09-23','23:44:00','2020-09-24','11:24:00','Em-987','500','on-time','PVG','JFK'),('Emirate','E0342','2020-08-12','20:16:00','2020-08-13','09:23:00','Em-987','430','delayed','PVG','JFK'),('Emirate','E1111','2021-04-20','06:00:00','2021-04-21','18:00:00','Em-777','300','on-time','SFO','JFK'),('Emirate','E2233','2021-04-25','13:00:00','2021-04-26','06:00:00','Em-777','240','on-time','PVG','JFK'),('Emirate','E3333','2021-05-21','16:00:00','2021-05-22','13:21:00','Em-987','499','on-time','PVG','CHN'),('Emirate','E4432','2021-06-03','12:00:00','2021-06-04','09:00:00','Em-777','300','delayed','PVG','SFO'),('Emirate','E4435','2021-05-02','13:23:00','2021-05-03','09:00:00','Em-777','455','on-time','SFO','PVG'),('Emirate','E5432','2021-05-01','20:16:00','2021-05-02','08:20:00','Em-777','432','delayed','SFO','PVG'),('Emirate','E9191','2021-03-30','16:27:00','2021-04-01','15:29:00','Em-987','199','on-time','CHN','PVG');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone_num`
--

DROP TABLE IF EXISTS `phone_num`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone_num` (
  `username` varchar(30) NOT NULL,
  `number` varchar(30) NOT NULL,
  PRIMARY KEY (`username`,`number`),
  CONSTRAINT `phone_num_username_bc6c3de7_fk_staff_username` FOREIGN KEY (`username`) REFERENCES `staff` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_num`
--

LOCK TABLES `phone_num` WRITE;
/*!40000 ALTER TABLE `phone_num` DISABLE KEYS */;
/*!40000 ALTER TABLE `phone_num` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate` (
  `customer_email` varchar(50) NOT NULL,
  `airline_name` varchar(30) NOT NULL,
  `flight_num` varchar(30) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_email`,`airline_name`,`flight_num`,`depart_time`,`depart_date`),
  KEY `rate_ibfk_2` (`airline_name`,`flight_num`,`depart_date`,`depart_time`),
  CONSTRAINT `rate_customer_email_93a46bcf_fk_customer_email` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rate_ibfk_2` FOREIGN KEY (`airline_name`, `flight_num`, `depart_date`, `depart_time`) REFERENCES `flight` (`airline_name`, `flight_num`, `depart_date`, `depart_time`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` VALUES ('cust1@gmail.com','China Eastern','CE123','2020-04-19','14:23:00','Great trip!',7,'2021-04-19 15:35:05'),('cust1@gmail.com','Emirate','E2233','2021-04-25','13:00:00','bad',7,'2021-05-01 15:00:20'),('cust2@gmail.com','Emirate','E0122','2020-09-23','23:44:00','lalala',9,'2021-05-05 06:16:07'),('cust2@gmail.com','Emirate','E2233','2021-04-25','13:00:00','I love this trip!',9,'2021-04-26 13:11:32'),('cust3@gmail.com','Emirate','E2233','2021-04-25','13:00:00','Not a good trip!',5,'2021-04-26 13:33:18');
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `f_name` varchar(30) NOT NULL,
  `l_name` varchar(30) NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `airline_name` varchar(30) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `staff_airline_name_a0016044_fk_airline_airline_name` (`airline_name`),
  CONSTRAINT `staff_airline_name_a0016044_fk_airline_airline_name` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('staff1','504a98573c8c8f6bc92701002f8c693c6727998af12ed2724887fb59ec886ff3','Leo','Li','2002-03-04 00:00:00','Emirate');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `ticket_id` varchar(11) NOT NULL,
  `sold_price` float NOT NULL,
  `airline_name` varchar(50) NOT NULL,
  `flight_num` varchar(30) NOT NULL,
  `depart_date` date NOT NULL,
  `depart_time` time NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `ticket_ibfk_1` (`airline_name`,`flight_num`,`depart_date`,`depart_time`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`airline_name`, `flight_num`, `depart_date`, `depart_time`) REFERENCES `flight` (`airline_name`, `flight_num`, `depart_date`, `depart_time`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES ('322FD9kd87Q',211,'Emirate','E0000','2021-05-27','17:17:00'),('324BffwJXRw',199,'Emirate','E9191','2021-03-30','16:27:00'),('325UzEP5jrQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('32BgZzTopWY',211,'Emirate','E0000','2021-05-27','17:17:00'),('32fJqtZjhBG',211,'Emirate','E0000','2021-05-27','17:17:00'),('32G7dRSyYe6',211,'Emirate','E0000','2021-05-27','17:17:00'),('32GTewjeGCP',211,'Emirate','E0000','2021-05-27','17:17:00'),('32iy2AjSzKz',199,'Emirate','E9191','2021-03-30','16:27:00'),('32jNbMhrKcE',199,'Emirate','E9191','2021-03-30','16:27:00'),('32u4H3V9Rre',199,'Emirate','E9191','2021-03-30','16:27:00'),('32xfEVNvGP4',199,'Emirate','E9191','2021-03-30','16:27:00'),('32ZAx2wBTZr',211,'Emirate','E0000','2021-05-27','17:17:00'),('32ZpppmRLnX',199,'Emirate','E9191','2021-03-30','16:27:00'),('333Lhnw6FJU',199,'Emirate','E9191','2021-03-30','16:27:00'),('3373Fq8R8S4',199,'Emirate','E9191','2021-03-30','16:27:00'),('339hSGkoo7t',211,'Emirate','E0000','2021-05-27','17:17:00'),('33a4b7Aerh4',199,'Emirate','E9191','2021-03-30','16:27:00'),('33AdLHV7Wi3',199,'Emirate','E9191','2021-03-30','16:27:00'),('33aZHv7zsgp',211,'Emirate','E0000','2021-05-27','17:17:00'),('33Dg2rD3sg4',211,'Emirate','E0000','2021-05-27','17:17:00'),('33eWt7F6fT4',211,'Emirate','E0000','2021-05-27','17:17:00'),('33FgezFuTYW',199,'Emirate','E9191','2021-03-30','16:27:00'),('33gVih3KbBJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('33Lx656zt2Q',211,'Emirate','E0000','2021-05-27','17:17:00'),('33Mhfd3SGE7',199,'Emirate','E9191','2021-03-30','16:27:00'),('33oPMpZLarg',199,'Emirate','E9191','2021-03-30','16:27:00'),('33pEg7NyVgc',211,'Emirate','E0000','2021-05-27','17:17:00'),('33Pjp9mzjVS',199,'Emirate','E9191','2021-03-30','16:27:00'),('33pJPRGD7sU',211,'Emirate','E0000','2021-05-27','17:17:00'),('33qHykLvFyJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('33QVngLsP2e',199,'Emirate','E9191','2021-03-30','16:27:00'),('33TLY7bN3JW',199,'Emirate','E9191','2021-03-30','16:27:00'),('348KRPQTPFe',199,'Emirate','E9191','2021-03-30','16:27:00'),('34GAbRMiHTd',211,'Emirate','E0000','2021-05-27','17:17:00'),('34hHQ5y4UKa',211,'Emirate','E0000','2021-05-27','17:17:00'),('34JT3UaV4bu',199,'Emirate','E9191','2021-03-30','16:27:00'),('34kXCKT2RXE',199,'Emirate','E9191','2021-03-30','16:27:00'),('34MRTBHYbZU',211,'Emirate','E0000','2021-05-27','17:17:00'),('34pooK6RrTX',211,'Emirate','E0000','2021-05-27','17:17:00'),('34vpsSiqYp3',211,'Emirate','E0000','2021-05-27','17:17:00'),('34XpJLuPkq5',211,'Emirate','E0000','2021-05-27','17:17:00'),('34yg6LnJNMz',211,'Emirate','E0000','2021-05-27','17:17:00'),('359JbNcx67u',199,'Emirate','E9191','2021-03-30','16:27:00'),('35APAkahKPW',211,'Emirate','E0000','2021-05-27','17:17:00'),('35CMiVxo28g',211,'Emirate','E0000','2021-05-27','17:17:00'),('35CwmCZEGi5',199,'Emirate','E9191','2021-03-30','16:27:00'),('35iCqYVsp9h',211,'Emirate','E0000','2021-05-27','17:17:00'),('35KDkczaZum',199,'Emirate','E9191','2021-03-30','16:27:00'),('35M5HkNoMT6',199,'Emirate','E9191','2021-03-30','16:27:00'),('35rheY8fvZD',211,'Emirate','E0000','2021-05-27','17:17:00'),('35rQTt8Z3v7',199,'Emirate','E9191','2021-03-30','16:27:00'),('35tYUmESxVx',199,'Emirate','E9191','2021-03-30','16:27:00'),('35U8WuQC8Qi',199,'Emirate','E9191','2021-03-30','16:27:00'),('362uZEr75fr',211,'Emirate','E0000','2021-05-27','17:17:00'),('36cpKGB9hJQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('36hJieSsKkY',211,'Emirate','E0000','2021-05-27','17:17:00'),('36kKtHpL4FE',211,'Emirate','E0000','2021-05-27','17:17:00'),('36pNmnfxbBQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('36SuChKHPPK',211,'Emirate','E0000','2021-05-27','17:17:00'),('36xDJUeMdvn',211,'Emirate','E0000','2021-05-27','17:17:00'),('37C4rJoScBF',199,'Emirate','E9191','2021-03-30','16:27:00'),('37cA535MHfU',211,'Emirate','E0000','2021-05-27','17:17:00'),('37DPjgoLbCL',211,'Emirate','E0000','2021-05-27','17:17:00'),('37fZxkjwwoQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('37JNrkyzuk3',211,'Emirate','E0000','2021-05-27','17:17:00'),('37nuhNjy7Q9',199,'Emirate','E9191','2021-03-30','16:27:00'),('37nx3UqjGU6',211,'Emirate','E0000','2021-05-27','17:17:00'),('37QozQ4arom',211,'Emirate','E0000','2021-05-27','17:17:00'),('37Zqpi7TXHq',211,'Emirate','E0000','2021-05-27','17:17:00'),('384EQLdgKiq',199,'Emirate','E9191','2021-03-30','16:27:00'),('385yeWQPBao',211,'Emirate','E0000','2021-05-27','17:17:00'),('387PasruBCc',211,'Emirate','E0000','2021-05-27','17:17:00'),('38bKjBFn7ap',211,'Emirate','E0000','2021-05-27','17:17:00'),('38H79axayqM',211,'Emirate','E0000','2021-05-27','17:17:00'),('38H8ToudajK',199,'Emirate','E9191','2021-03-30','16:27:00'),('38kv87acxr9',199,'Emirate','E9191','2021-03-30','16:27:00'),('38LB4XmqsEr',199,'Emirate','E9191','2021-03-30','16:27:00'),('38NpQheyfK7',211,'Emirate','E0000','2021-05-27','17:17:00'),('38npQsVru76',211,'Emirate','E0000','2021-05-27','17:17:00'),('38pvN9yYJ8e',199,'Emirate','E9191','2021-03-30','16:27:00'),('38yGEyAVQT9',199,'Emirate','E9191','2021-03-30','16:27:00'),('38yP4GXjyHW',211,'Emirate','E0000','2021-05-27','17:17:00'),('38ytLiGZdjC',211,'Emirate','E0000','2021-05-27','17:17:00'),('395XmSgATJG',211,'Emirate','E0000','2021-05-27','17:17:00'),('39bCjss8mqC',211,'Emirate','E0000','2021-05-27','17:17:00'),('39bwmKRnXKp',199,'Emirate','E9191','2021-03-30','16:27:00'),('39CCL67tsbF',199,'Emirate','E9191','2021-03-30','16:27:00'),('39Gi3yYdYJR',199,'Emirate','E9191','2021-03-30','16:27:00'),('39GioarEAve',211,'Emirate','E0000','2021-05-27','17:17:00'),('39hECm85FGP',199,'Emirate','E9191','2021-03-30','16:27:00'),('39kHnvf7gzP',211,'Emirate','E0000','2021-05-27','17:17:00'),('39NXZVdcDXu',199,'Emirate','E9191','2021-03-30','16:27:00'),('39oEKMrD9Q8',199,'Emirate','E9191','2021-03-30','16:27:00'),('39rTT2L7guv',199,'Emirate','E9191','2021-03-30','16:27:00'),('39SKgt5JpbZ',199,'Emirate','E9191','2021-03-30','16:27:00'),('39Wfewr3dhs',199,'Emirate','E9191','2021-03-30','16:27:00'),('39wSHAQoJ85',211,'Emirate','E0000','2021-05-27','17:17:00'),('39YwLRFZYkZ',199,'Emirate','E9191','2021-03-30','16:27:00'),('3A3vXksrC4z',211,'Emirate','E0000','2021-05-27','17:17:00'),('3A4mZQcvdiG',199,'Emirate','E9191','2021-03-30','16:27:00'),('3A7amwjSfSD',211,'Emirate','E0000','2021-05-27','17:17:00'),('3A8j4rYhLug',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Adv3KQT2cP',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Aek7GcLpSH',211,'Emirate','E0000','2021-05-27','17:17:00'),('3APQsWZszzC',199,'Emirate','E9191','2021-03-30','16:27:00'),('3AWVacryzrp',211,'Emirate','E0000','2021-05-27','17:17:00'),('3AZvWrjGV9u',199,'Emirate','E9191','2021-03-30','16:27:00'),('3AzY4Cbuvo6',211,'Emirate','E0000','2021-05-27','17:17:00'),('3BaSBnua26f',199,'Emirate','E9191','2021-03-30','16:27:00'),('3BeRePgTMxL',211,'Emirate','E0000','2021-05-27','17:17:00'),('3BHXU3hdRhC',199,'Emirate','E9191','2021-03-30','16:27:00'),('3BKVNKVYx2X',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Bnhodi4SiA',199,'Emirate','E9191','2021-03-30','16:27:00'),('3BooCuB6BTm',211,'Emirate','E0000','2021-05-27','17:17:00'),('3BPgRmeHy2y',211,'Emirate','E0000','2021-05-27','17:17:00'),('3BQ6DjX6jqp',199,'Emirate','E9191','2021-03-30','16:27:00'),('3By6mpCxsbY',199,'Emirate','E9191','2021-03-30','16:27:00'),('3ByUFmkyHJS',211,'Emirate','E0000','2021-05-27','17:17:00'),('3C52bGQttYG',211,'Emirate','E0000','2021-05-27','17:17:00'),('3CACzqiYKNx',211,'Emirate','E0000','2021-05-27','17:17:00'),('3CcaYTydkek',199,'Emirate','E9191','2021-03-30','16:27:00'),('3CegYJNWmyR',211,'Emirate','E0000','2021-05-27','17:17:00'),('3CF9v55cN8t',211,'Emirate','E0000','2021-05-27','17:17:00'),('3cFwAehzdvD',199,'Emirate','E9191','2021-03-30','16:27:00'),('3CjUosG6RKv',199,'Emirate','E9191','2021-03-30','16:27:00'),('3cnYLrToUG9',199,'Emirate','E9191','2021-03-30','16:27:00'),('3CSL3Rtnqpc',199,'Emirate','E9191','2021-03-30','16:27:00'),('3CSqJMsQgsV',199,'Emirate','E9191','2021-03-30','16:27:00'),('3CtsFxrfbao',211,'Emirate','E0000','2021-05-27','17:17:00'),('3CVVLdMPy9p',211,'Emirate','E0000','2021-05-27','17:17:00'),('3CybCgNQBAK',211,'Emirate','E0000','2021-05-27','17:17:00'),('3D7vtY6yqSA',211,'Emirate','E0000','2021-05-27','17:17:00'),('3D9TAMTrP5N',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DAgsMVi5Vw',211,'Emirate','E0000','2021-05-27','17:17:00'),('3dCxRASdfdB',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DDeUDFFkvk',211,'Emirate','E0000','2021-05-27','17:17:00'),('3DG7nFmpbfL',211,'Emirate','E0000','2021-05-27','17:17:00'),('3DjHXnZb9vC',211,'Emirate','E0000','2021-05-27','17:17:00'),('3DpxoDWUTsz',211,'Emirate','E0000','2021-05-27','17:17:00'),('3DqiFBon2du',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Dt87SpsMVB',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DuxzdeESTp',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DXgxdx2sCH',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DypmBVcuNM',199,'Emirate','E9191','2021-03-30','16:27:00'),('3DyvuWM4AdT',199,'Emirate','E9191','2021-03-30','16:27:00'),('3EAF79mpJhG',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EaqHYUZxji',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EEmrMCAu4y',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EJWpttcekH',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EMe2hRK4wp',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EMm2si4PUf',199,'Emirate','E9191','2021-03-30','16:27:00'),('3En4hfoJvbY',199,'Emirate','E9191','2021-03-30','16:27:00'),('3EoNcebVHSu',211,'Emirate','E0000','2021-05-27','17:17:00'),('3EWvGXHRfWK',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Exp4voc9WJ',211,'Emirate','E0000','2021-05-27','17:17:00'),('3ExUsEHGMR8',199,'Emirate','E9191','2021-03-30','16:27:00'),('3EzRyUqYWpS',211,'Emirate','E0000','2021-05-27','17:17:00'),('3F3qu2PsRAy',211,'Emirate','E0000','2021-05-27','17:17:00'),('3F5GNb5iX5t',199,'Emirate','E9191','2021-03-30','16:27:00'),('3F5ihpGKjzj',199,'Emirate','E9191','2021-03-30','16:27:00'),('3FCrjxDtz8z',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FENkAkxjqb',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FjuAVsud4S',199,'Emirate','E9191','2021-03-30','16:27:00'),('3FMC5NJEJTQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('3FqfHjfXt4S',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FSHZSnsvUZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FsqQohjwdb',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FwdbLb2G4n',211,'Emirate','E0000','2021-05-27','17:17:00'),('3FWfmMjU8Zy',199,'Emirate','E9191','2021-03-30','16:27:00'),('3FXYCnSxgkb',199,'Emirate','E9191','2021-03-30','16:27:00'),('3G2iZURGQYi',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GaFJhRTaUT',211,'Emirate','E0000','2021-05-27','17:17:00'),('3GbzQHAweZ6',211,'Emirate','E0000','2021-05-27','17:17:00'),('3GJJTeU94x6',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GofFzHPYqS',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Gq3kL73LjC',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GrrXFZqBbS',211,'Emirate','E0000','2021-05-27','17:17:00'),('3GVgX24gCdR',211,'Emirate','E0000','2021-05-27','17:17:00'),('3GxENaqx6dU',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GzNGZtoN3g',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GzoZk9vRFR',199,'Emirate','E9191','2021-03-30','16:27:00'),('3GzVL4bPaJg',211,'Emirate','E0000','2021-05-27','17:17:00'),('3h5tFusKY7M',199,'Emirate','E9191','2021-03-30','16:27:00'),('3H7x6Hk4W6d',211,'Emirate','E0000','2021-05-27','17:17:00'),('3HewbRDuQhm',211,'Emirate','E0000','2021-05-27','17:17:00'),('3HJWyDHDqrW',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Hkp6mSz62S',211,'Emirate','E0000','2021-05-27','17:17:00'),('3HMQLy8xysE',199,'Emirate','E9191','2021-03-30','16:27:00'),('3HRiJZXjr3W',199,'Emirate','E9191','2021-03-30','16:27:00'),('3HUMAjMT3ra',211,'Emirate','E0000','2021-05-27','17:17:00'),('3HxqtNFKrmu',199,'Emirate','E9191','2021-03-30','16:27:00'),('3HYe8ckywwj',199,'Emirate','E9191','2021-03-30','16:27:00'),('3HZfdq3KFKr',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JB67UanVpu',199,'Emirate','E9191','2021-03-30','16:27:00'),('3JcXBXbr63B',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JeU3tKzBGU',199,'Emirate','E9191','2021-03-30','16:27:00'),('3JFnJHu9a88',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Jh7AJ8iEPV',199,'Emirate','E9191','2021-03-30','16:27:00'),('3JhApWwareg',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JNeE6YFKzG',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JpmGY3n7sa',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JpsBwPvShj',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JQ3Niz6tfx',211,'Emirate','E0000','2021-05-27','17:17:00'),('3JqLhKc7LKr',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Jy55Pq7qZu',199,'Emirate','E9191','2021-03-30','16:27:00'),('3K6wu2pPCJf',211,'Emirate','E0000','2021-05-27','17:17:00'),('3K8jcwZ9MxT',211,'Emirate','E0000','2021-05-27','17:17:00'),('3KBoUpT6EQz',199,'Emirate','E9191','2021-03-30','16:27:00'),('3KMkKbDzmwD',211,'Emirate','E0000','2021-05-27','17:17:00'),('3KozVtap9J7',199,'Emirate','E9191','2021-03-30','16:27:00'),('3KPKiL6aiMN',211,'Emirate','E0000','2021-05-27','17:17:00'),('3KsQRotakEq',211,'Emirate','E0000','2021-05-27','17:17:00'),('3KSyhZBdHMx',199,'Emirate','E9191','2021-03-30','16:27:00'),('3KtoTvwfeNP',211,'Emirate','E0000','2021-05-27','17:17:00'),('3L3qvoXDdW3',199,'Emirate','E9191','2021-03-30','16:27:00'),('3L53cyJxV6C',199,'Emirate','E9191','2021-03-30','16:27:00'),('3L8t8PL2aq7',199,'Emirate','E9191','2021-03-30','16:27:00'),('3LaXQTd8Vjv',211,'Emirate','E0000','2021-05-27','17:17:00'),('3LbzunRtaY2',211,'Emirate','E0000','2021-05-27','17:17:00'),('3LETBg2LrrR',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Lf7boE3bfe',199,'Emirate','E9191','2021-03-30','16:27:00'),('3LHgBe6LqYA',211,'Emirate','E0000','2021-05-27','17:17:00'),('3LKPzDSYEvh',199,'Emirate','E9191','2021-03-30','16:27:00'),('3LWtbFC6MyV',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Lx9n6dgSK9',199,'Emirate','E9191','2021-03-30','16:27:00'),('3MGE8qMjGte',211,'Emirate','E0000','2021-05-27','17:17:00'),('3MJH2s6Pnta',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Mkvqox9L9w',211,'Emirate','E0000','2021-05-27','17:17:00'),('3MnPpGgNzvH',199,'Emirate','E9191','2021-03-30','16:27:00'),('3MU7wC5Aiof',199,'Emirate','E9191','2021-03-30','16:27:00'),('3MUGAxxn4JC',211,'Emirate','E0000','2021-05-27','17:17:00'),('3MWc6viBPiV',199,'Emirate','E9191','2021-03-30','16:27:00'),('3MxFThEoLjm',199,'Emirate','E9191','2021-03-30','16:27:00'),('3N3HzQEAhtz',211,'Emirate','E0000','2021-05-27','17:17:00'),('3N4Km5NnmNs',199,'Emirate','E9191','2021-03-30','16:27:00'),('3N5BsVQ3L3t',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NbUuCLpfqv',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NDTePVnhuQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('3NF7bds256q',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NFUzwmktmP',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NgVqRnD5Qw',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NHJCozkNhX',199,'Emirate','E9191','2021-03-30','16:27:00'),('3NKCEz7Mr6V',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NnWCPs6B2H',199,'Emirate','E9191','2021-03-30','16:27:00'),('3NQ8iH3qjTA',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NQLdE7GyWA',211,'Emirate','E0000','2021-05-27','17:17:00'),('3NR5tmcAtzE',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Nw46L7J9Db',199,'Emirate','E9191','2021-03-30','16:27:00'),('3NWuJUVgf2v',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Nx3bNEKRoN',199,'Emirate','E9191','2021-03-30','16:27:00'),('3NZS9A6QGEL',199,'Emirate','E9191','2021-03-30','16:27:00'),('3PnCE5Qbwvm',211,'Emirate','E0000','2021-05-27','17:17:00'),('3PTuthAbQaJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('3PzDYTuU47g',199,'Emirate','E9191','2021-03-30','16:27:00'),('3Q3AvTtNdyB',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Q86Nr9LfTD',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QdroM8tdJ7',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QeDcFqGUAR',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Qf9ZR4n8ez',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QfeHJZLoiG',211,'Emirate','E0000','2021-05-27','17:17:00'),('3QiePbDLG68',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QiviukJMQd',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QJbUNT2B2d',211,'Emirate','E0000','2021-05-27','17:17:00'),('3QjhHbwvcZf',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QMMQRQjEZp',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QTR3ppHcVz',211,'Emirate','E0000','2021-05-27','17:17:00'),('3QUUY68c2N6',199,'Emirate','E9191','2021-03-30','16:27:00'),('3QVtWSGhrFR',211,'Emirate','E0000','2021-05-27','17:17:00'),('3QwdFjNK4Ac',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Qx3E3V9UMX',211,'Emirate','E0000','2021-05-27','17:17:00'),('3QyLJV6bBiR',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RE6tACuZes',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RekoiYMQab',211,'Emirate','E0000','2021-05-27','17:17:00'),('3RLE8bQCQHR',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RmEbTgaipY',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RN4yWXXGvu',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RP8JfqyUZF',211,'Emirate','E0000','2021-05-27','17:17:00'),('3RQPEahRnaX',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Rsk2iTepgM',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RSZJMTPmGh',211,'Emirate','E0000','2021-05-27','17:17:00'),('3Ruv5hcn79R',199,'Emirate','E9191','2021-03-30','16:27:00'),('3RZHVF8MNax',199,'Emirate','E9191','2021-03-30','16:27:00'),('3uvS9KbgkjZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('3VAQMTvWPwc',211,'Emirate','E0000','2021-05-27','17:17:00'),('3WXzexAABoC',211,'Emirate','E0000','2021-05-27','17:17:00'),('44cTNDTATGt',199,'Emirate','E9191','2021-03-30','16:27:00'),('48Lw47GtCo5',199,'Emirate','E9191','2021-03-30','16:27:00'),('48ziekJdEYW',211,'Emirate','E0000','2021-05-27','17:17:00'),('4d8tMrUr2aB',211,'Emirate','E0000','2021-05-27','17:17:00'),('4fFJFViTJKw',199,'Emirate','E9191','2021-03-30','16:27:00'),('4fHqvDdKKj5',199,'Emirate','E9191','2021-03-30','16:27:00'),('4Fv9pWY2ZXJ',211,'Emirate','E0000','2021-05-27','17:17:00'),('4LbsG345q2H',211,'Emirate','E0000','2021-05-27','17:17:00'),('4MTDSTRZ8qc',199,'Emirate','E9191','2021-03-30','16:27:00'),('4NvD4yBSyZP',199,'Emirate','E9191','2021-03-30','16:27:00'),('4oX3if3ULMv',211,'Emirate','E0000','2021-05-27','17:17:00'),('4T5eVunXYEi',199,'Emirate','E9191','2021-03-30','16:27:00'),('4TXtZkWLa8d',211,'Emirate','E0000','2021-05-27','17:17:00'),('53B2JJSMSsu',199,'Emirate','E9191','2021-03-30','16:27:00'),('55qjSx9iUW8',211,'Emirate','E0000','2021-05-27','17:17:00'),('55xw6wqSVUZ',199,'Emirate','E9191','2021-03-30','16:27:00'),('59UtjHkQMLq',211,'Emirate','E0000','2021-05-27','17:17:00'),('5Cz3KKn9FKN',211,'Emirate','E0000','2021-05-27','17:17:00'),('5EUKtSR5iSH',211,'Emirate','E0000','2021-05-27','17:17:00'),('5FRyGyEGDNU',211,'Emirate','E0000','2021-05-27','17:17:00'),('5HtGXEXGMxL',211,'Emirate','E0000','2021-05-27','17:17:00'),('5LRtio4uk5W',199,'Emirate','E9191','2021-03-30','16:27:00'),('62RkFaTU3rD',199,'Emirate','E9191','2021-03-30','16:27:00'),('6629QUmDiks',199,'Emirate','E9191','2021-03-30','16:27:00'),('6m5SSrwwKsD',211,'Emirate','E0000','2021-05-27','17:17:00'),('6TgUPVzxM8d',211,'Emirate','E0000','2021-05-27','17:17:00'),('6TkbLvUnZKa',211,'Emirate','E0000','2021-05-27','17:17:00'),('6UHej4nQhiN',199,'Emirate','E9191','2021-03-30','16:27:00'),('6VoBYaohEvf',211,'Emirate','E0000','2021-05-27','17:17:00'),('78iQThgVjaG',199,'Emirate','E9191','2021-03-30','16:27:00'),('7AJ5EU8onaR',199,'Emirate','E9191','2021-03-30','16:27:00'),('7aneUdEkV9V',199,'Emirate','E9191','2021-03-30','16:27:00'),('7d35L6Ru5DY',211,'Emirate','E0000','2021-05-27','17:17:00'),('7EmhECqS9zE',199,'Emirate','E9191','2021-03-30','16:27:00'),('7hThTxoGcB2',211,'Emirate','E0000','2021-05-27','17:17:00'),('7Q4mPgxzWaF',199,'Emirate','E9191','2021-03-30','16:27:00'),('7q6tjjA5BqW',199,'Emirate','E9191','2021-03-30','16:27:00'),('7QbB3iWvrBg',211,'Emirate','E0000','2021-05-27','17:17:00'),('7qNXZuW4RjN',211,'Emirate','E0000','2021-05-27','17:17:00'),('7sci3YEjMMH',211,'Emirate','E0000','2021-05-27','17:17:00'),('7THCjMUuLMQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('7VHYhRXX7E6',199,'Emirate','E9191','2021-03-30','16:27:00'),('7VxcLqoXnBv',199,'Emirate','E9191','2021-03-30','16:27:00'),('7XEYZ6zGXQT',199,'Emirate','E9191','2021-03-30','16:27:00'),('7YdA3D7JeeE',199,'Emirate','E9191','2021-03-30','16:27:00'),('7yRZ8wU6Amp',211,'Emirate','E0000','2021-05-27','17:17:00'),('8B3KoAyj4W9',211,'Emirate','E0000','2021-05-27','17:17:00'),('8FecJmMzzpB',199,'Emirate','E9191','2021-03-30','16:27:00'),('8HbGajRgkKX',199,'Emirate','E9191','2021-03-30','16:27:00'),('8NfrpkKi2Wc',199,'Emirate','E9191','2021-03-30','16:27:00'),('8on4euH785Z',211,'Emirate','E0000','2021-05-27','17:17:00'),('8vDpSmHfFvE',211,'Emirate','E0000','2021-05-27','17:17:00'),('8zrTWFAiNLu',211,'Emirate','E0000','2021-05-27','17:17:00'),('98sEpknsVtC',199,'Emirate','E9191','2021-03-30','16:27:00'),('9DktZgiUh3x',199,'Emirate','E9191','2021-03-30','16:27:00'),('9DLT3y3fbnZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('9Hs5L9vFTi4',199,'Emirate','E9191','2021-03-30','16:27:00'),('9V3DFMh7bEs',199,'Emirate','E9191','2021-03-30','16:27:00'),('A001',500,'Delta','D1233','2020-04-14','13:30:00'),('A002',500,'Delta','D1233','2020-04-14','13:30:00'),('A003',500,'Delta','D1233','2020-04-14','13:30:00'),('A5dgx4vv7Ai',211,'Emirate','E0000','2021-05-27','17:17:00'),('A8ZqrVmSFDX',199,'Emirate','E9191','2021-03-30','16:27:00'),('abfujfYz5bq',199,'Emirate','E9191','2021-03-30','16:27:00'),('aCF5xgztpGm',211,'Emirate','E0000','2021-05-27','17:17:00'),('ACKX7SKS5FX',199,'Emirate','E9191','2021-03-30','16:27:00'),('aE96yPuo2fQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('Agb58i7TB7k',199,'Emirate','E9191','2021-03-30','16:27:00'),('AJm7dCZd7vF',211,'Emirate','E0000','2021-05-27','17:17:00'),('AKj5gF6g3HE',199,'Emirate','E9191','2021-03-30','16:27:00'),('AmEVeKTy4QB',199,'Emirate','E9191','2021-03-30','16:27:00'),('AMMqs28QigT',211,'Emirate','E0000','2021-05-27','17:17:00'),('amzfDG85o3r',199,'Emirate','E9191','2021-03-30','16:27:00'),('An8RNELQSYx',199,'Emirate','E9191','2021-03-30','16:27:00'),('ANfmybBYjum',211,'Emirate','E0000','2021-05-27','17:17:00'),('AnvDhXuP9QD',199,'Emirate','E9191','2021-03-30','16:27:00'),('ao3pgKZWrxH',199,'Emirate','E9191','2021-03-30','16:27:00'),('aoKCgUw3Lrr',199,'Emirate','E9191','2021-03-30','16:27:00'),('Ap6UP2qhVYP',211,'Emirate','E0000','2021-05-27','17:17:00'),('AptiuVncsQY',211,'Emirate','E0000','2021-05-27','17:17:00'),('AQ4U7UhXEuP',199,'Emirate','E9191','2021-03-30','16:27:00'),('aqgCxyx5yPt',211,'Emirate','E0000','2021-05-27','17:17:00'),('aREP96ecSTR',199,'Emirate','E9191','2021-03-30','16:27:00'),('asAHKtwzetf',199,'Emirate','E9191','2021-03-30','16:27:00'),('asCgd9y832B',199,'Emirate','E9191','2021-03-30','16:27:00'),('ATRtHfhqtiY',199,'Emirate','E9191','2021-03-30','16:27:00'),('awYbrV9uXaH',211,'Emirate','E0000','2021-05-27','17:17:00'),('Ax7A7TtDCxe',211,'Emirate','E0000','2021-05-27','17:17:00'),('aZz4tUUyFm4',199,'Emirate','E9191','2021-03-30','16:27:00'),('AzZ4UbBsDgD',199,'Emirate','E9191','2021-03-30','16:27:00'),('B2ZG6B5fTAP',199,'Emirate','E9191','2021-03-30','16:27:00'),('B4PDeBX5iFZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('b7pU2w9z5To',211,'Emirate','E0000','2021-05-27','17:17:00'),('B8KYD7b4pxf',199,'Emirate','E9191','2021-03-30','16:27:00'),('b8ZA6eZwU52',199,'Emirate','E9191','2021-03-30','16:27:00'),('bdhTtuW4R5X',199,'Emirate','E9191','2021-03-30','16:27:00'),('BeeywXjiYKw',199,'Emirate','E9191','2021-03-30','16:27:00'),('BeKCczJyqfG',199,'Emirate','E9191','2021-03-30','16:27:00'),('BgM8uZciZj6',199,'Emirate','E9191','2021-03-30','16:27:00'),('bgNjGcBXG2U',211,'Emirate','E0000','2021-05-27','17:17:00'),('BJ3Ps3J5Cn2',199,'Emirate','E9191','2021-03-30','16:27:00'),('BJdJ3mTyRWJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('BLWtP6My2dC',211,'Emirate','E0000','2021-05-27','17:17:00'),('BNRs9YRSWJ8',199,'Emirate','E9191','2021-03-30','16:27:00'),('Bs5H73Acktr',199,'Emirate','E9191','2021-03-30','16:27:00'),('bsoBGr58gkP',199,'Emirate','E9191','2021-03-30','16:27:00'),('btMDyxVgofg',211,'Emirate','E0000','2021-05-27','17:17:00'),('BVvWbV7q5TN',199,'Emirate','E9191','2021-03-30','16:27:00'),('BxS7XBr6iwN',199,'Emirate','E9191','2021-03-30','16:27:00'),('BYfV5hKKhcJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('bYHnq4CcDkY',211,'Emirate','E0000','2021-05-27','17:17:00'),('BYoDcyLa5o9',199,'Emirate','E9191','2021-03-30','16:27:00'),('c8eRitv5rAB',211,'Emirate','E0000','2021-05-27','17:17:00'),('caDeVpHNoyS',199,'Emirate','E9191','2021-03-30','16:27:00'),('caRnf7VeaVZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('CCkXBFT6VD5',211,'Emirate','E0000','2021-05-27','17:17:00'),('CdWovmsbEGx',211,'Emirate','E0000','2021-05-27','17:17:00'),('CEFK6pWWLQX',211,'Emirate','E0000','2021-05-27','17:17:00'),('cETMs7AggH6',199,'Emirate','E9191','2021-03-30','16:27:00'),('cGg58bkhX7G',211,'Emirate','E0000','2021-05-27','17:17:00'),('CGTx2XDGFoG',199,'Emirate','E9191','2021-03-30','16:27:00'),('Chh3sLAEbu9',199,'Emirate','E9191','2021-03-30','16:27:00'),('CiBerDcYFRB',199,'Emirate','E9191','2021-03-30','16:27:00'),('CjuKkQuEapQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('CKXBV9oym2w',199,'Emirate','E9191','2021-03-30','16:27:00'),('cLhUVGhFTsd',211,'Emirate','E0000','2021-05-27','17:17:00'),('cm6Ygk7EzzX',211,'Emirate','E0000','2021-05-27','17:17:00'),('cokxn6quf9f',199,'Emirate','E9191','2021-03-30','16:27:00'),('CPPyL828PrQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('Ct3QJfAofSN',199,'Emirate','E9191','2021-03-30','16:27:00'),('cTQQMbYmivw',211,'Emirate','E0000','2021-05-27','17:17:00'),('CtXc3rodepF',199,'Emirate','E9191','2021-03-30','16:27:00'),('cVua6PnKCK8',199,'Emirate','E9191','2021-03-30','16:27:00'),('CWMMdRVfpKW',211,'Emirate','E0000','2021-05-27','17:17:00'),('cXUZ2vUnUd6',199,'Emirate','E9191','2021-03-30','16:27:00'),('CZA4fcMsDQf',199,'Emirate','E9191','2021-03-30','16:27:00'),('CZrZHW8ypJz',199,'Emirate','E9191','2021-03-30','16:27:00'),('D001',1000,'China Eastern','CE123','2020-04-19','14:23:00'),('D002',1000,'China Eastern','CE123','2020-04-19','14:23:00'),('D003',1000,'China Eastern','CE123','2020-04-19','14:23:00'),('D4DAt3xwMox',211,'Emirate','E0000','2021-05-27','17:17:00'),('D4V937ArseH',211,'Emirate','E0000','2021-05-27','17:17:00'),('d5gBQAz88TH',211,'Emirate','E0000','2021-05-27','17:17:00'),('D8mq2TD9CLX',211,'Emirate','E0000','2021-05-27','17:17:00'),('d8nB8TKAxC9',199,'Emirate','E9191','2021-03-30','16:27:00'),('dazkHCRfYbi',211,'Emirate','E0000','2021-05-27','17:17:00'),('dDKQiQxFV5q',211,'Emirate','E0000','2021-05-27','17:17:00'),('Df5Xo5PeeHV',211,'Emirate','E0000','2021-05-27','17:17:00'),('DgHCd42cvau',199,'Emirate','E9191','2021-03-30','16:27:00'),('DGHHNJxUGin',211,'Emirate','E0000','2021-05-27','17:17:00'),('djuJops8zhu',199,'Emirate','E9191','2021-03-30','16:27:00'),('dnspqPBerNZ',199,'Emirate','E9191','2021-03-30','16:27:00'),('DpGzbd6YwXV',211,'Emirate','E0000','2021-05-27','17:17:00'),('dQ4bhKGBNC4',211,'Emirate','E0000','2021-05-27','17:17:00'),('DqtxJocAg9k',211,'Emirate','E0000','2021-05-27','17:17:00'),('DVA9JPqTRYt',211,'Emirate','E0000','2021-05-27','17:17:00'),('dVSQTumxChC',211,'Emirate','E0000','2021-05-27','17:17:00'),('DXujUnbtQWh',211,'Emirate','E0000','2021-05-27','17:17:00'),('E001',300,'Emirate','E1111','2021-04-20','06:00:00'),('E002',300,'Emirate','E1111','2021-04-20','06:00:00'),('E003',300,'Emirate','E1111','2021-04-20','06:00:00'),('E101',455,'Emirate','E0122','2020-09-23','23:44:00'),('E102',455,'Emirate','E0122','2020-09-23','23:44:00'),('E103',455,'Emirate','E0122','2020-09-23','23:44:00'),('E231',312,'Emirate','E2233','2021-04-25','13:00:00'),('E232',240,'Emirate','E2233','2021-04-25','13:00:00'),('E233',240,'Emirate','E2233','2021-04-25','13:00:00'),('E234',422,'Emirate','E2233','2021-04-25','13:00:00'),('E301',512,'Emirate','E0342','2020-08-12','20:16:00'),('E302',512,'Emirate','E0342','2020-08-12','20:16:00'),('E303',512,'Emirate','E0342','2020-08-12','20:16:00'),('e36tbbF26og',211,'Emirate','E0000','2021-05-27','17:17:00'),('E3AsacL96Bg',211,'Emirate','E0000','2021-05-27','17:17:00'),('e3cZ2r7vpRa',211,'Emirate','E0000','2021-05-27','17:17:00'),('E401',300,'Emirate','E4432','2021-06-03','12:00:00'),('E402',300,'Emirate','E4432','2021-06-03','12:00:00'),('E403',300,'Emirate','E4432','2021-06-03','12:00:00'),('E4SBG59GdGQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('e6oPPTejDVg',199,'Emirate','E9191','2021-03-30','16:27:00'),('E7GgitddwxT',211,'Emirate','E0000','2021-05-27','17:17:00'),('Ef65vspzQD5',199,'Emirate','E9191','2021-03-30','16:27:00'),('EFLGGL8msPw',211,'Emirate','E0000','2021-05-27','17:17:00'),('eGj2bqJPYst',211,'Emirate','E0000','2021-05-27','17:17:00'),('eHNQeqxAmc5',211,'Emirate','E0000','2021-05-27','17:17:00'),('ejTHhet6HDp',211,'Emirate','E0000','2021-05-27','17:17:00'),('EMaNYM99TkT',211,'Emirate','E0000','2021-05-27','17:17:00'),('eMtGrarQvVq',199,'Emirate','E9191','2021-03-30','16:27:00'),('er2WHHduKML',199,'Emirate','E9191','2021-03-30','16:27:00'),('Esbw5cVjwFt',199,'Emirate','E9191','2021-03-30','16:27:00'),('eswFE4JwdKU',211,'Emirate','E0000','2021-05-27','17:17:00'),('etGg8NqX2UF',199,'Emirate','E9191','2021-03-30','16:27:00'),('eUfvDd5yosm',199,'Emirate','E9191','2021-03-30','16:27:00'),('eujuwYqFrof',211,'Emirate','E0000','2021-05-27','17:17:00'),('euWAARxdipd',199,'Emirate','E9191','2021-03-30','16:27:00'),('EvyLJvPrUk9',199,'Emirate','E9191','2021-03-30','16:27:00'),('EXaEFbyS4eL',199,'Emirate','E9191','2021-03-30','16:27:00'),('eXVZtufrkQo',199,'Emirate','E9191','2021-03-30','16:27:00'),('EyyFvDEdNNA',211,'Emirate','E0000','2021-05-27','17:17:00'),('f7vmDDosmJV',211,'Emirate','E0000','2021-05-27','17:17:00'),('f7xx4c6bkWi',199,'Emirate','E9191','2021-03-30','16:27:00'),('f849dwL7Lwn',199,'Emirate','E9191','2021-03-30','16:27:00'),('f9xoibSNuQ8',211,'Emirate','E0000','2021-05-27','17:17:00'),('faiMUUFV9RZ',211,'Emirate','E0000','2021-05-27','17:17:00'),('fBBdmLjX3UP',211,'Emirate','E0000','2021-05-27','17:17:00'),('fboQLpaZvaD',199,'Emirate','E9191','2021-03-30','16:27:00'),('fbrQ5SoxkDs',199,'Emirate','E9191','2021-03-30','16:27:00'),('fDr8pjv9Rpm',211,'Emirate','E0000','2021-05-27','17:17:00'),('Fe2xN6c9qPH',211,'Emirate','E0000','2021-05-27','17:17:00'),('FeD8vFNis46',211,'Emirate','E0000','2021-05-27','17:17:00'),('FF25DFEXCnA',199,'Emirate','E9191','2021-03-30','16:27:00'),('ffg4GQsBKuH',211,'Emirate','E0000','2021-05-27','17:17:00'),('FfmPWGsBbrT',199,'Emirate','E9191','2021-03-30','16:27:00'),('FLRC6EpXsfi',211,'Emirate','E0000','2021-05-27','17:17:00'),('FNBUZaqyqaG',211,'Emirate','E0000','2021-05-27','17:17:00'),('fnMqGVwdyFx',199,'Emirate','E9191','2021-03-30','16:27:00'),('foEy422JWxW',199,'Emirate','E9191','2021-03-30','16:27:00'),('fpjkJ8gjsBz',211,'Emirate','E0000','2021-05-27','17:17:00'),('FQY7QE27xn3',211,'Emirate','E0000','2021-05-27','17:17:00'),('FrqBkMGqw4G',211,'Emirate','E0000','2021-05-27','17:17:00'),('fTNfc9pynUd',199,'Emirate','E9191','2021-03-30','16:27:00'),('fwJLtqhdXCu',211,'Emirate','E0000','2021-05-27','17:17:00'),('Fwjwrei4MFa',199,'Emirate','E9191','2021-03-30','16:27:00'),('fwKzpmU9uje',199,'Emirate','E9191','2021-03-30','16:27:00'),('Fz3D4xttSgV',199,'Emirate','E9191','2021-03-30','16:27:00'),('g3GoZbVw8QS',211,'Emirate','E0000','2021-05-27','17:17:00'),('G4AeRT2V5Am',211,'Emirate','E0000','2021-05-27','17:17:00'),('g4pvfTPAKPV',211,'Emirate','E0000','2021-05-27','17:17:00'),('g8MU7gsvRFe',199,'Emirate','E9191','2021-03-30','16:27:00'),('gCMHMvURLDm',211,'Emirate','E0000','2021-05-27','17:17:00'),('gdNCgTV3rHV',211,'Emirate','E0000','2021-05-27','17:17:00'),('gDTEfej5yof',211,'Emirate','E0000','2021-05-27','17:17:00'),('gE88mUjmZSA',199,'Emirate','E9191','2021-03-30','16:27:00'),('gh3WJtpNd5v',199,'Emirate','E9191','2021-03-30','16:27:00'),('GHAhkj7f7Dj',199,'Emirate','E9191','2021-03-30','16:27:00'),('gHM2ow8JAPV',211,'Emirate','E0000','2021-05-27','17:17:00'),('giFcd7YJpAd',211,'Emirate','E0000','2021-05-27','17:17:00'),('gJ8P7G7gXax',211,'Emirate','E0000','2021-05-27','17:17:00'),('gjVQdcJoVSK',211,'Emirate','E0000','2021-05-27','17:17:00'),('gkHEW7Mzq7V',211,'Emirate','E0000','2021-05-27','17:17:00'),('gkZtYgfmtKW',199,'Emirate','E9191','2021-03-30','16:27:00'),('Gmdgth4NznM',211,'Emirate','E0000','2021-05-27','17:17:00'),('gn28sT9gs3D',211,'Emirate','E0000','2021-05-27','17:17:00'),('goMWeQXZDiJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('gPnenUbvSeS',211,'Emirate','E0000','2021-05-27','17:17:00'),('Gqg2bVM2Akk',199,'Emirate','E9191','2021-03-30','16:27:00'),('gSEHBmfFsv8',211,'Emirate','E0000','2021-05-27','17:17:00'),('GTh2k6UHPjN',199,'Emirate','E9191','2021-03-30','16:27:00'),('gtxZDTrUbNA',199,'Emirate','E9191','2021-03-30','16:27:00'),('GUchFBcXP3Z',199,'Emirate','E9191','2021-03-30','16:27:00'),('GwDXypJNAtu',211,'Emirate','E0000','2021-05-27','17:17:00'),('gZjVv9QFUYr',199,'Emirate','E9191','2021-03-30','16:27:00'),('H5g4nx8nwea',199,'Emirate','E9191','2021-03-30','16:27:00'),('h6kejZdyDDV',211,'Emirate','E0000','2021-05-27','17:17:00'),('h8AhXJWR7Qr',199,'Emirate','E9191','2021-03-30','16:27:00'),('hahLkmQvXUz',211,'Emirate','E0000','2021-05-27','17:17:00'),('HaHzvdaBDm8',199,'Emirate','E9191','2021-03-30','16:27:00'),('HAi3Ca9MPK8',199,'Emirate','E9191','2021-03-30','16:27:00'),('hAuashZiXua',211,'Emirate','E0000','2021-05-27','17:17:00'),('HAz8MNGnA8x',211,'Emirate','E0000','2021-05-27','17:17:00'),('HbbR2UtAYAg',199,'Emirate','E9191','2021-03-30','16:27:00'),('Hbtp2z9uqyg',211,'Emirate','E0000','2021-05-27','17:17:00'),('hCuCsfMKmuK',211,'Emirate','E0000','2021-05-27','17:17:00'),('hjfGwDvKvVk',211,'Emirate','E0000','2021-05-27','17:17:00'),('hkvkTjVakLD',211,'Emirate','E0000','2021-05-27','17:17:00'),('HMx5CRfbFjA',211,'Emirate','E0000','2021-05-27','17:17:00'),('HmzFrAiMHma',211,'Emirate','E0000','2021-05-27','17:17:00'),('HpB4eYskNUV',211,'Emirate','E0000','2021-05-27','17:17:00'),('hSFThtJZfym',211,'Emirate','E0000','2021-05-27','17:17:00'),('htvZdcng4ti',211,'Emirate','E0000','2021-05-27','17:17:00'),('hUnNV4NPovw',199,'Emirate','E9191','2021-03-30','16:27:00'),('hVmQsjYjt2J',199,'Emirate','E9191','2021-03-30','16:27:00'),('HWR8DyycyB9',199,'Emirate','E9191','2021-03-30','16:27:00'),('HwY34E3cbsa',211,'Emirate','E0000','2021-05-27','17:17:00'),('HWzXtPsdgzL',199,'Emirate','E9191','2021-03-30','16:27:00'),('hXmyisDa32V',211,'Emirate','E0000','2021-05-27','17:17:00'),('HZpcTodfyZk',211,'Emirate','E0000','2021-05-27','17:17:00'),('i23jFbHt7T2',199,'Emirate','E9191','2021-03-30','16:27:00'),('i5T7fpAwRa6',211,'Emirate','E0000','2021-05-27','17:17:00'),('icqoVwMYPDJ',211,'Emirate','E0000','2021-05-27','17:17:00'),('iCZxECgBAWv',211,'Emirate','E0000','2021-05-27','17:17:00'),('iDMZRvELHSd',211,'Emirate','E0000','2021-05-27','17:17:00'),('ighsdsy5U5k',199,'Emirate','E9191','2021-03-30','16:27:00'),('iHbG3VFbHpp',199,'Emirate','E9191','2021-03-30','16:27:00'),('iHNLBg7gjZT',199,'Emirate','E9191','2021-03-30','16:27:00'),('iJ4bKiXDTWB',199,'Emirate','E9191','2021-03-30','16:27:00'),('iJB5NHjWpZk',211,'Emirate','E0000','2021-05-27','17:17:00'),('iqWtBLnURkg',211,'Emirate','E0000','2021-05-27','17:17:00'),('iSUB5Nkmvga',199,'Emirate','E9191','2021-03-30','16:27:00'),('iuRp8EYsbtz',211,'Emirate','E0000','2021-05-27','17:17:00'),('iVEtFkoiZiF',211,'Emirate','E0000','2021-05-27','17:17:00'),('J4tBu2wB5JA',211,'Emirate','E0000','2021-05-27','17:17:00'),('J6riakZ8q8y',199,'Emirate','E9191','2021-03-30','16:27:00'),('jA9RJEvEVHU',199,'Emirate','E9191','2021-03-30','16:27:00'),('JBAuGDWBhw4',199,'Emirate','E9191','2021-03-30','16:27:00'),('JBfNqjvBbLs',211,'Emirate','E0000','2021-05-27','17:17:00'),('jLbmPtY2ha8',211,'Emirate','E0000','2021-05-27','17:17:00'),('JLJURixFvKK',199,'Emirate','E9191','2021-03-30','16:27:00'),('JLQN8adshSR',199,'Emirate','E9191','2021-03-30','16:27:00'),('JPLAv4tKabQ',199,'Emirate','E9191','2021-03-30','16:27:00'),('JQ22evN4rcv',211,'Emirate','E0000','2021-05-27','17:17:00'),('jQDPvreisCg',199,'Emirate','E9191','2021-03-30','16:27:00'),('JRAr468SwJm',211,'Emirate','E0000','2021-05-27','17:17:00'),('JrHVK9dpers',199,'Emirate','E9191','2021-03-30','16:27:00'),('JTRJDtoMkPC',199,'Emirate','E9191','2021-03-30','16:27:00'),('JttKQJWYR2r',211,'Emirate','E0000','2021-05-27','17:17:00'),('JtYLdPrGzGr',211,'Emirate','E0000','2021-05-27','17:17:00'),('jUYrYNoQA2j',211,'Emirate','E0000','2021-05-27','17:17:00'),('JXDhko35XfT',199,'Emirate','E9191','2021-03-30','16:27:00'),('JXmRhD4wxco',211,'Emirate','E0000','2021-05-27','17:17:00'),('jXVvwrmEbUk',211,'Emirate','E0000','2021-05-27','17:17:00'),('jyERAgBBdSk',211,'Emirate','E0000','2021-05-27','17:17:00'),('k8BQTKmuBL7',199,'Emirate','E9191','2021-03-30','16:27:00'),('k8dFmtnYgdq',199,'Emirate','E9191','2021-03-30','16:27:00'),('K8Uk3YBvmg5',211,'Emirate','E0000','2021-05-27','17:17:00'),('K937QUvDfny',211,'Emirate','E0000','2021-05-27','17:17:00'),('k93BLBArCkr',199,'Emirate','E9191','2021-03-30','16:27:00'),('kCkrcSsN4Jz',211,'Emirate','E0000','2021-05-27','17:17:00'),('KCubnZUcTDh',211,'Emirate','E0000','2021-05-27','17:17:00'),('KD2NQ8u4GMY',199,'Emirate','E9191','2021-03-30','16:27:00'),('KG3xt83iH65',211,'Emirate','E0000','2021-05-27','17:17:00'),('KKDpnvwmR8S',211,'Emirate','E0000','2021-05-27','17:17:00'),('kMBYJttd4us',211,'Emirate','E0000','2021-05-27','17:17:00'),('kMcJ8hLJDYq',211,'Emirate','E0000','2021-05-27','17:17:00'),('koeYEz2FfVN',199,'Emirate','E9191','2021-03-30','16:27:00'),('KqJWoaJXEGT',211,'Emirate','E0000','2021-05-27','17:17:00'),('kRjsqMtYGk6',199,'Emirate','E9191','2021-03-30','16:27:00'),('kTG8fgHdpmo',199,'Emirate','E9191','2021-03-30','16:27:00'),('ktJLDHWRrNb',211,'Emirate','E0000','2021-05-27','17:17:00'),('Ktm2WkmDjMm',199,'Emirate','E9191','2021-03-30','16:27:00'),('KWAUaEL8iEg',211,'Emirate','E0000','2021-05-27','17:17:00'),('KWPMwJG7mmE',211,'Emirate','E0000','2021-05-27','17:17:00'),('KX3BpnZdfTU',211,'Emirate','E0000','2021-05-27','17:17:00'),('kxwE3t7k7cw',199,'Emirate','E9191','2021-03-30','16:27:00'),('kytbATWZxD8',199,'Emirate','E9191','2021-03-30','16:27:00'),('kzjxf5yBSAT',199,'Emirate','E9191','2021-03-30','16:27:00'),('KzoXfzaoYyi',199,'Emirate','E9191','2021-03-30','16:27:00'),('KzRNxfhPNrQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('KZvxBWfwEH4',199,'Emirate','E9191','2021-03-30','16:27:00'),('L8bV4spdADR',199,'Emirate','E9191','2021-03-30','16:27:00'),('LFwZWmuCG6L',211,'Emirate','E0000','2021-05-27','17:17:00'),('LFyoDKgmwHm',211,'Emirate','E0000','2021-05-27','17:17:00'),('LgxVhua5beQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('LifHSjDFGvm',199,'Emirate','E9191','2021-03-30','16:27:00'),('LKDEGoLwtwC',199,'Emirate','E9191','2021-03-30','16:27:00'),('LMVeutqz6nH',211,'Emirate','E0000','2021-05-27','17:17:00'),('LTmrctZNctz',199,'Emirate','E9191','2021-03-30','16:27:00'),('LWtBXMPoave',211,'Emirate','E0000','2021-05-27','17:17:00'),('Ly7ZjxmZdMs',211,'Emirate','E0000','2021-05-27','17:17:00'),('LZNSb72otYW',211,'Emirate','E0000','2021-05-27','17:17:00'),('m3fmgUKdW7H',199,'Emirate','E9191','2021-03-30','16:27:00'),('mDmyaLUFYM9',199,'Emirate','E9191','2021-03-30','16:27:00'),('Mdx3cshdTsv',211,'Emirate','E0000','2021-05-27','17:17:00'),('mgCbpFnfyNK',211,'Emirate','E0000','2021-05-27','17:17:00'),('MGvgVVf66WJ',199,'Emirate','E9191','2021-03-30','16:27:00'),('Mj8VK6M8JEk',199,'Emirate','E9191','2021-03-30','16:27:00'),('mkaLSbTFEFV',211,'Emirate','E0000','2021-05-27','17:17:00'),('mnVT5Y5wMQ9',211,'Emirate','E0000','2021-05-27','17:17:00'),('mS23gukfJs5',199,'Emirate','E9191','2021-03-30','16:27:00'),('mspwVLcfBE4',199,'Emirate','E9191','2021-03-30','16:27:00'),('MTKbYYKgyaH',199,'Emirate','E9191','2021-03-30','16:27:00'),('muLxNBoKx7h',199,'Emirate','E9191','2021-03-30','16:27:00'),('mUYStdJcN35',199,'Emirate','E9191','2021-03-30','16:27:00'),('mv44s94L43S',211,'Emirate','E0000','2021-05-27','17:17:00'),('MVdxcMkJerP',211,'Emirate','E0000','2021-05-27','17:17:00'),('mx4wqno9fmu',211,'Emirate','E0000','2021-05-27','17:17:00'),('mxuNMEKk2zx',211,'Emirate','E0000','2021-05-27','17:17:00'),('MxvrP6GE3VL',199,'Emirate','E9191','2021-03-30','16:27:00'),('mxZ9TPqe8FK',199,'Emirate','E9191','2021-03-30','16:27:00'),('mZcxArTFJBn',199,'Emirate','E9191','2021-03-30','16:27:00'),('mZK29dqTDQj',199,'Emirate','E9191','2021-03-30','16:27:00'),('MZSS3zTY2uc',199,'Emirate','E9191','2021-03-30','16:27:00'),('n7frkvT6bkE',211,'Emirate','E0000','2021-05-27','17:17:00'),('N8X6KcaYrDS',199,'Emirate','E9191','2021-03-30','16:27:00'),('na9GCjhTK2w',199,'Emirate','E9191','2021-03-30','16:27:00'),('nAjeiTaWCtq',211,'Emirate','E0000','2021-05-27','17:17:00'),('nbHWWm5YqUe',211,'Emirate','E0000','2021-05-27','17:17:00'),('NdgZmNNDetc',211,'Emirate','E0000','2021-05-27','17:17:00'),('nhsUTfBJKUj',199,'Emirate','E9191','2021-03-30','16:27:00'),('NioQ7fWzHvm',199,'Emirate','E9191','2021-03-30','16:27:00'),('NJwxkmUgyQD',211,'Emirate','E0000','2021-05-27','17:17:00'),('NjZEtYLQJeH',211,'Emirate','E0000','2021-05-27','17:17:00'),('NKgjxTmxgdz',211,'Emirate','E0000','2021-05-27','17:17:00'),('NoMmMSiUhUT',199,'Emirate','E9191','2021-03-30','16:27:00'),('NPWbstF7wTe',211,'Emirate','E0000','2021-05-27','17:17:00'),('Nqqg9VsLPwR',211,'Emirate','E0000','2021-05-27','17:17:00'),('Nt9xgqygBye',199,'Emirate','E9191','2021-03-30','16:27:00'),('NThxVMPPaCs',199,'Emirate','E9191','2021-03-30','16:27:00'),('NUsRNWiEyRL',199,'Emirate','E9191','2021-03-30','16:27:00'),('NWaHFPhRFhe',199,'Emirate','E9191','2021-03-30','16:27:00'),('nWCCrv2VTxs',199,'Emirate','E9191','2021-03-30','16:27:00'),('Nxwib3zyfKW',199,'Emirate','E9191','2021-03-30','16:27:00'),('nyYHNXRW8Cg',199,'Emirate','E9191','2021-03-30','16:27:00'),('nZ8s7XXsE88',199,'Emirate','E9191','2021-03-30','16:27:00'),('nZY9RgK6888',199,'Emirate','E9191','2021-03-30','16:27:00'),('o6AYH8bCAcX',199,'Emirate','E9191','2021-03-30','16:27:00'),('oDXU2HvDGYn',199,'Emirate','E9191','2021-03-30','16:27:00'),('orJLLmbWvxw',211,'Emirate','E0000','2021-05-27','17:17:00'),('oSZpzirnpvS',199,'Emirate','E9191','2021-03-30','16:27:00'),('oVVzSnu9rAQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('oZQXPcHrJ3f',199,'Emirate','E9191','2021-03-30','16:27:00'),('ozRKdXW9Mw7',199,'Emirate','E9191','2021-03-30','16:27:00'),('p3USMDAFFB9',211,'Emirate','E0000','2021-05-27','17:17:00'),('p4CWqzHM3ZR',211,'Emirate','E0000','2021-05-27','17:17:00'),('pAB9keguA4D',199,'Emirate','E9191','2021-03-30','16:27:00'),('pCCe9dzaJp5',199,'Emirate','E9191','2021-03-30','16:27:00'),('peVSqYRmVkM',199,'Emirate','E9191','2021-03-30','16:27:00'),('PEzPsLLyNng',211,'Emirate','E0000','2021-05-27','17:17:00'),('PFBHg8ycbeF',211,'Emirate','E0000','2021-05-27','17:17:00'),('pfyAxUh2ZYU',199,'Emirate','E9191','2021-03-30','16:27:00'),('pGFJtMGMb9N',211,'Emirate','E0000','2021-05-27','17:17:00'),('Pgq4w79MiNL',211,'Emirate','E0000','2021-05-27','17:17:00'),('Phfu9USpfCA',199,'Emirate','E9191','2021-03-30','16:27:00'),('PhzDXmtGhKu',199,'Emirate','E9191','2021-03-30','16:27:00'),('pjAxM5Yfe4P',199,'Emirate','E9191','2021-03-30','16:27:00'),('pJZsjgwYXQk',199,'Emirate','E9191','2021-03-30','16:27:00'),('pkoty5CL36K',199,'Emirate','E9191','2021-03-30','16:27:00'),('pPrUyEr7HJN',211,'Emirate','E0000','2021-05-27','17:17:00'),('pQes88kk8eX',199,'Emirate','E9191','2021-03-30','16:27:00'),('pSo96sV6soL',199,'Emirate','E9191','2021-03-30','16:27:00'),('PsqinWnNXPV',199,'Emirate','E9191','2021-03-30','16:27:00'),('PUFyTy8ZWF8',211,'Emirate','E0000','2021-05-27','17:17:00'),('PUsyfUMpV4j',199,'Emirate','E9191','2021-03-30','16:27:00'),('pV686Jj9TTH',211,'Emirate','E0000','2021-05-27','17:17:00'),('pvBriaDZph2',199,'Emirate','E9191','2021-03-30','16:27:00'),('PwGgaYHE6cg',211,'Emirate','E0000','2021-05-27','17:17:00'),('pxYr2cjnEAC',199,'Emirate','E9191','2021-03-30','16:27:00'),('pyEdnKounah',199,'Emirate','E9191','2021-03-30','16:27:00'),('pzzrzNim4Ka',211,'Emirate','E0000','2021-05-27','17:17:00'),('Q78RmQQ2pZB',199,'Emirate','E9191','2021-03-30','16:27:00'),('q7GhcPsSzmb',211,'Emirate','E0000','2021-05-27','17:17:00'),('q9DsJmCzDhf',199,'Emirate','E9191','2021-03-30','16:27:00'),('qaw55dKL9aj',211,'Emirate','E0000','2021-05-27','17:17:00'),('QdNVkrv28iK',211,'Emirate','E0000','2021-05-27','17:17:00'),('QEQeyYVHd8p',211,'Emirate','E0000','2021-05-27','17:17:00'),('qiuHkRpVBu5',211,'Emirate','E0000','2021-05-27','17:17:00'),('qjL7mQMdddT',199,'Emirate','E9191','2021-03-30','16:27:00'),('qoTX9JifzG8',199,'Emirate','E9191','2021-03-30','16:27:00'),('qphFhJLqraM',199,'Emirate','E9191','2021-03-30','16:27:00'),('qqRkN2xyJve',199,'Emirate','E9191','2021-03-30','16:27:00'),('qrexo2XV67H',199,'Emirate','E9191','2021-03-30','16:27:00'),('qt5E3gyy4rV',211,'Emirate','E0000','2021-05-27','17:17:00'),('QTRp8poMjmq',199,'Emirate','E9191','2021-03-30','16:27:00'),('QtXa2YwY7Cj',199,'Emirate','E9191','2021-03-30','16:27:00'),('quxn7HmRzCN',211,'Emirate','E0000','2021-05-27','17:17:00'),('qwCARUo7pg2',211,'Emirate','E0000','2021-05-27','17:17:00'),('QxeZ7cWVMRh',211,'Emirate','E0000','2021-05-27','17:17:00'),('QxPM4qCgFao',211,'Emirate','E0000','2021-05-27','17:17:00'),('Qy3wAEi3WHa',199,'Emirate','E9191','2021-03-30','16:27:00'),('QY9QVpJGDcX',211,'Emirate','E0000','2021-05-27','17:17:00'),('qZkGgQorkTU',199,'Emirate','E9191','2021-03-30','16:27:00'),('R9Z9eNykq2G',211,'Emirate','E0000','2021-05-27','17:17:00'),('RbgXYjAGs3v',199,'Emirate','E9191','2021-03-30','16:27:00'),('rBtfrxdSRWN',211,'Emirate','E0000','2021-05-27','17:17:00'),('rfdasFLjVnR',211,'Emirate','E0000','2021-05-27','17:17:00'),('RKfoirFdM2e',211,'Emirate','E0000','2021-05-27','17:17:00'),('Rkv2NjVbXFc',211,'Emirate','E0000','2021-05-27','17:17:00'),('rpy8WQFur2C',211,'Emirate','E0000','2021-05-27','17:17:00'),('rqYYGq7MQob',199,'Emirate','E9191','2021-03-30','16:27:00'),('RrRnybGJpmK',211,'Emirate','E0000','2021-05-27','17:17:00'),('rvN6YkVjGZu',211,'Emirate','E0000','2021-05-27','17:17:00'),('rx8EWeA69zC',211,'Emirate','E0000','2021-05-27','17:17:00'),('s2qFMszYxsR',211,'Emirate','E0000','2021-05-27','17:17:00'),('S4k9VTNoiun',199,'Emirate','E9191','2021-03-30','16:27:00'),('SBhxUMi4v69',211,'Emirate','E0000','2021-05-27','17:17:00'),('sCa5ktZ8EhJ',211,'Emirate','E0000','2021-05-27','17:17:00'),('seWqEN876rB',199,'Emirate','E9191','2021-03-30','16:27:00'),('seXsW2T5UZG',211,'Emirate','E0000','2021-05-27','17:17:00'),('sfbk4D8Qpzd',199,'Emirate','E9191','2021-03-30','16:27:00'),('sfSZnnXwbja',199,'Emirate','E9191','2021-03-30','16:27:00'),('SJ8B3g3nJ8h',211,'Emirate','E0000','2021-05-27','17:17:00'),('sJCBKDiEDH6',199,'Emirate','E9191','2021-03-30','16:27:00'),('SjQf8zFdy5U',199,'Emirate','E9191','2021-03-30','16:27:00'),('skMxHveqGgD',199,'Emirate','E9191','2021-03-30','16:27:00'),('skPZyHt9TSc',199,'Emirate','E9191','2021-03-30','16:27:00'),('sLz6767Bhfc',199,'Emirate','E9191','2021-03-30','16:27:00'),('soCFyA3uEBp',211,'Emirate','E0000','2021-05-27','17:17:00'),('sP8uCXBsZED',211,'Emirate','E0000','2021-05-27','17:17:00'),('sPEfRYLCzoH',211,'Emirate','E0000','2021-05-27','17:17:00'),('sPosz6ZR6yt',199,'Emirate','E9191','2021-03-30','16:27:00'),('sPUFWiNkrpq',199,'Emirate','E9191','2021-03-30','16:27:00'),('sQ2todXrjSe',199,'Emirate','E9191','2021-03-30','16:27:00'),('stDhMnKjKhV',211,'Emirate','E0000','2021-05-27','17:17:00'),('sTM5bT2VgAn',211,'Emirate','E0000','2021-05-27','17:17:00'),('T3YjQmq6Agp',211,'Emirate','E0000','2021-05-27','17:17:00'),('T4gMPqafsLb',211,'Emirate','E0000','2021-05-27','17:17:00'),('t7W9McEzXYd',211,'Emirate','E0000','2021-05-27','17:17:00'),('Ta8Rb7oSAca',211,'Emirate','E0000','2021-05-27','17:17:00'),('tC4s4PxGxeH',211,'Emirate','E0000','2021-05-27','17:17:00'),('TfYJwga5Uvx',211,'Emirate','E0000','2021-05-27','17:17:00'),('thxQvseK3z4',211,'Emirate','E0000','2021-05-27','17:17:00'),('tLYQKj3ZtYB',199,'Emirate','E9191','2021-03-30','16:27:00'),('TpitxGFv2Hi',211,'Emirate','E0000','2021-05-27','17:17:00'),('TpmfaZt3Zhy',199,'Emirate','E9191','2021-03-30','16:27:00'),('TPxmoHtVHbT',199,'Emirate','E9191','2021-03-30','16:27:00'),('TqDSv3u2JmX',211,'Emirate','E0000','2021-05-27','17:17:00'),('tVue7AzaDTX',211,'Emirate','E0000','2021-05-27','17:17:00'),('TZhvXwKVSaA',211,'Emirate','E0000','2021-05-27','17:17:00'),('TzoqzTWfh2J',211,'Emirate','E0000','2021-05-27','17:17:00'),('U2artephFhY',199,'Emirate','E9191','2021-03-30','16:27:00'),('u2EqLtqvQaq',211,'Emirate','E0000','2021-05-27','17:17:00'),('U7ecUL5XVbj',199,'Emirate','E9191','2021-03-30','16:27:00'),('u8XqbvKTLE2',211,'Emirate','E0000','2021-05-27','17:17:00'),('uB8vt7J3RJn',211,'Emirate','E0000','2021-05-27','17:17:00'),('UCHGfjTPyQf',199,'Emirate','E9191','2021-03-30','16:27:00'),('ueHPYTPkwWk',211,'Emirate','E0000','2021-05-27','17:17:00'),('UhbfhFSDZBp',199,'Emirate','E9191','2021-03-30','16:27:00'),('uhyBgbD57nr',199,'Emirate','E9191','2021-03-30','16:27:00'),('UJm34pBHCnb',199,'Emirate','E9191','2021-03-30','16:27:00'),('UNUUryjsaDV',199,'Emirate','E9191','2021-03-30','16:27:00'),('UorNY77j9V4',211,'Emirate','E0000','2021-05-27','17:17:00'),('UPA3JFcRNZg',211,'Emirate','E0000','2021-05-27','17:17:00'),('UQp9RXccKf9',211,'Emirate','E0000','2021-05-27','17:17:00'),('uR7PRqBTeiT',211,'Emirate','E0000','2021-05-27','17:17:00'),('UsK9KmrQSDs',211,'Emirate','E0000','2021-05-27','17:17:00'),('uVRm6zfx2eU',211,'Emirate','E0000','2021-05-27','17:17:00'),('uwRiUZamRdv',199,'Emirate','E9191','2021-03-30','16:27:00'),('UWw8KZaSMQX',199,'Emirate','E9191','2021-03-30','16:27:00'),('Ux9koHLkBFh',199,'Emirate','E9191','2021-03-30','16:27:00'),('UZFKmDUDVkN',199,'Emirate','E9191','2021-03-30','16:27:00'),('v6yQ4du9BBh',211,'Emirate','E0000','2021-05-27','17:17:00'),('v9edRFw8QV6',199,'Emirate','E9191','2021-03-30','16:27:00'),('VeCDnHzDXe7',211,'Emirate','E0000','2021-05-27','17:17:00'),('Vfmvf9A8MzR',199,'Emirate','E9191','2021-03-30','16:27:00'),('vhPyL75oiC7',211,'Emirate','E0000','2021-05-27','17:17:00'),('vhw6CK6FquL',199,'Emirate','E9191','2021-03-30','16:27:00'),('vNNUGLgnxF9',199,'Emirate','E9191','2021-03-30','16:27:00'),('vP5wr5vkqb3',199,'Emirate','E9191','2021-03-30','16:27:00'),('vPKRNmSCAnV',211,'Emirate','E0000','2021-05-27','17:17:00'),('VpMHWrmDiRc',211,'Emirate','E0000','2021-05-27','17:17:00'),('VrBzFpNkhMV',199,'Emirate','E9191','2021-03-30','16:27:00'),('vRjxarQj4eE',211,'Emirate','E0000','2021-05-27','17:17:00'),('vRS3P2YEPiT',199,'Emirate','E9191','2021-03-30','16:27:00'),('vrZWMP3poSv',199,'Emirate','E9191','2021-03-30','16:27:00'),('vsC6fuZQeFh',211,'Emirate','E0000','2021-05-27','17:17:00'),('VVxh7kK6Znq',211,'Emirate','E0000','2021-05-27','17:17:00'),('vxzVtPCx6PF',211,'Emirate','E0000','2021-05-27','17:17:00'),('VYyCYXmdieb',211,'Emirate','E0000','2021-05-27','17:17:00'),('vz9RHbNPLVR',199,'Emirate','E9191','2021-03-30','16:27:00'),('VZw6Nq2CLkL',199,'Emirate','E9191','2021-03-30','16:27:00'),('W5pUAse7dRt',211,'Emirate','E0000','2021-05-27','17:17:00'),('WbCpAD4Hahj',199,'Emirate','E9191','2021-03-30','16:27:00'),('WgZN3mrvPgh',211,'Emirate','E0000','2021-05-27','17:17:00'),('wgzngLSsHnt',199,'Emirate','E9191','2021-03-30','16:27:00'),('wHoqNTw4XcR',211,'Emirate','E0000','2021-05-27','17:17:00'),('wkmJScYj3bu',199,'Emirate','E9191','2021-03-30','16:27:00'),('wmzL3qtrtwH',199,'Emirate','E9191','2021-03-30','16:27:00'),('WNrRsJHYfdw',211,'Emirate','E0000','2021-05-27','17:17:00'),('wpPhUdcbqkV',211,'Emirate','E0000','2021-05-27','17:17:00'),('WqL7y2KTZUG',211,'Emirate','E0000','2021-05-27','17:17:00'),('wQopE845XzP',211,'Emirate','E0000','2021-05-27','17:17:00'),('WRiih3CqZXG',199,'Emirate','E9191','2021-03-30','16:27:00'),('WSczzaHvWhz',199,'Emirate','E9191','2021-03-30','16:27:00'),('WtFvxFEA5hW',199,'Emirate','E9191','2021-03-30','16:27:00'),('wUHFGyQiGC2',199,'Emirate','E9191','2021-03-30','16:27:00'),('wuzRwXvzfpq',199,'Emirate','E9191','2021-03-30','16:27:00'),('wWWP2PJwU3N',199,'Emirate','E9191','2021-03-30','16:27:00'),('wx4EPoQnqoQ',211,'Emirate','E0000','2021-05-27','17:17:00'),('wxm5FRoWMho',199,'Emirate','E9191','2021-03-30','16:27:00'),('wYrPKfDmRaM',211,'Emirate','E0000','2021-05-27','17:17:00'),('X2AJz9XMgTy',199,'Emirate','E9191','2021-03-30','16:27:00'),('x3BHsk8zRcq',211,'Emirate','E0000','2021-05-27','17:17:00'),('X8gi8JiFNkC',199,'Emirate','E9191','2021-03-30','16:27:00'),('XACJF6DATt8',211,'Emirate','E0000','2021-05-27','17:17:00'),('XdhLPdhffgT',199,'Emirate','E9191','2021-03-30','16:27:00'),('XHdEQw7Xcg3',199,'Emirate','E9191','2021-03-30','16:27:00'),('xHe4D2YXRV6',199,'Emirate','E9191','2021-03-30','16:27:00'),('xHMERrtdKVb',199,'Emirate','E9191','2021-03-30','16:27:00'),('xLhmKYZYTLW',199,'Emirate','E9191','2021-03-30','16:27:00'),('XqcJTKPCNGW',199,'Emirate','E9191','2021-03-30','16:27:00'),('XUG5YmZPgMN',211,'Emirate','E0000','2021-05-27','17:17:00'),('xvkomHb6xzj',211,'Emirate','E0000','2021-05-27','17:17:00'),('xVLqJLfNyGx',199,'Emirate','E9191','2021-03-30','16:27:00'),('XWy3MzLwTLx',199,'Emirate','E9191','2021-03-30','16:27:00'),('XxEFGj4ocC5',211,'Emirate','E0000','2021-05-27','17:17:00'),('XZQk8e7fh5k',211,'Emirate','E0000','2021-05-27','17:17:00'),('xzZj8c2j267',199,'Emirate','E9191','2021-03-30','16:27:00'),('Y4AdGALxruv',211,'Emirate','E0000','2021-05-27','17:17:00'),('Y7mYPihHRUn',199,'Emirate','E9191','2021-03-30','16:27:00'),('y8jNQJx4xxc',199,'Emirate','E9191','2021-03-30','16:27:00'),('Y9LiqhUPsLB',211,'Emirate','E0000','2021-05-27','17:17:00'),('YbBE9PTdMot',211,'Emirate','E0000','2021-05-27','17:17:00'),('YC7qHDvyhnU',199,'Emirate','E9191','2021-03-30','16:27:00'),('yFKZBoYjojM',199,'Emirate','E9191','2021-03-30','16:27:00'),('ygMWjouXrR2',211,'Emirate','E0000','2021-05-27','17:17:00'),('YipqqMsFyLx',211,'Emirate','E0000','2021-05-27','17:17:00'),('YJD9fMAhuWy',199,'Emirate','E9191','2021-03-30','16:27:00'),('yk3Vz5Ju8aT',199,'Emirate','E9191','2021-03-30','16:27:00'),('yMBYzf79NVc',199,'Emirate','E9191','2021-03-30','16:27:00'),('YoC7FyemvF9',211,'Emirate','E0000','2021-05-27','17:17:00'),('YoX4p9VwApn',199,'Emirate','E9191','2021-03-30','16:27:00'),('YPg4jVH92Rg',211,'Emirate','E0000','2021-05-27','17:17:00'),('yRNYXqeGoG7',211,'Emirate','E0000','2021-05-27','17:17:00'),('yrq8juy8sid',211,'Emirate','E0000','2021-05-27','17:17:00'),('YRQYez5bhX5',211,'Emirate','E0000','2021-05-27','17:17:00'),('YsSTAQFsBpo',199,'Emirate','E9191','2021-03-30','16:27:00'),('yt2Yn9abY7k',199,'Emirate','E9191','2021-03-30','16:27:00'),('yujxtFzy9gt',211,'Emirate','E0000','2021-05-27','17:17:00'),('yvFxJ8VQY6i',199,'Emirate','E9191','2021-03-30','16:27:00'),('YvtAQTcgZdk',199,'Emirate','E9191','2021-03-30','16:27:00'),('YWb7gAHQLix',211,'Emirate','E0000','2021-05-27','17:17:00'),('YZnFFap4pHk',199,'Emirate','E9191','2021-03-30','16:27:00'),('Z3vXozz44mu',211,'Emirate','E0000','2021-05-27','17:17:00'),('Z4f5wypULJU',199,'Emirate','E9191','2021-03-30','16:27:00'),('Z86V5f3uGPE',211,'Emirate','E0000','2021-05-27','17:17:00'),('ZAmyyHdjbMi',199,'Emirate','E9191','2021-03-30','16:27:00'),('zco9rwionS6',211,'Emirate','E0000','2021-05-27','17:17:00'),('zetAso4WP4H',211,'Emirate','E0000','2021-05-27','17:17:00'),('zFpTx5cVxvz',199,'Emirate','E9191','2021-03-30','16:27:00'),('zi6atxW5yj8',199,'Emirate','E9191','2021-03-30','16:27:00'),('Zj9yGyNEfKR',199,'Emirate','E9191','2021-03-30','16:27:00'),('ZjgxHJg9gfd',211,'Emirate','E0000','2021-05-27','17:17:00'),('ZNBkivtD4JM',199,'Emirate','E9191','2021-03-30','16:27:00'),('ZPNLuYReRHh',211,'Emirate','E0000','2021-05-27','17:17:00'),('zQSL9zg2kgD',211,'Emirate','E0000','2021-05-27','17:17:00'),('zStcHfH7iYh',199,'Emirate','E9191','2021-03-30','16:27:00'),('ZSVxQsPm2mj',211,'Emirate','E0000','2021-05-27','17:17:00'),('zUQ3zPvYFBD',199,'Emirate','E9191','2021-03-30','16:27:00'),('zuXLx9MVm3r',211,'Emirate','E0000','2021-05-27','17:17:00'),('zVT7BsPrJxg',211,'Emirate','E0000','2021-05-27','17:17:00'),('zwLgzrPQKNt',199,'Emirate','E9191','2021-03-30','16:27:00'),('zWtwM37Z9B3',199,'Emirate','E9191','2021-03-30','16:27:00'),('zwX2iAwSGeu',211,'Emirate','E0000','2021-05-27','17:17:00'),('zynafkCotvj',199,'Emirate','E9191','2021-03-30','16:27:00'),('ZzE2SdVGkrU',199,'Emirate','E9191','2021-03-30','16:27:00'),('ZZzwtCLjfDK',211,'Emirate','E0000','2021-05-27','17:17:00');
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-05 15:26:04
