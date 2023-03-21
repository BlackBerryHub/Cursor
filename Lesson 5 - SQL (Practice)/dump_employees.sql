-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: employees
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `country_name` varchar(255) NOT NULL,
  `region_id` int NOT NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `country_id` (`country_id`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `countries_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `regions` (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'United States',1),(2,'Canada',1),(3,'Mexico',1),(4,'Brazil',2),(5,'Argentina',2),(6,'France',3),(7,'Germany',3),(8,'China',4),(9,'Japan',4),(10,'South Africa',5);
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(255) NOT NULL,
  `manager_id` int NOT NULL,
  `location_id` int NOT NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE KEY `department_id` (`department_id`),
  KEY `departments_ibfk_1` (`manager_id`),
  KEY `departments_ibfk_2` (`location_id`),
  CONSTRAINT `departments_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `departments_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Sales',1,1),(2,'Marketing',2,2),(3,'Finance',3,3),(4,'Human Resources',4,4),(5,'Research and Development',5,5),(6,'Information Technology',6,6),(7,'Legal',7,7),(8,'Customer Service',8,8),(9,'Operations',9,9),(10,'Procurement',10,10);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `hire_date` varchar(255) DEFAULT NULL,
  `job_id` int NOT NULL,
  `salary` int DEFAULT NULL,
  `commission_pct` int DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `department_id` int NOT NULL,
  UNIQUE KEY `employee_id` (`employee_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  KEY `job_id` (`job_id`),
  KEY `employees_ibfk_2` (`department_id`),
  KEY `employees_ibfk_3` (`manager_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'John','Doe','johndoe@example.com','123-456-7890','2022-01-01',1,50000,0,1,1),(2,'Jane','Smith','janesmith@example.com','234-567-8901','2022-01-02',2,60000,0,1,1),(3,'Bob','Johnson','bobjohnson@example.com','345-678-9012','2022-01-03',3,70000,0,2,2),(4,'Sarah','Williams','sarahwilliams@example.com','456-789-0123','2022-01-04',4,80000,0,2,2),(5,'Mike','Brown','mikebrown@example.com','567-890-1234','2022-01-05',5,90000,0,3,3),(6,'Emily','Davis','emilydavis@example.com','678-901-2345','2022-01-06',6,100000,0,3,3),(7,'David','Garcia','davidgarcia@example.com','789-012-3456','2022-01-07',7,110000,0,4,4),(8,'Olivia','Lopez','olivialopez@example.com','890-123-4567','2022-01-08',8,120000,0,4,4),(9,'George','Martinez','georgemartinez@example.com','901-234-5678','2022-01-09',9,130000,0,5,5),(10,'Isabella','Gonzalez','isabellagonzalez@example.com','012-345-6789','2022-01-10',10,140000,0,5,5),(11,'Peter','Lee','peterlee@example.com','123-456-7891','2022-01-11',1,50000,0,1,6),(12,'Linda','Wang','lindawang@example.com','234-567-8902','2022-01-12',2,60000,0,1,6),(13,'Tom','Chen','tomchen@example.com','345-678-9013','2022-01-13',3,70000,0,2,7),(14,'Grace','Zhang','gracezhang@example.com','456-789-0124','2022-01-14',4,80000,0,2,7),(15,'Steven','Wu','stevenwu@example.com','567-890-1235','2022-01-15',5,90000,0,3,8),(16,'John','Doe','john.doe@company.com','223-456-7890','2021-01-01',3,50000,10,3,1),(17,'Jane','Smith','jane.smith@company.com','334-567-8901','2021-02-15',4,55000,12,4,2),(18,'Mark','Johnson','mark.johnson@company.com','445-678-9012','2021-03-01',3,50000,10,3,1),(19,'Emily','Davis','emily.davis@company.com','556-789-0123','2021-04-15',5,60000,11,5,3),(20,'Michael','Wilson','michael.wilson@company.com','667-890-1234','2021-05-01',3,50000,10,3,1),(21,'Sarah','Brown','sarah.brown@company.com','778-901-2345','2021-06-15',4,55000,12,4,2),(22,'David','Anderson','david.anderson@company.com','889-012-3456','2021-07-01',5,60000,11,5,3),(23,'Jessica','Garcia','jessica.garcia@company.com','990-123-4567','2021-08-15',3,50000,10,3,1),(24,'James','Thomas','james.thomas@company.com','001-234-5678','2021-09-01',4,55000,12,4,2),(25,'Linda','Lee','linda.lee@company.com','032-345-6789','2021-10-15',5,60000,11,5,3);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_history`
--

DROP TABLE IF EXISTS `job_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_history` (
  `employee_id` int NOT NULL,
  `start_date` varchar(255) NOT NULL,
  `end_date` varchar(255) NOT NULL,
  `job_id` int NOT NULL,
  `department_id` int NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `job_id` (`job_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `job_history_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`),
  CONSTRAINT `job_history_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`),
  CONSTRAINT `job_history_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_history`
--

LOCK TABLES `job_history` WRITE;
/*!40000 ALTER TABLE `job_history` DISABLE KEYS */;
INSERT INTO `job_history` VALUES (1,'2022-01-01','2022-01-20',1,1),(2,'2022-01-20','2022-04-20',3,2),(3,'2023-02-12','2023-02-26',9,6),(4,'2023-02-06','2023-03-03',9,2),(5,'2023-01-12','2023-03-01',5,8),(6,'2023-01-18','2023-03-01',6,7),(7,'2023-02-22','2023-03-04',7,5),(8,'2023-02-12','2023-03-17',3,6),(9,'2023-02-19','2023-03-19',1,2),(10,'2023-03-12','2023-03-18',3,9);
/*!40000 ALTER TABLE `job_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `job_title` varchar(255) NOT NULL,
  `min_salary` int DEFAULT NULL,
  `max_salary` int DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  UNIQUE KEY `job_id` (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,'Accountant',40000,80000),(2,'Administration Assistant',25000,35000),(3,'Chief Executive Officer',150000,300000),(4,'Chief Financial Officer',125000,250000),(5,'Chief Operating Officer',125000,250000),(6,'Database Administrator',60000,120000),(7,'Developer',70000,130000),(8,'Graphic Designer',45000,85000),(9,'Human Resources Specialist',50000,90000),(10,'Information Security Analyst',75000,130000),(11,'IT Manager',100000,200000),(12,'Marketing Manager',75000,150000),(13,'Network Administrator',60000,120000),(14,'Project Manager',80000,150000),(15,'Quality Assurance Tester',50000,95000),(16,'Sales Manager',75000,150000),(17,'Software Engineer',80000,150000),(18,'Technical Writer',50000,90000),(19,'Web Designer',50000,90000),(20,'Web Developer',60000,120000);
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `street_address` varchar(255) NOT NULL,
  `postal_code` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state_province` varchar(255) DEFAULT NULL,
  `country_id` int NOT NULL,
  UNIQUE KEY `location_id` (`location_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'123 Main St','10001','New York','NY',1),(2,'456 1st Ave','V6C 1A1','Vancouver','BC',2),(3,'789 2nd St','01001','Mexico City','CDMX',3),(4,'234 3rd Ave','01432','Sao Paulo','SP',4),(5,'567 4th St','14201','Buenos Aires','BA',5),(6,'890 5th Ave','75008','Paris','Ile-de-France',6),(7,'1234 6th St','10178','Berlin','Berlin',7),(8,'5678 7th Ave','100000','Beijing','Beijing',8),(9,'9012 8th St','100-0001','Tokyo','Tokyo',9),(10,'3456 9th Ave','7100','Cape Town','Western Cape',10);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regions` (
  `region_id` int NOT NULL AUTO_INCREMENT,
  `region_name` varchar(255) NOT NULL,
  PRIMARY KEY (`region_id`),
  UNIQUE KEY `region_id` (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
INSERT INTO `regions` VALUES (1,'North America'),(2,'South America'),(3,'Europe'),(4,'Asia'),(5,'Africa'),(6,'Australia'),(7,'Middle East'),(8,'Caribbean'),(9,'Central America'),(10,'Antarctica');
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-21 23:41:25
