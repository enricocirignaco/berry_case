#!/bin/bash
USER=enricocirignaco
IMAGENAME=stm32_build
IMAGETAG=develop
CONTAINER_NAME=setup_stm32_project

#build image from dockerfile locally
#docker build --pull --rm -t $IMAGENAME:$IMAGETAG .

#download image from dockerhub
docker pull $USER/$IMAGENAME:$IMAGETAG
#Run image in detached container
docker run -ti -d --name $CONTAINER_NAME --volume ${PWD}:/project $USER/$IMAGENAME:$IMAGETAG bash
#Update git repo and copy content to project directory
docker exec $CONTAINER_NAME /usr/bin/git -C ../stm32_build pull --recurse-submodules
docker exec $CONTAINER_NAME /usr/bin/cp -a ../stm32_build/vscode/. ./
docker exec $CONTAINER_NAME /usr/bin/cp -a ../stm32_build/VS-Code-STM32-IDE/ideScripts/ ./
docker exec $CONTAINER_NAME /usr/bin/cp -a ../stm32_build/scripts/project_update.sh ./
#Find out name of project 
PROJECTNAME=`docker exec $CONTAINER_NAME sh -c "/usr/bin/ls *.ioc | /usr/bin/sed -e 's/\..*$//'"`
#Rename workspace with project name
docker exec $CONTAINER_NAME /usr/bin/mv ./workspace.code-workspace ./$PROJECTNAME.code-workspace
#Compile vs code workspace with python3 script
docker exec $CONTAINER_NAME /usr/bin/python3 ./ideScripts/update.py
#backup generated tasks.json file and replace it with own tasks.json file
docker exec  $CONTAINER_NAME /usr/bin/mv .vscode/tasks.json .vscode/tasks.json.backup
docker exec  $CONTAINER_NAME /usr/bin/cp ../stm32_build/ressources/tasks_macos.json .vscode/tasks.json
#Stop and delete running container
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME