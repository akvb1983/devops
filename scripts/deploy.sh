#!/bin/bash

APP_DIR=/opt/employee-portal

mkdir -p $APP_DIR

echo "Deployment completed: $(date)" \
>> $APP_DIR/deploy.log
