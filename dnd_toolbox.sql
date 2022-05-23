-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dnd_toolbox_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dnd_toolbox_db` ;

-- -----------------------------------------------------
-- Schema dnd_toolbox_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dnd_toolbox_db` DEFAULT CHARACTER SET utf8 ;
USE `dnd_toolbox_db` ;

-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `pw_hash` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`characters` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `char_class` VARCHAR(255) NULL,
  `users_id` INT NOT NULL,
  `race` VARCHAR(45) NULL,
  `class` VARCHAR(45) NULL,
  `strength` INT NULL,
  `constitution` INT NULL,
  `dexterity` INT NULL,
  `intelligence` INT NULL,
  `wisdom` INT NULL,
  `charisma` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_characters_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_characters_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `dnd_toolbox_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`masters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`masters` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_masters_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_masters_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dnd_toolbox_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`campaigns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`campaigns` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `notes` TEXT NULL,
  `master_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_campaigns_masters1_idx` (`master_id` ASC) VISIBLE,
  CONSTRAINT `fk_campaigns_masters1`
    FOREIGN KEY (`master_id`)
    REFERENCES `dnd_toolbox_db`.`masters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`users_has_campaigns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`users_has_campaigns` (
  `user_id` INT NOT NULL,
  `campaign_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `campaign_id`),
  INDEX `fk_users_has_campaigns_campaigns1_idx` (`campaign_id` ASC) VISIBLE,
  INDEX `fk_users_has_campaigns_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_campaigns_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dnd_toolbox_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_campaigns_campaigns1`
    FOREIGN KEY (`campaign_id`)
    REFERENCES `dnd_toolbox_db`.`campaigns` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dnd_toolbox_db`.`campaigns_has_characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dnd_toolbox_db`.`campaigns_has_characters` (
  `campaign_id` INT NOT NULL,
  `character_id` INT NOT NULL,
  PRIMARY KEY (`campaign_id`, `character_id`),
  INDEX `fk_campaigns_has_characters_characters1_idx` (`character_id` ASC) VISIBLE,
  INDEX `fk_campaigns_has_characters_campaigns1_idx` (`campaign_id` ASC) VISIBLE,
  CONSTRAINT `fk_campaigns_has_characters_campaigns1`
    FOREIGN KEY (`campaign_id`)
    REFERENCES `dnd_toolbox_db`.`campaigns` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_campaigns_has_characters_characters1`
    FOREIGN KEY (`character_id`)
    REFERENCES `dnd_toolbox_db`.`characters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
