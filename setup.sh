#!/bin/bash

echo
echo "Welcome to the bprimekit setup script!"
echo

echo "Set up JetToolBox"
git clone https://github.com/cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X_v1
echo

echo "Set up Muon user code"
git clone https://github.com/ETHZ/sixie-Muon-MuonAnalysisTools.git UserCode/sixie/Muon/MuonAnalysisTools
echo

echo "Done with setup script! You still need to build!"
echo
