# 0x0D. SQL - Introduction

## Comments for your SQL file:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS:
sudo apt update
sudo apt install mysql-server
mysql --version

## Connect to your MySQL server:
sudo mysql
