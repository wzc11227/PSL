create table IF NOT EXISTS `bag` (
  `ID` smallint(6) NOT NULL auto_increment,
  `User` int(11) NOT NULL,
  `Player` int(11) NOT NULL,
  primary key(`id`)
) default charset = utf8;