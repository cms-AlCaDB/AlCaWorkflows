from alcaval_steps import *
workflows = Matrix()

# CRUZET 2021
# Following workflows share same cmsDriver configuration
workflows[1.1] = ['CRUZET2022', ['Cosmics2021', 'HLT_CRUZET2021', 'RECO_CRUZET2021', 'HARVEST_CRUZET2021']]
workflows[1.2] = ['CRUZET2022', ['Cosmics2021', 'RECO_CRUZET2021', 'HARVEST_CRUZET2021']]
workflows[1.3] = ['CRUZET2022', ['ExpressCosmics2021', 'HLT_CRUZET2021', 'RECO_CRUZET2021', 'HARVEST_CRUZET2021']]
workflows[1.4] = ['CRUZET2022', ['ExpressCosmics2021', 'RECO_CRUZET2021', 'HARVEST_CRUZET2021']]
#-----------------------------------------------------------------------------------------------------------------

# PBT 2021
# Following workflows share same cmsDriver configuration
workflows[2.1] = ['PBT2021', ['MinimumBias2021', 'HLT_PBT2021', 'RECO_PBT2021', 'HARVEST_PBT2021']]
workflows[2.2] = ['PBT2021', ['MinimumBias2021', 'RECOPE_PBT21', 'HARVEST_PBT2021']]
workflows[2.3] = ['PBT2021', ['ZeroBias2021', 'HLT_PBT2021', 'RECO_PBT2021', 'HARVEST_PBT2021']]
workflows[2.4] = ['PBT2021', ['ZeroBias2021', 'RECOPE_PBT21', 'HARVEST_PBT2021']]
workflows[2.5] = ['PBT2021', ['HLTPhysics2021', 'HLT_PBT2021', 'RECO_PBT2021', 'HARVEST_PBT2021']]
workflows[2.6] = ['PBT2021', ['HLTPhysics2021', 'RECOPE_PBT21', 'HARVEST_PBT2021']]
#-----------------------------------------------------------------------------------------------------------------

# MWGR 2022
# Following workflows share same cmsDriver configuration
workflows[3.1] = ['MWGR2022', ['HcalNZS2022', 'HLT_MWGR2022', 'RECO_MWGR2022', 'HARVEST_MWGR2022']]
workflows[3.2] = ['MWGR2022', ['HcalNZS2022', 'RECO_MWGR2022', 'HARVEST_MWGR2022']]
#-----------------------------------------------------------------------------------------------------------------

# CRAFT 2022
# Following workflows share same cmsDriver configuration
workflows[4.1] = ['CRAFT2022', ['HLTPhysics2022', 'HLT_CRAFT22', 'RECO_CRAFT2022', 'HARVEST_CRAFT22']]
workflows[4.2] = ['CRAFT2022', ['HLTPhysics2022', 'RECO_CRAFT2022', 'HARVEST_CRAFT22']]
workflows[4.3] = ['', ['Cosmics2022', 'HLT_CRAFT22', 'RECO_CRAFT2022', 'HARVEST_CRAFT22']]
workflows[4.4] = ['', ['Cosmics2022', 'RECO_CRAFT2022', 'HARVEST_CRAFT22']]
workflows[4.5] = ['', ['Cosmics2022', 'HLT_CRAFT22_v2', 'RECO_CRAFT2022_v2', 'HARVEST_CRAFT22_v2']]
workflows[4.6] = ['', ['Cosmics2022', 'RECO_CRAFT2022_v2', 'HARVEST_CRAFT22_v2']]

workflows[4.11] = ['', ['Cosmics2022_v2', 'HLT_CRAFT22_v2', 'RECO_CRAFT2022_v2', 'HARVEST_CRAFT22_v2']]
workflows[4.12] = ['', ['Cosmics2022_v2', 'RECO_CRAFT2022_v2', 'HARVEST_CRAFT22_v2']]
#-----------------------------------------------------------------------------------------------------------------


# MRH Test for Express WF
workflows[5.1] = ['MRHTest22', ['MinimumBias2021', 'RECO_MRH_Test', 'ALCARECO_MRH_Test']]


# Collision 2022

## Dataset v1: 352567
workflows[6.1] = ['', ['RunHLTPhysics2022A', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.2] = ['', ['RunHLTPhysics2022A', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.3] = ['', ['RunJetHT2022A', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.4] = ['', ['RunJetHT2022A', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.5] = ['', ['RunZeroBias2022A', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.6] = ['', ['RunZeroBias2022A', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
#-----------------------------------------------------------------------------------------------------------------

## Dataset v2: 353060
# Following workflows share same cmsDriver configuration
workflows[6.7] = ['', ['RunHLTPhysics2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.8] = ['', ['RunHLTPhysics2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.11] = ['', ['RunZeroBias2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.12] = ['', ['RunZeroBias2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.13] = ['', ['RunMinimumBias2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.14] = ['', ['RunMinimumBias2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.15] = ['', ['RunEGamma2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.16] = ['', ['RunEGamma2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.17] = ['', ['RunJetHT2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.18] = ['', ['RunJetHT2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.21] = ['', ['RunMET2022A_v2', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.22] = ['', ['RunMET2022A_v2', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]

workflows[6.23] = ['', ['RunJetHT2022B_v1', 'HLT_Collision22_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
workflows[6.24] = ['', ['RunJetHT2022B_v1', 'RECO_Collision22_v1', 'HARVEST_Collision22_v1']]
#-----------------------------------------------------------------------------------------------------------------

## Dataset v3: 355558 
# Following workflows share same cmsDriver configuration
workflows[6.25] = ['', ['RunZeroBias2022B_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.26] = ['', ['RunZeroBias2022B_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]

workflows[6.27] = ['', ['RunHLTPhysics2022B_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.28] = ['', ['RunHLTPhysics2022B_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]

workflows[6.31] = ['', ['RunEGamma2022B_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.32] = ['', ['RunEGamma2022B_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]

## Dataset 2022C: 356005
workflows[6.33] = ['', ['RunJetHT2022C_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.34] = ['', ['RunJetHT2022C_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]

workflows[6.35] = ['', ['RunEGamma2022C_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.36] = ['', ['RunEGamma2022C_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]

#-----------------------------------------------------------------------------------------------------------------
# HLT:Custom menu

workflows[6.37] = ['', ['RunEGamma2022C_v1', 'HLT_Collision22_v3', 'RECO_Collision22_v3', 'HARVEST_Collision22_v2']]
workflows[6.39] = ['', ['RunHLTPhysics22D_v1', 'HLT_Collision22_v3', 'RECO_Collision22_v3', 'HARVEST_Collision22_v2']]
workflows[6.41] = ['', ['RunMuon22D_v1', 'HLT_Collision22_v3', 'RECO_Collision22_v3', 'HARVEST_Collision22_v2']]
workflows[6.43] = ['', ['RunJetMET22D_v1', 'HLT_Collision22_v3', 'RECO_Collision22_v3', 'HARVEST_Collision22_v2']]
#-----------------------------------------------------------------------------------------------------------------
# To be used in HCAL FTV: CMSALCA-182
workflows[6.44] = ['', ['RunHLTPhysics22D_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.46] = ['', ['RunMuon22D_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
workflows[6.48] = ['', ['RunJetMET22D_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
#-----------------------------------------------------------------------------------------------------------------
# With 'reHLT' process in RECO step for HLT workflow: 28th Sep 22
workflows[6.51] = ['', ['RunEGamma2022C_v1', 'HLT_Collision22_v2', 'RECO_Collision22_v3', 'HARVEST_Collision22_v2']]
workflows[6.52] = ['', ['RunEGamma2022C_v1', 'RECO_Collision22_v2', 'HARVEST_Collision22_v2']]
