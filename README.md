# EOSC-Future science projects - Reproducible analyses

EOSC-Future funds two differen kinds of science projects:
1. Dark Matter 
2. Extreme Universe

You can find out more about them [here](https://escape2020.pages.in2p3.fr/virtual-environment/home/). 

The VRE aims at developing:
- an infrastructure where to run an end-to-end analysis in one place
- a solution to preserve the analysis steps in case of re-use 
- an interdisciplinary open science example from a bottom-up effort

If your project doesn't belong to the above categories, you can still use the VRE to run your analysis. Add your project within a new folder and follow the instructions below.

This repo contains the code and the analysis steps to reproduce the analyses that the scientists have decided to make public. 
In order to re-run an analysis stored here, follow the following steps:

- if you didn't already, create a IAM account following [this](https://vre-hub.github.io/docs/rucio.html). It will authenticate you to the notebook service, Rucio and Reana. 
- log into the [VRE Jupyterhub notebook service](https://jhub-vre.cern.ch/) by using your IAM credentials.
- obtain a Reana token via the [VRE-Reana UI](https://reana-vre.cern.ch/) interface. 
- open a terminal on Jupyterhub and add your reana server and reana secrets via the `reana-client` following [this](https://vre-hub.github.io/docs/reana.html). 
- have a look how to create a reana file and how to run it by checking the `yaml` and the `bash` files of the, for example, [ATLAS Dark Matter reinterpretation](https://github.com/vre-hub/science-projects/tree/main/dark_matter/ATLAS-dilepton) science project.
- check the status of your workflow run on the Reana UI and get the outputted results. 

# License anc citation

This repository is a compilation of different projects, each one with its own license. The same applies to its citation. Please check the license and citation of each project before using it.
