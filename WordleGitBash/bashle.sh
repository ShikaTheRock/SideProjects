#!/bin/bash

#Buscar si el .scrtsnt(.txt) esta creado en $HOME, /usr/bin/, /etc/

if [ -f $HOME/.scrtsnt ]; then
    rm -rf $HOME/.scrtsnt

elif [ -f $XDG_CONFIG_HOME/.scrtsnt ]; then
    rm -rf $XDG_CONFIG_HOME/.scrtsnt

elif [ -f $XDG_CACHE_HOME/.scrtsnt ]; then
    rm -rf $XDG_CACHE_HOME/.scrtsnt

elif [ -f $HOME/.local/share/.scrtsnt ]; then
    rm -rf $HOME/.local/share/.scrtsnt

else 
    dest=($RANDOM%4)
    if [ $dest -eq 1 ]; then
        touch $HOME/.scrtsnt
    
    elif [ $dest -eq 2 ]; then
        touch $XDG_CONFIG_HOME/.scrtsnt
    
    elif [ $dest -eq 3 ]; then
        touch $XDG_CACHE_HOME/.scrtsnt
    
    elif [ $dest -eq 4 ]; then
        touch $HOME/.local/share/.scrtsnt
    
    fi
fi

