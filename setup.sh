#!/usr/bin/env bash

asdf plugin add awscli
asdf plugin-add terraform https://github.com/asdf-community/asdf-hashicorp.git
asdf install

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt install git-lfs pigz # or brew install pigz git-lfs

git lfs install
git submodule update --init --recursive
