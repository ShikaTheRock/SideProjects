#!/bin/bash

echo "BIENVENIDO A BASHLE! 

Fecheando la palabra del dia..."

#Buscar si el .scrtsnt(.txt) esta creado en los directorios, si no esta, que lo cree

if [ -f $HOME/.scrtsnt ]; then
    rm -rf $HOME/.scrtsnt

elif [ -f $XDG_CONFIG_HOME/.scrtsnt ]; then
    rm -rf $XDG_CONFIG_HOME/.scrtsnt

elif [ -f $XDG_CACHE_HOME/.scrtsnt ]; then
    rm -rf $XDG_CACHE_HOME/.scrtsnt

elif [ -f $HOME/.local/share/.scrtsnt ]; then
    rm -rf $HOME/.local/share/.scrtsnt
fi
let dest=($RANDOM%4)
echo "DEBUG: $dest"
if [ $dest -eq 0 ]; then
    touch $HOME/.scrtsnt
    ub=$HOME/.scrtsnt
    wget -q https://raw.githubusercontent.com/ShikaTheRock/SideProjects/refs/heads/main/WordleGitBash/scrt
    cat scrt > $HOME/.scrtsnt
    rm scrt

elif [ $dest -eq 1 ]; then
    touch $XDG_CONFIG_HOME/.scrtsnt
    ub=$XDG_CONFIG_HOME/.scrtsnt
    wget -q https://raw.githubusercontent.com/ShikaTheRock/SideProjects/refs/heads/main/WordleGitBash/scrt
    cat scrt > $XDG_CONFIG_HOME/.scrtsnt
    rm scrt

elif [ $dest -eq 2 ]; then
    touch $XDG_CACHE_HOME/.scrtsnt
    ub=$XDG_CACHE_HOME/.scrtsnt
    wget -q https://raw.githubusercontent.com/ShikaTheRock/SideProjects/refs/heads/main/WordleGitBash/scrt
    cat scrt > $XDG_CACHE_HOME/.scrtsnt
    rm scrt

elif [ $dest -eq 3 ]; then
    touch $HOME/.local/share/.scrtsnt
    ub=$HOME/.local/share/.scrtsnt
    wget -q https://raw.githubusercontent.com/ShikaTheRock/SideProjects/refs/heads/main/WordleGitBash/scrt
    cat scrt > $HOME/.local/share/.scrtsnt
    rm scrt
fi

echo "DEBUG $ub"



