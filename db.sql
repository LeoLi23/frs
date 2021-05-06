-- MySQL dump 10.13  Distribute 8.0.22, for osx10.16 (x86_64)
--
-- Host: localhost    Database: frs_prod
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

CREATE DATABASE IF NOT EXISTS `frs_prod`DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE `frs_prod`;

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
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `ticket_id` varchar(30) NOT NULL,
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

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

