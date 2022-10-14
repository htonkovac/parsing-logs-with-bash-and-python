#!/bin/bash
cat apache_logs | awk '{print $9}' | sort | uniq -c
