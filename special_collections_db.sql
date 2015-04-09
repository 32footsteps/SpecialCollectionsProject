-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: special_collections_db
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_4fe58bc8340c2ad9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_2a2d382d45abcb59_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_24c98332c6358ed9_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add sc user',6,'add_scuser'),(17,'Can change sc user',6,'change_scuser'),(18,'Can delete sc user',6,'delete_scuser'),(19,'Can add collection',7,'add_collection'),(20,'Can change collection',7,'change_collection'),(21,'Can delete collection',7,'delete_collection'),(22,'Can add item',8,'add_item'),(23,'Can change item',8,'change_item'),(24,'Can delete item',8,'delete_item'),(25,'Can add temp item',9,'add_tempitem'),(26,'Can change temp item',9,'change_tempitem'),(27,'Can delete temp item',9,'delete_tempitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_collection`
--

DROP TABLE IF EXISTS `collection_collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collection_collection` (
  `collection_name` varchar(70) NOT NULL,
  `collection_description` longtext NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`collection_name`),
  KEY `collection_collection_4f331e2f` (`author_id`),
  CONSTRAINT `collecti_author_id_494e68f61f987fa9_fk_collection_user_scuser_id` FOREIGN KEY (`author_id`) REFERENCES `collection_user_scuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_collection`
--

LOCK TABLES `collection_collection` WRITE;
/*!40000 ALTER TABLE `collection_collection` DISABLE KEYS */;
INSERT INTO `collection_collection` VALUES ('Fuck','shit','2015-04-02 22:40:34','2015-04-02 22:40:34',2),('Fuck jk','gbhujnkml','2015-04-05 08:25:54','2015-04-05 08:25:54',1),('Jew Gold','Shit','2015-03-30 16:56:29','2015-03-30 16:56:29',1),('sdljfsdlfj','lsjlfjdsfdfs\r\n','2015-04-02 22:21:39','2015-04-02 22:21:39',1);
/*!40000 ALTER TABLE `collection_collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_collection_item`
--

DROP TABLE IF EXISTS `collection_collection_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collection_collection_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collection_id` varchar(70) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `collection_id` (`collection_id`,`item_id`),
  KEY `collection_collection_item_0a1a4dd8` (`collection_id`),
  KEY `collection_collection_item_82bfda79` (`item_id`),
  CONSTRAINT `b5773ae51d8dddafc52f8036cfed4a3c` FOREIGN KEY (`collection_id`) REFERENCES `collection_collection` (`collection_name`),
  CONSTRAINT `collection_c_item_id_6e5d702893be56ed_fk_collection_item_item_id` FOREIGN KEY (`item_id`) REFERENCES `collection_item_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_collection_item`
--

LOCK TABLES `collection_collection_item` WRITE;
/*!40000 ALTER TABLE `collection_collection_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `collection_collection_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_item_item`
--

DROP TABLE IF EXISTS `collection_item_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collection_item_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `subject` varchar(120) NOT NULL,
  `description` longtext NOT NULL,
  `publisher` varchar(80) NOT NULL,
  `contributor` varchar(80) NOT NULL,
  `date` datetime NOT NULL,
  `item_type` varchar(80) NOT NULL,
  `item_format` varchar(20) NOT NULL,
  `identifier` varchar(40) NOT NULL,
  `source` varchar(40) NOT NULL,
  `language` varchar(40) NOT NULL,
  `relation` varchar(40) NOT NULL,
  `coverage` varchar(80) NOT NULL,
  `rights` varchar(80) NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `item_image` varchar(100) NOT NULL,
  `creator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `collection_item_item_3700153c` (`creator_id`),
  CONSTRAINT `collect_creator_id_1e5939efa6596248_fk_collection_user_scuser_id` FOREIGN KEY (`creator_id`) REFERENCES `collection_user_scuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_item_item`
--

LOCK TABLES `collection_item_item` WRITE;
/*!40000 ALTER TABLE `collection_item_item` DISABLE KEYS */;
INSERT INTO `collection_item_item` VALUES (1,'Jews and Their Gold','General Jewery','kfdskfkdsj','kjdfsjdsjkf','kjhdklfjdsjflk','2015-03-30 16:58:07','kdsfds','sdfsd','sdfsdf','sdfsdf','sdfsdfs','dsfsdf','sdfsdf','sdfsd','2015-03-30 16:58:08',0,'media/1t1rAFi.jpg',1),(2,'Shit Cowboys','Cowboys in Pueblo','Shit Cowboys are still cowboys','Jew World','Me','2015-03-31 16:18:14','Mime','Shit','Joos','None','Farsi','None','kldf','Jew','2015-03-31 16:18:15',0,'media/1N4bP.jpg',1),(3,'Jew ABlls','sdsf','xfvxvxxc','xcvxv','vxcvx','2015-04-05 07:26:58','xcvx','xcvxcv','xcvxc','xcvcxv','xcvxcv','xcvxc','xcvx','xcvxc','2015-04-05 07:26:58',0,'media/00I0I_2CIF1RGme3L_600x450_niR2juj.jpg',2),(4,'Jew Shit','fddgdfgd','fgffg','dfgd','dfgdfg','2015-04-05 07:27:29','dfgdf','dfgdfg','dfgdfg','dfgd','dfgdfg','dfgd','dfg','dfg','2015-04-05 07:27:29',0,'media/4CV7kyq.jpg',2),(5,'Jew Shit rtr','rtryrty','rtytry','rtyr','rtyrty','2015-04-05 07:28:19','','rtyr','rt','rtyrty','yy','yy','','','2015-04-05 07:28:19',0,'media/00505_89R9PSBpI5B_600x450.jpg',2),(6,'Jew Habalas','asdasd','asdasdsa','asdasd','asdasd','2015-04-05 07:30:01','','asdasd','asdasd','asdsad','asdasd','sadasd','','','2015-04-05 07:30:01',0,'media/8326580594_ec8b059b81_b.jpg',2),(7,'Jewery Shit','dsfdsfdf','dsfdsf','dfdsf','dsfsdf','2015-04-05 07:30:36','sdfsd','dsfsf','dsfsd','sdfsd','sdfsd','sdfsdf','','','2015-04-05 07:30:36',0,'media/8255108403_4c26d63bc0_h.jpg',2),(8,'Jew Shit sdf','dsfdsf','sdfdsf','dsfsdf','sdfds','2015-04-05 07:31:04','','sdfsd','sdf','rvrvr','vvfv','vfvf','','','2015-04-05 07:31:04',0,'media/andy-lee01.jpg',2),(9,'gaf','shit','Fart shit','sdddsf','Dick Fill','2015-04-05 07:36:19','','dsfds','sdfs','dsfdsf','sdfdsf','sfsdf','','','2015-04-05 07:36:19',0,'media/andy-lee04.jpg',2);
/*!40000 ALTER TABLE `collection_item_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_item_tempitem`
--

DROP TABLE IF EXISTS `collection_item_tempitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collection_item_tempitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `temp_item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `collection_item_tempitem_197690eb` (`temp_item_id`),
  CONSTRAINT `collect_temp_item_id_2f9f3a281b7fe610_fk_collection_item_item_id` FOREIGN KEY (`temp_item_id`) REFERENCES `collection_item_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_item_tempitem`
--

LOCK TABLES `collection_item_tempitem` WRITE;
/*!40000 ALTER TABLE `collection_item_tempitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `collection_item_tempitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_user_scuser`
--

DROP TABLE IF EXISTS `collection_user_scuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collection_user_scuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `email` varchar(75) NOT NULL,
  `username` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_user_scuser`
--

LOCK TABLES `collection_user_scuser` WRITE;
/*!40000 ALTER TABLE `collection_user_scuser` DISABLE KEYS */;
INSERT INTO `collection_user_scuser` VALUES (1,'pbkdf2_sha256$15000$yZtYrNVFtcY9$rRV/BbbBytHSUJswOF/yCpYycxKbFA2lBt67z3+JZwc=','2015-04-08 17:46:09','issou@gmail.com','zissou','michael','degraw',1,'2015-03-30 16:52:38','2015-03-30 16:52:38'),(2,'pbkdf2_sha256$15000$UlEJz2ELJVFJ$s3Xwq7AZ2dyYsfv8q3wBh0rcNuybrZEP4iKs6V/WAZU=','2015-04-06 21:16:39','shit@jjew.xom','shittit','ssdkj	','skdj',1,'2015-04-02 22:23:04','2015-04-02 22:23:04');
/*!40000 ALTER TABLE `collection_user_scuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_adm_user_id_7b001ab949c6048e_fk_collection_user_scuser_id` FOREIGN KEY (`user_id`) REFERENCES `collection_user_scuser` (`id`),
  CONSTRAINT `djang_content_type_id_1da037826d73c83c_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_7e2ef51e88d364c3_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'sc user','collection_user','scuser'),(7,'collection','collection','collection'),(8,'item','collection_item','item'),(9,'temp item','collection_item','tempitem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-03-30 16:52:07'),(2,'collection_user','0001_initial','2015-03-30 16:52:08'),(3,'admin','0001_initial','2015-03-30 16:52:09'),(4,'auth','0001_initial','2015-03-30 16:52:11'),(5,'sessions','0001_initial','2015-03-30 16:52:11'),(6,'collection_item','0001_initial','2015-03-30 16:54:22'),(7,'collection_item','0002_item_is_approved','2015-03-30 16:54:23'),(8,'collection_item','0003_auto_20150329_2126','2015-03-30 16:54:24'),(9,'collection_item','0004_auto_20150330_1522','2015-03-30 16:54:24'),(10,'collection','0001_initial','2015-03-30 16:54:26'),(11,'collection','0002_auto_20150329_1448','2015-03-30 16:54:27'),(12,'collection','0003_auto_20150329_1539','2015-03-30 16:54:28'),(13,'collection','0004_auto_20150330_1522','2015-03-30 16:54:28'),(14,'collection','0005_auto_20150330_1620','2015-03-30 16:54:29'),(15,'collection','0006_auto_20150330_1621','2015-03-30 16:54:30'),(16,'collection','0007_auto_20150330_1628','2015-03-30 16:54:30'),(17,'collection','0008_remove_collection_author','2015-03-30 16:54:31'),(18,'collection','0009_collection_author','2015-03-30 16:54:32'),(19,'collection','0010_auto_20150330_1637','2015-03-30 16:54:33'),(20,'collection_item','0005_auto_20150330_1637','2015-03-30 16:54:34'),(21,'collection_item','0006_item_tempitem','2015-03-30 16:54:36'),(22,'collection','0011_collection','2015-03-30 16:54:38');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('66bmapj49a2rgcyifxw67dtwbl53l30u','NjI1OWNmNjFiNDBkZmQ5M2NkMzIxZWQyY2VjMjEwZDU1OWU0NWViYzp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWQ2Y2E1ODA1NTBiNzhiNWVhNTk1OGE0NDQ3ZTkwMmIyZjBiNjlmNSJ9','2015-04-21 08:49:27'),('9grbs6rxq6p7uc5xzqqm0ujy9sxx3ny2','NjI1OWNmNjFiNDBkZmQ5M2NkMzIxZWQyY2VjMjEwZDU1OWU0NWViYzp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWQ2Y2E1ODA1NTBiNzhiNWVhNTk1OGE0NDQ3ZTkwMmIyZjBiNjlmNSJ9','2015-04-21 08:48:58'),('dtsaafr7x9ezvpyoqfqr8aazhjoz30b8','NjI1OWNmNjFiNDBkZmQ5M2NkMzIxZWQyY2VjMjEwZDU1OWU0NWViYzp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWQ2Y2E1ODA1NTBiNzhiNWVhNTk1OGE0NDQ3ZTkwMmIyZjBiNjlmNSJ9','2015-04-22 17:46:09'),('rhrcmuq842swps3t643jlena0jd10v86','NjI1OWNmNjFiNDBkZmQ5M2NkMzIxZWQyY2VjMjEwZDU1OWU0NWViYzp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWQ2Y2E1ODA1NTBiNzhiNWVhNTk1OGE0NDQ3ZTkwMmIyZjBiNjlmNSJ9','2015-04-20 08:02:47'),('yxbljmfchw7oak6z5s5y5gbrnaa2e8nn','NmZjMzNiZmY5M2I5ODU4OGNiYmRiZjJiYTgyZTNiNzhhZWEyMGJkNzp7fQ==','2015-04-23 07:16:58');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-09 13:17:48
