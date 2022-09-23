ALTER TABLE `purchases` ADD 
   CONSTRAINT `fk_purchases_posts1` 
      FOREIGN KEY (`post_id`)
      REFERENCES `posts` (`id`)
      ON DELETE CASCADE;
   