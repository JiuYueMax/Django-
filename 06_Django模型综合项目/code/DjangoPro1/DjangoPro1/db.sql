
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for author_author
-- ----------------------------
DROP TABLE IF EXISTS `author_author`;
CREATE TABLE `author_author`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `gender` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of author_author
-- ----------------------------
INSERT INTO `author_author` VALUES (1, '吴', '承恩', 'wuchengen@gudai.comww', 1);
INSERT INTO `author_author` VALUES (2, '罗', '贯中', 'luoguanzhong@gudai.com', 1);
INSERT INTO `author_author` VALUES (3, '曹', '雪芹', 'caoxueqin@gudai.com', 1);
INSERT INTO `author_author` VALUES (4, '施', '耐庵', 'shinaian@gudai.com', 1);

DROP TABLE IF EXISTS `publisher_publisher`;
CREATE TABLE `publisher_publisher`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `city` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `state_province` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `country` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `website` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of publisher_publisher
-- ----------------------------
INSERT INTO `publisher_publisher` VALUES (1, '北京出版社', '北京西城区', '北京', '北京', '中国', 'http://www.baidu.com');
INSERT INTO `publisher_publisher` VALUES (2, '清华出版社', '北京市海淀区', '北京', '北京', '中国', 'https://www.douyin.com/');
INSERT INTO `publisher_publisher` VALUES (3, '人民文学出版社', '北京市东城区朝阳门内大街166号', '北京', '北京', '中国', 'http://book.cnpubg.com/');
INSERT INTO `publisher_publisher` VALUES (4, '‌‌人民邮电出版社', '北京市丰台区成寿寺路11号邮电出版大厦', '北京', '北京', '中国', 'https://www.ptpress.com.cn/');


DROP TABLE IF EXISTS `book_book`;
CREATE TABLE `book_book`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `publish_date` date NOT NULL,
  `author_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `book_book_author_id_40846805_fk_author_author_id`(`author_id`) USING BTREE,
  CONSTRAINT `book_book_author_id_40846805_fk_author_author_id` FOREIGN KEY (`author_id`) REFERENCES `author_author` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book_book
-- ----------------------------
INSERT INTO `book_book` VALUES (1, '《红楼梦》', '2024-09-08', 3);
INSERT INTO `book_book` VALUES (2, '《脂砚斋重评石头记》', '2024-09-07', 3);
INSERT INTO `book_book` VALUES (3, '《三国演义》', '2024-09-08', 2);
INSERT INTO `book_book` VALUES (4, '《隋唐两朝志传》', '2024-09-08', 2);
INSERT INTO `book_book` VALUES (5, '《三国志通俗演义》', '2024-09-08', 1);
INSERT INTO `book_book` VALUES (6, '《西游记》', '2024-09-08', 1);
INSERT INTO `book_book` VALUES (7, '《花草新编》', '2024-09-08', 1);
INSERT INTO `book_book` VALUES (8, '《射阳先生存稿》', '2024-09-08', 1);
INSERT INTO `book_book` VALUES (9, '《水浒传》', '2024-09-08', 4);

DROP TABLE IF EXISTS `book_book_publishers`;
CREATE TABLE `book_book_publishers`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `book_id` bigint(20) NOT NULL,
  `publisher_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `book_book_publishers_book_id_publisher_id_441b0eee_uniq`(`book_id`, `publisher_id`) USING BTREE,
  INDEX `book_book_publishers_publisher_id_b2dc50d0_fk_publisher`(`publisher_id`) USING BTREE,
  CONSTRAINT `book_book_publishers_book_id_834922fa_fk_book_book_id` FOREIGN KEY (`book_id`) REFERENCES `book_book` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `book_book_publishers_publisher_id_b2dc50d0_fk_publisher` FOREIGN KEY (`publisher_id`) REFERENCES `publisher_publisher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of book_book_publishers
-- ----------------------------
INSERT INTO `book_book_publishers` VALUES (1, 1, 2);
INSERT INTO `book_book_publishers` VALUES (2, 1, 3);
INSERT INTO `book_book_publishers` VALUES (3, 2, 1);
INSERT INTO `book_book_publishers` VALUES (4, 2, 2);
INSERT INTO `book_book_publishers` VALUES (5, 3, 1);
INSERT INTO `book_book_publishers` VALUES (6, 3, 2);
INSERT INTO `book_book_publishers` VALUES (7, 3, 3);
INSERT INTO `book_book_publishers` VALUES (8, 4, 3);
INSERT INTO `book_book_publishers` VALUES (9, 4, 4);
INSERT INTO `book_book_publishers` VALUES (10, 5, 1);
INSERT INTO `book_book_publishers` VALUES (11, 5, 2);
INSERT INTO `book_book_publishers` VALUES (12, 5, 3);
INSERT INTO `book_book_publishers` VALUES (13, 5, 4);
INSERT INTO `book_book_publishers` VALUES (14, 6, 2);
INSERT INTO `book_book_publishers` VALUES (15, 6, 3);
INSERT INTO `book_book_publishers` VALUES (16, 7, 4);
INSERT INTO `book_book_publishers` VALUES (17, 8, 2);
INSERT INTO `book_book_publishers` VALUES (18, 8, 3);
INSERT INTO `book_book_publishers` VALUES (19, 8, 4);
INSERT INTO `book_book_publishers` VALUES (20, 9, 1);
INSERT INTO `book_book_publishers` VALUES (21, 9, 2);
INSERT INTO `book_book_publishers` VALUES (22, 9, 3);
INSERT INTO `book_book_publishers` VALUES (23, 9, 4);