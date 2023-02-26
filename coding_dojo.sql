CREATE  TABLE `holamundo`.`pie` (

  `id` INT NOT NULL AUTO_INCREMENT ,

  `name` VARCHAR(45) NOT NULL ,

  `filling` VARCHAR(45) NOT NULL ,

  `crust` VARCHAR(45) NOT NULL ,

  `votes` INT NOT NULL ,

  `user_id` INT NOT NULL ,

  PRIMARY KEY (`id`) ,

  INDEX `id` (`user_id` ASC) ,

  CONSTRAINT `id`

    FOREIGN KEY (`user_id` )

    REFERENCES `holamundo`.`users` (`id` )

    ON DELETE NO ACTION

    ON UPDATE NO ACTION);