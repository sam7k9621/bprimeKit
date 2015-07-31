from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'CRAB_JOB_NAME'
config.General.workArea = 'bprimekit_crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BPK_PYTHONFILE'
config.JobType.inputFiles = [
    '../dataEIDMVA' ] 

config.Data.inputDataset = 'CRAB_DATA_SET'

config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_b2g/BprimeKit_Ntuples' 
#config.Data.publication = True
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = 'T2_CERN_CH'