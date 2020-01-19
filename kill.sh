#!/bin/bash
MYSQL="mysql -h10.66.111.6 -upaydayloan -pYZ3Td8r3r8MEPl2pRiPhXf4VgCumjvPd_1470816485"
for pid in `$MYSQL -B -e  "show processlist " |grep "SELECT COUNT(*) FROM `pay_log` LEFT JOIN `apply` ON apply_id = pay_log_target_id" |awk '{print $1}' `
do
    echo $pid
   $MYSQL -e " kill $pid"
done
