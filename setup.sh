#!/usr/bin/env bash

set -e

INSTALL_TOOLING="${INSTALL_TOOLING:=false}"

if [[ $INSTALL_TOOLING == 'true' ]]; then
    asdf plugin add awscli
    asdf plugin-add terraform https://github.com/asdf-community/asdf-hashicorp.git
    asdf install
fi

if [[ $OSTYPE == 'darwin'* ]]; then
    brew install pigz git-lfs
elif [[ $OSTYPE == 'linux-gnu'* ]]; then
    # Assuming debian-based
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    sudo apt install git-lfs pigz
else
    >&2 echo "OS not known" && exit 1
fi

git lfs install
git submodule update --init --recursive
