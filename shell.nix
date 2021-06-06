{ nixpkgs ? import (fetchTarball https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz) {} }:
with nixpkgs;

let
  customPython = python39.buildEnv.override {
    extraLibs = [
      python39Packages.notebook
      python39Packages.jupyter
      python39Packages.scipy
      python39Packages.numpy
      python39Packages.matplotlib
      # python39Packages.nbdime
    ];
  };
in
  pkgs.mkShell {
    buildInputs = [
      customPython
      git-lfs
    ];
  }
