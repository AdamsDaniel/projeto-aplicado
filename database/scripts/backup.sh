#!/bin/sh
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/backups"
MYSQL_HOST="db"   # Nome do serviço do MySQL definido no docker-compose.yml
MYSQL_USER="root"
MYSQL_PASSWORD="password"
DATABASE="risk_management"

mkdir -p $BACKUP_DIR

mysqldump -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $DATABASE | gzip > $BACKUP_DIR/backup_$TIMESTAMP.sql.gz

# Remove backups com mais de 7 dias
find $BACKUP_DIR -name "*.sql.gz" -mtime +7 -exec rm {} \;

echo "$(date) - Backup realizado: backup_$TIMESTAMP.sql.gz" >> $BACKUP_DIR/backup.log
