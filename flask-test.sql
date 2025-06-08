CREATE TABLE `files` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`filename` VARCHAR(255),
	`original_filename` VARCHAR(255),
	`file_path` VARCHAR(500),
	`file_size` INTEGER,
	`file_type` VARCHAR(255),
	`created_at` DATETIME,
	`updated_at` DATETIME,
	PRIMARY KEY(`id`)
);


CREATE TABLE `products` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`name` VARCHAR(255),
	`description` TEXT(65535),
	`code` VARCHAR(255),
	`status` VARCHAR(255),
	`created_at` DATETIME,
	`updated_at` DATETIME,
	PRIMARY KEY(`id`)
);


CREATE TABLE `users` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`username` VARCHAR(255) UNIQUE,
	`email` VARCHAR(255) UNIQUE,
	`password_hash` VARCHAR(255),
	`is_admin` BOOLEAN,
	`created_at` DATETIME,
	`updated_at` DATETIME,
	PRIMARY KEY(`id`)
);


CREATE INDEX `users_index_0`
ON `users` (`username`, `email`);
CREATE TABLE `versions` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`version_number` VARCHAR(255),
	`description` TEXT(65535),
	`release_notes` TEXT(65535),
	`status` VARCHAR(255),
	`created_at` DATETIME,
	`updated_at` DATETIME,
	`released_at` DATETIME,
	`product_id` INTEGER,
	`author_id` INTEGER,
	PRIMARY KEY(`id`)
);


