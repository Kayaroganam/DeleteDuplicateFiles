#!/bin/bash

read -p "Enter folder Name: " folder
cd "$folder"
du -sB K * > ../first
cd $folder
du -sB K * > ../../second
cd $folder
du -sB K * > ../../../third
