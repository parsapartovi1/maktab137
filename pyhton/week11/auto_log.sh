#!/bin/bash


LOG_DIR="/var/log"                     # dir
BACKUP_DIR="/var/log/backups"          # backup 
ARCHIVE_DIR="/var/log/archives"        # archive destination
REPORT_DIR="/var/log/logmaster"        # report dir
PYTHON_TOOL="/usr/bin/python3 /path/to/logmaster.py"  # adjust path to your tool


mkdir -p "$BACKUP_DIR" "$ARCHIVE_DIR" "$REPORT_DIR"


DATE=$(date +"%Y-%m-%d")
BACKUP_FILE="$BACKUP_DIR/logs_$DATE.tar.gz"
tar -czf "$BACKUP_FILE" "$LOG_DIR"/*.log 2>/dev/null
echo "Backup created: $BACKUP_FILE"


find "$LOG_DIR" -name "*.log" -type f -mtime +7 -exec mv {} "$ARCHIVE_DIR" \;
echo "Archived logs older than 7 days to $ARCHIVE_DIR"

$PYTHON_TOOL scan --file "$LOG_DIR/syslog" --errors --count > "$REPORT_DIR/report.txt" 2>&1
echo "Logmaster report saved to $REPORT_DIR/report.txt"


USAGE=$(df "$LOG_DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$USAGE" -gt 90 ]; then
    echo "WARNING: Low disk space ($USAGE% used)"
else
    echo "Disk usage OK ($USAGE% used)"
fi
