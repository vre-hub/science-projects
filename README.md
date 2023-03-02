# EOSC-Future science projects - Reproducible analyses

EOSC-Future funds two differen kinds of science projects:
1. Dark Matter 
2. Extreme Universe

You can find out more about them [here](https://escape2020.pages.in2p3.fr/virtual-environment/home/). 

The VRE aims at developing:
- an infrastructure where to run an end-to-end analysis in one place
- a solution to preserve the analysis steps in case of re-use 
- an interdisciplinary open science example from a bottom-up effort

This repo contains the code and the analysis steps to reproduce the analyses that the scientists have decided to make public. 
In order to re-run an analysis stored here, follow the following steps:

- if you didn't already, create a IAM account following [this](https://datalake-rucio.docs.cern.ch/). It will authenticate you to the notebook service, Rucio and Reana. 
- log into the [Jupyterhub notebook](https://escape-notebook.cern.ch/) and into the VRE's [Reana UI](ADDDDDD LLIIINKKKKK TO VRE REANA) interface by using your IAM credentials. 
- open a terminal on Jupyterhub and add your reana server and reana secrets via the `reana-client` following [this](https://datalake-rucio.docs.cern.ch/reana/). 
- clone the repo you are interested in. 
- run the `reana.sh` script 
- check the status of your workflow run on the Reana UI and get the outputted results. 
