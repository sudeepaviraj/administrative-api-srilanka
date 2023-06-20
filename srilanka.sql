-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2023 at 03:51 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `srilanka`
--

-- --------------------------------------------------------

--
-- Table structure for table `districts`
--

CREATE TABLE `districts` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `province_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `districts`
--

INSERT INTO `districts` (`id`, `name`, `province_id`) VALUES
(42, 'Colombo', 63),
(43, 'Gampaha', 63),
(44, 'Kalutara', 63),
(45, 'Kandy', 64),
(46, 'Matale', 64),
(47, 'Nuwara Eliya', 64),
(48, 'Galle', 65),
(49, 'Matara', 65),
(50, 'Hambantota', 65),
(51, 'Jaffna', 66),
(52, 'Mannar', 66),
(53, 'Vavuniya', 66),
(54, 'Mullaitivu', 66),
(55, 'Kilinochchi', 66),
(56, 'Batticaloa', 67),
(57, 'Ampara', 67),
(58, 'Trincomalee', 67),
(59, 'Kurunegala', 68),
(60, 'Puttalam', 68),
(61, 'Anuradhapura', 69),
(62, 'Polonnaruwa', 69),
(63, 'Badulla', 70),
(64, 'Moneragala', 70),
(65, 'Ratnapura', 71),
(66, 'Kegalle', 71);

-- --------------------------------------------------------

--
-- Table structure for table `divisions`
--

CREATE TABLE `divisions` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `district_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `divisions`
--

INSERT INTO `divisions` (`id`, `name`, `district_id`) VALUES
(950, 'Colombo', 42),
(951, 'Kolonnawa', 42),
(952, 'Kaduwela', 42),
(953, ' Homagama', 42),
(954, ' Hanwella', 42),
(955, ' Padukka', 42),
(956, ' Maharagama', 42),
(957, ' Sri Jayawardanapura Kotte', 42),
(958, ' Thimbirigasyaya', 42),
(959, ' Dehiwala-Mount Lavinia', 42),
(960, ' Ratmalana', 42),
(961, ' Moratuwa', 42),
(962, ' Kesbewa', 42),
(963, 'Negombo', 43),
(964, 'Katana', 43),
(965, 'Divulapitiya', 43),
(966, ' Mirigama', 43),
(967, ' Minuwangoda', 43),
(968, ' Wattala', 43),
(969, ' Ja-Ela', 43),
(970, ' Gampaha', 43),
(971, ' Attanagalla', 43),
(972, ' Dompe', 43),
(973, ' Mahara', 43),
(974, ' Kelaniya', 43),
(975, ' Biyagama', 43),
(976, 'Panadura', 44),
(977, 'Bandaragama', 44),
(978, 'Horana', 44),
(979, ' Ingiriya', 44),
(980, ' Bulathsinhala', 44),
(981, ' Madurawala', 44),
(982, ' Millaniya', 44),
(983, ' Kalutara', 44),
(984, ' Beruwala', 44),
(985, ' Dodangoda', 44),
(986, ' Mathugama', 44),
(987, ' Agalawatta', 44),
(988, ' Palindanuwara', 44),
(989, ' Walallavita', 44),
(990, 'Thumpane', 45),
(991, 'Poojapitiya', 45),
(992, 'Akurana', 45),
(993, ' Pathadumbara', 45),
(994, ' Panvila', 45),
(995, ' Udadumbara', 45),
(996, ' Minipe', 45),
(997, ' Medadumbara', 45),
(998, ' Kundasale', 45),
(999, ' Kandy Four Gravets & Gangawata Korale', 45),
(1000, ' Harispattuwa', 45),
(1001, ' Hatharaliyadda', 45),
(1002, ' Yatinuwara', 45),
(1003, ' Udunuwara', 45),
(1004, ' Doluwa', 45),
(1005, ' Pathahewaheta', 45),
(1006, ' Delthota', 45),
(1007, ' Udapalatha', 45),
(1008, ' Ganga Ihala Korale', 45),
(1009, ' Pasbage Korale', 45),
(1010, 'Galewela', 46),
(1011, 'Dambulla', 46),
(1012, 'Naula', 46),
(1013, ' Pallepola', 46),
(1014, ' Yatawatta', 46),
(1015, ' Matale', 46),
(1016, ' Ambanganga Korale', 46),
(1017, ' Laggala-Pallegama', 46),
(1018, ' Wilgamuwa', 46),
(1019, ' Rattota', 46),
(1020, ' Ukuwela', 46),
(1021, 'Kothmale', 47),
(1022, 'Hanguranketha', 47),
(1023, 'Walapane', 47),
(1024, ' Nuwara Eliya', 47),
(1025, ' Ambagamuwa', 47),
(1026, 'Benthota', 48),
(1027, 'Balapitiya', 48),
(1028, 'Karandeniya', 48),
(1029, ' Elpitiya', 48),
(1030, ' Niyagama', 48),
(1031, ' Thawalama', 48),
(1032, ' Neluwa', 48),
(1033, ' Nagoda', 48),
(1034, ' Baddegama', 48),
(1035, ' Welivitiya-Divithura', 48),
(1036, ' Ambalangoda', 48),
(1037, ' Hikkaduwa', 48),
(1038, ' Galle Four Gravets', 48),
(1039, ' Bope-Poddala', 48),
(1040, ' Akmeemana', 48),
(1041, ' Yakkalamulla', 48),
(1042, ' Imaduwa', 48),
(1043, ' Habaraduwa', 48),
(1044, 'Pitabeddara', 49),
(1045, 'Kotapola', 49),
(1046, 'Pasgoda', 49),
(1047, ' Mulatiyana', 49),
(1048, ' Athuraliya', 49),
(1049, ' Akuressa', 49),
(1050, ' Welipitiya', 49),
(1051, ' Malimbada', 49),
(1052, ' Kamburupitiya', 49),
(1053, ' Hakmana', 49),
(1054, ' Kirinda Puhulwella', 49),
(1055, ' Thihagoda', 49),
(1056, ' Weligama', 49),
(1057, ' Four Gravets', 49),
(1058, ' Devinuwara', 49),
(1059, ' Dickwella', 49),
(1060, 'Sooriyawewa', 50),
(1061, 'Lunugamvehera', 50),
(1062, 'Tissamaharama', 50),
(1063, ' Hambantota', 50),
(1064, ' Ambalantota', 50),
(1065, ' Angunakolapelessa', 50),
(1066, ' Weeraketiya', 50),
(1067, ' Katuwana', 50),
(1068, ' Okewela', 50),
(1069, ' Beliatta', 50),
(1070, ' Tangalle', 50),
(1071, 'Island North (Kayts)', 51),
(1072, 'Valikamam West (Chankanai)', 51),
(1073, 'Valikamam South-West (Sandilipay)', 51),
(1074, ' Valikamam North (Tellipallai)', 51),
(1075, ' Valikamam South (Uduvil)', 51),
(1076, ' valikamam-East(kopayi)', 51),
(1077, ' Vadamaradchy South-West, Karaveddy', 51),
(1078, ' Vadamaradchi East (Maruthnkerny)', 51),
(1079, ' Vadamaradchi North (Point Pedro)', 51),
(1080, ' Thenmaradchi (Chavakachcheri)', 51),
(1081, ' Nallur', 51),
(1082, ' Jaffna', 51),
(1083, ' Island South ,Velanai', 51),
(1084, ' Delft', 51),
(1085, 'Mannar Town', 52),
(1086, 'Manthai West', 52),
(1087, 'Madhu', 52),
(1088, ' Nanaddan', 52),
(1089, ' Musalai', 52),
(1090, 'Vavuniya North', 53),
(1091, 'Vavuniya South', 53),
(1092, 'Vavuniya', 53),
(1093, ' Vengalacheddikulam', 53),
(1094, 'Thunukkai', 54),
(1095, 'Manthai East', 54),
(1096, 'Puthukudiyiruppu', 54),
(1097, ' Oddusuddan', 54),
(1098, ' Maritimepattu', 54),
(1099, 'Pachchilaipalli', 55),
(1100, 'Kandavalai', 55),
(1101, 'Karachchi', 55),
(1102, ' Poonakary', 55),
(1103, 'Koralai Pattu North', 56),
(1104, 'Koralai Pattu West (Oddamavadi)', 56),
(1105, 'Koralai Pattu (Valachchenai)', 56),
(1106, ' Eravur Pattu', 56),
(1107, ' Eravur Town', 56),
(1108, ' Manmunai North', 56),
(1109, ' Manmunai West', 56),
(1110, ' Kattankudy', 56),
(1111, ' Manmunai Pattu (Arayampathy', 56),
(1112, ' Manmunai South-West', 56),
(1113, ' Porativu Pattu', 56),
(1114, ' Manmunai South & Eruvil Pattu', 56),
(1115, ' Koralai Pattu South (Kiran)', 56),
(1116, 'Dehiattakandiya', 57),
(1117, 'Padiyathalawa', 57),
(1118, 'Mahaoya', 57),
(1119, ' Uhana', 57),
(1120, ' Ampara', 57),
(1121, ' Navithanvelly', 57),
(1122, ' Samanthurai', 57),
(1123, ' Kalmunai', 57),
(1124, ' Sainthamarathu', 57),
(1125, ' Karaitivu', 57),
(1126, ' Ninthavur', 57),
(1127, ' Addalaichenai', 57),
(1128, ' Irakkamam', 57),
(1129, ' Akkaraipattu', 57),
(1130, ' Alayadiwembu', 57),
(1131, ' Damana', 57),
(1132, ' Thirukkovil', 57),
(1133, ' Pothuvil', 57),
(1134, ' Lahugala', 57),
(1135, 'Padavi Sri Pura', 58),
(1136, 'Kuchchaveli', 58),
(1137, 'Gomarankadawala', 58),
(1138, ' Morawewa', 58),
(1139, ' Trincomalee Town and Gravets', 58),
(1140, ' Thambalagamuwa', 58),
(1141, ' Kantalai', 58),
(1142, ' Kinniya', 58),
(1143, ' Muthur', 58),
(1144, ' Seruwila', 58),
(1145, ' Verugal', 58),
(1146, 'Giribawa', 59),
(1147, 'Galgamuwa', 59),
(1148, 'Ehetuwewa', 59),
(1149, ' Ambanpola', 59),
(1150, ' Kotavehera', 59),
(1151, ' Rasnayakapura', 59),
(1152, ' Nikaweratiya', 59),
(1153, ' Mahawa', 59),
(1154, ' Polpithigama', 59),
(1155, ' Ibbagamuwa', 59),
(1156, ' Ganewatta', 59),
(1157, ' Wariyapola', 59),
(1158, ' Kobeigane', 59),
(1159, ' Bingiriya', 59),
(1160, ' Panduwasnuwara', 59),
(1161, ' Paduwasnuwara East ', 59),
(1162, ' Bamunakotuwa', 59),
(1163, ' Maspotha', 59),
(1164, ' Kurunegala', 59),
(1165, ' Mallawapitiya', 59),
(1166, ' Mawathagama', 59),
(1167, ' Rideegama', 59),
(1168, ' Weerambugedara', 59),
(1169, ' Kuliyapitiya East', 59),
(1170, ' Kuliyapitiya West', 59),
(1171, ' Udubaddawa', 59),
(1172, ' Pannala', 59),
(1173, ' Narammala', 59),
(1174, ' Alawwa', 59),
(1175, ' Polgahawela', 59),
(1176, 'Kalpitiya', 60),
(1177, 'Vanathavilluwa', 60),
(1178, 'Karuwalagaswewa', 60),
(1179, ' Nawagattegama', 60),
(1180, ' Puttalam', 60),
(1181, ' Mundalama', 60),
(1182, ' Mahakumbukkadawala', 60),
(1183, ' Anamaduwa', 60),
(1184, ' Pallama', 60),
(1185, ' Arachchikattuwa', 60),
(1186, ' Chilaw', 60),
(1187, ' Madampe', 60),
(1188, ' Mahawewa', 60),
(1189, ' Nattandiya', 60),
(1190, ' Wennappuwa', 60),
(1191, ' Dankotuwa', 60),
(1192, 'Padaviya', 61),
(1193, 'Kebithigollewa', 61),
(1194, 'Medawachchiya', 61),
(1195, ' Mahavilachchiya', 61),
(1196, ' Nuwaragam Palatha Central', 61),
(1197, ' Rambewa', 61),
(1198, ' Kahatagasdigiliya', 61),
(1199, ' Horowpothana', 61),
(1200, ' Galenbindunuwewa', 61),
(1201, ' Mihinthale', 61),
(1202, ' Nuwaragam Palatha East', 61),
(1203, ' Nachchadoowa', 61),
(1204, ' Nochchiyagama', 61),
(1205, ' Rajanganaya', 61),
(1206, ' Thambuttegama', 61),
(1207, ' Thalawa', 61),
(1208, ' Thirappane', 61),
(1209, ' Kekirawa', 61),
(1210, ' Palugaswewa', 61),
(1211, ' Ipalogama', 61),
(1212, ' Galnewa', 61),
(1213, ' Palagala', 61),
(1214, 'Hingurakgoda', 62),
(1215, 'Medirigiriya', 62),
(1216, 'Lankapura', 62),
(1217, ' Welikanda', 62),
(1218, ' Dimbulagala', 62),
(1219, ' Thamankaduwa', 62),
(1220, ' Elahera', 62),
(1221, 'Mahiyanganaya', 63),
(1222, 'Rideemaliyadda', 63),
(1223, 'Meegahakivula', 63),
(1224, ' Kandaketiya', 63),
(1225, ' Soranathota', 63),
(1226, ' Passara', 63),
(1227, ' Lunugala', 63),
(1228, ' Badulla', 63),
(1229, ' Hali-Ela', 63),
(1230, ' Uva-Paranagama', 63),
(1231, ' Welimada', 63),
(1232, ' Bandarawela', 63),
(1233, ' Ella', 63),
(1234, ' Haputale', 63),
(1235, ' Haldummulla', 63),
(1236, 'Bibile', 64),
(1237, 'Madulla', 64),
(1238, 'Medagama', 64),
(1239, ' Siyambalanduwa', 64),
(1240, ' Moneragala', 64),
(1241, ' Badalkumbura', 64),
(1242, ' Wellawaya', 64),
(1243, ' Buttala', 64),
(1244, ' Katharagama', 64),
(1245, ' Thanamalvila', 64),
(1246, ' Sevanagala', 64),
(1247, 'Eheliyagoda', 65),
(1248, 'Kuruvita', 65),
(1249, 'Kiriella', 65),
(1250, ' Ratnapura', 65),
(1251, ' Imbulpe', 65),
(1252, ' Balangoda', 65),
(1253, ' Opanayaka', 65),
(1254, ' Pelmadulla', 65),
(1255, ' Elapatha', 65),
(1256, ' Ayagama', 65),
(1257, ' Kalawana', 65),
(1258, ' Nivithigala', 65),
(1259, ' Kahawatta', 65),
(1260, ' Godakawela', 65),
(1261, ' Weligepola', 65),
(1262, ' Embilipitiya', 65),
(1263, ' Kolonna', 65),
(1264, 'Rambukkana', 66),
(1265, 'Mawanella', 66),
(1266, 'Aranayaka', 66),
(1267, ' Kegalle', 66),
(1268, ' Galigamuwa', 66),
(1269, ' Warakapola', 66),
(1270, ' Ruwanwella', 66),
(1271, ' Bulathkohupitiya', 66),
(1272, ' Yatiyanthota', 66),
(1273, ' Dehiovita', 66),
(1274, ' Deraniyagala', 66),
(1275, ' Welioya', 54),
(1280, ' Gonapinuwala', 48),
(1283, ' Walasmulla', 50),
(1285, ' Karainagar', 51),
(1292, ' Kalmunai North Sub Office', 57),
(1293, ' Koralai Pattu Central', 56),
(1296, ' Rathgama', 48),
(1297, ' Madampagama', 48),
(1298, ' Waduramba', 48),
(1299, ' Kalthota', 65),
(1300, ' Norwood', 47),
(1301, 'Kothmale (West)', 47),
(1302, ' Nildandahinna', 47),
(1303, ' Thalawakale', 47),
(1304, 'Mathurata', 47);

-- --------------------------------------------------------

--
-- Table structure for table `provinces`
--

CREATE TABLE `provinces` (
  `id` int(11) NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provinces`
--

INSERT INTO `provinces` (`id`, `name`) VALUES
(63, 'Western'),
(64, 'Central'),
(65, 'Southern'),
(66, 'Northern'),
(67, 'Eastern'),
(68, 'North-Western'),
(69, 'North-Central'),
(70, 'Uva'),
(71, 'Sabaragamuwa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `districts`
--
ALTER TABLE `districts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `province_id` (`province_id`);

--
-- Indexes for table `divisions`
--
ALTER TABLE `divisions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `district_id` (`district_id`);

--
-- Indexes for table `provinces`
--
ALTER TABLE `provinces`
  ADD PRIMARY KEY (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `districts`
--
ALTER TABLE `districts`
  ADD CONSTRAINT `districts_ibfk_1` FOREIGN KEY (`province_id`) REFERENCES `provinces` (`id`);

--
-- Constraints for table `divisions`
--
ALTER TABLE `divisions`
  ADD CONSTRAINT `divisions_ibfk_1` FOREIGN KEY (`district_id`) REFERENCES `districts` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
