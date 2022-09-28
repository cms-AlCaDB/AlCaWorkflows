from __future__ import absolute_import
from Configuration.PyReleaseValidation.MatrixUtil import *

steps = Steps()

## Step1
# CRUZET 2021
steps['ExpressCosmics2021']={'INPUT':InputInfo(dataSet='/ExpressCosmics/Commissioning2021-Express-v1/FEVT',ls={345755: [[1, 990]]})}
steps['Cosmics2021']={'INPUT':InputInfo(dataSet='/Cosmics/Commissioning2021-v1/RAW',ls={344518: [[1, 1892]]})}

# PBT 2021
steps['MinimumBias2021']={'INPUT':InputInfo(dataSet='/MinimumBias/Commissioning2021-v1/RAW',ls={346512: [[1,400]]})}
steps['ZeroBias2021']={'INPUT':InputInfo(dataSet='/ZeroBias/Commissioning2021-v1/RAW', ls={346512: [[1,400]]})}
steps['HLTPhysics2021']={'INPUT':InputInfo(dataSet='/HLTPhysics/Commissioning2021-v1/RAW',ls={346512: [[1,400]]})}

# MWGR 2022
steps['HcalNZS2022']={'INPUT':InputInfo(dataSet='/HcalNZS/Commissioning2022-v1/RAW',ls={347807: [[1, 838]]})}

# CRAFT 2022
steps['HLTPhysics2022']={'INPUT':InputInfo(dataSet='/HLTPhysics/Commissioning2022-v1/RAW',ls={348338: [[1,180]]})}
steps['Cosmics2022']={'INPUT':InputInfo(dataSet='/Cosmics/Commissioning2022-v1/RAW',ls={349840: [[1,2000]]})}
steps['Cosmics2022_v2']={'INPUT':InputInfo(dataSet='/Cosmics/Commissioning2022-v1/RAW',ls={348773: [[1,3222]]})}

# Step2 HLT: for run3
step2Defaults = {'--process':'reHLT',
                      '-s':'L1REPACK,HLT',
                      '--conditions':'auto:run3_data',
                      '--data':'',
                      '--eventcontent': 'FEVTDEBUGHLT',
                      '--datatier': 'FEVTDEBUGHLT',
                      '--era' : 'Run3',
                      '--scenario' : 'pp'
                      }

steps['HLT_PBT2021'] = merge( [ {'-s':'L1REPACK,HLT:GRun',},
                                {'--procModifiers'  : 'siPixelQualityRawToDigi'},
                                {'--customise'      : 'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3,RecoLocalCalo/Configuration/customiseHBHEreco.hbheUseM0FullRangePhase1'},
                                step2Defaults ] )

# Cosmics
steps['HLT_CRUZET2021'] = merge( [ {'--scenario': 'cosmics', '--datatier': 'FEVTDEBUGHLT', 
                                    '--eventcontent': 'FEVTDEBUG', '--magField': '0T'}, step2Defaults] )
steps['HLT_MWGR2022'] = merge( [ steps['HLT_CRUZET2021'] ] )
steps['HLT_CRAFT22'] = merge( [ {'--scenario': 'cosmics', '--datatier': 'FEVTDEBUGHLT',
				'--eventcontent': 'FEVTDEBUG',
				'--customise': 'L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML'
				}, step2Defaults] )
steps['HLT_CRAFT22_v2'] = merge( [ {'--scenario': 'cosmics', '--datatier': 'FEVTDEBUGHLT',
				'--eventcontent': 'FEVTDEBUG',
				'-s': 'L1REPACK:uGT,HLT',
				'--customise': 'L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML'
				}, step2Defaults] )

# Step3 RECO: for run3
step3Defaults = {
                  '-s'            : 'RAW2DIGI,L1Reco,RECO,EI,PAT,DQM',
                  '--conditions'  : 'auto:run3_data',
                  '--no_exec'     : '',
                  '--data'        : '',
                  '--datatier'    : 'RECO,DQMIO',
                  '--eventcontent': 'RECO,DQM',
                  '--era'         : 'Run3',
                  '--process'     : 'reRECO',
                  '--scenario'    : 'pp'
                  }

steps['RECO_PBT2021']=merge([
                            {'-s' : 'RAW2DIGI,L1Reco,RECO,EI,PAT,DQM:DQMOffline+offlineValidationHLTSource'},
                            {'--procModifiers'  : 'siPixelQualityRawToDigi'},
                            {'--customise':'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3,RecoLocalCalo/Configuration/customiseHBHEreco.hbheUseM0FullRangePhase1'},
                            step3Defaults])

steps['RECOPE_PBT21']=merge([
			    {'-s'            : 'RAW2DIGI,L1Reco,RECO,DQM'},
                            {'--procModifiers'  : 'siPixelQualityRawToDigi'},
                            {'--customise':'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3,RecoLocalCalo/Configuration/customiseHBHEreco.hbheUseM0FullRangePhase1'},
                            step3Defaults])

# Cosmics
steps['RECO_CRUZET2021']=merge([{'--scenario':'cosmics',
                                '-s'         : 'RAW2DIGI,L1Reco,RECO,DQM',
                                '--magField' : '0T',
                                },
                                step3Defaults]
                              )
steps['RECO_MWGR2022']=merge([ steps['RECO_CRUZET2021'] ])
steps['RECO_CRAFT2022']=merge([{'--scenario':'cosmics', '-s' : 'RAW2DIGI,L1Reco,RECO,DQM'},step3Defaults])
steps['RECO_CRAFT2022_v2']=merge([{'--scenario':'cosmics',
				'-s' : 'RAW2DIGI,L1Reco,RECO,DQM',
				'--customise': 'Configuration/DataProcessing/RecoTLR.customiseCosmicData',
				},step3Defaults])
steps['RECO_MRH_Test']=merge([{'-s': 'RAW2DIGI,L1Reco,RECO,ALCAPRODUCER:SiStripCalMinBiasAAG,ENDJOB',
                                '--conditions'  : '123X_dataRun3_Express_MRH_harvest_test',
                                '--datatier' : 'ALCARECO', '--eventcontent': 'ALCARECO',
                                '--process'  : 'RECO',
                                '--customise': 'Configuration/DataProcessing/RecoTLR.customiseExpress',
                                '--scenario' : 'pp',
                                '--era'      : 'Run3',
                                '--no_exec'  : '',
                                '--data'     : ''
                                }])

steps['ALCARECO_MRH_Test']=merge([{'-s': 'ALCAOUTPUT:SiStripCalMinBiasAAG,ALCA:PromptCalibProdSiStripGainsAAG',
                                    '--conditions'  : '123X_dataRun3_Express_MRH_harvest_test',
                                    '--datatier': 'ALCARECO',
                                    '--eventcontent': 'ALCARECO',
                                    '--process'  : 'reRECO',
                                    '--customise': 'Configuration/DataProcessing/RecoTLR.customiseExpress',
                                    '--scenario' : 'pp',
                                    '--era'      : 'Run3',
                                    '--no_exec'  : '',
                                    '--data'     : '',
                                    '--triggerResultsProcess': 'RECO'
                                    }])

# Step4 HARVESTING
steps['HARVESTDefault']={'-s':'HARVESTING:dqmHarvesting',
                   '--conditions':'auto:run3_data',
                   '--data'     :'',
                   '--no_exec'  :'',
                   '--filetype' :'DQM',
                   '--scenario' :'pp',
                   '--era'      :'Run3'
                   }

steps['HARVEST_PBT2021'] = merge([ steps['HARVESTDefault'] ])

# Cosmics
steps['HARVEST_CRUZET2021'] = merge([ {'--scenario':'cosmics'}, steps['HARVESTDefault'] ])
steps['HARVEST_MWGR2022'] = merge([ {'--scenario':'cosmics'}, steps['HARVESTDefault'] ])
steps['HARVEST_CRAFT22'] = merge([ {'--scenario':'cosmics'}, steps['HARVESTDefault'] ])
steps['HARVEST_CRAFT22_v2'] = merge([ {'--scenario':'cosmics',
				'--customise': 'Configuration/DataProcessing/RecoTLR.customiseCosmicData',
				}, steps['HARVESTDefault'] ])

# Collision 2022A
steps['RunHLTPhysics2022A']={'INPUT':InputInfo(dataSet='/HLTPhysics/Run2022A-v1/RAW',ls={352567: [[1,126]]})}
steps['RunJetHT2022A']={'INPUT':InputInfo(dataSet='/JetHT/Run2022A-v1/RAW',ls={352567: [[1,126]]})}
steps['RunZeroBias2022A']={'INPUT':InputInfo(dataSet='/ZeroBias/Run2022A-v1/RAW',ls={352567: [[1,126]]})}
steps['RunMinimumBias2022A']={'INPUT':InputInfo(dataSet='/MinimumBias/Run2022A-v1/RAW',ls={352567: [[1,126]]})}

steps['RunHLTPhysics2022A_v2']={'INPUT':InputInfo(dataSet='/HLTPhysics/Run2022A-v1/RAW',ls={353060: [[15,500]]})}
steps['RunZeroBias2022A_v2']={'INPUT':InputInfo(dataSet='/ZeroBias/Run2022A-v1/RAW',ls={353060: [[15,500]]})}
steps['RunMinimumBias2022A_v2']={'INPUT':InputInfo(dataSet='/MinimumBias/Run2022A-v1/RAW',ls={353060: [[15,500]]})}
steps['RunEGamma2022A_v2']={'INPUT':InputInfo(dataSet='/EGamma/Run2022A-v1/RAW',ls={353060: [[15,1278]]})}
steps['RunJetHT2022A_v2']={'INPUT':InputInfo(dataSet='/JetHT/Run2022A-v1/RAW',ls={353060: [[15,1278]]})}
steps['RunMET2022A_v2']={'INPUT':InputInfo(dataSet='/MET/Run2022A-v1/RAW',ls={353060: [[15,1278]]})}
#---------------------------------------------------------------------------------------------------


# Collision 2022B
steps['RunJetHT2022B_v1']={'INPUT':InputInfo(dataSet='/JetHT/Run2022B-v1/RAW',ls={355207: [[1,749]]})}

steps['HLT_Collision22_v1'] = merge( [ {
                '-s': 'L1REPACK:uGT,HLT',
                '--customise': 'L1Trigger/Configuration/customiseUtils.L1TGlobalMenuXML'
                }, step2Defaults] )
steps['RECO_Collision22_v1']=merge([{
                            '-s'            : 'RAW2DIGI,L1Reco,RECO,DQM'},
                            {'--customise':'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3'},
                            step3Defaults])
steps['HARVEST_Collision22_v1'] = merge([ steps['HARVESTDefault'] ])
#---------------------------------------------------------------------------------------------------


# Collision 2022B V2: 18th July 22 After CMSSW_12_4_3
steps['RunZeroBias2022B_v1']={'INPUT':InputInfo(dataSet='/ZeroBias/Run2022B-v1/RAW',ls={355558: [[122,409]]})}
steps['RunHLTPhysics2022B_v1']={'INPUT':InputInfo(dataSet='/HLTPhysics/Run2022B-v1/RAW',ls={355558: [[122,409]]})}
steps['RunEGamma2022B_v1']={'INPUT':InputInfo(dataSet='/EGamma/Run2022B-v1/RAW',ls={355558: [[122,409]]})}

steps['HLT_Collision22_v2'] = step2Defaults
steps['RECO_Collision22_v2']=merge([{
                            '-s'            : 'RAW2DIGI,L1Reco,RECO,DQM'},
                            {'--customise':'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3'},
                            step3Defaults])
steps['HARVEST_Collision22_v2'] = merge([ steps['HARVESTDefault'] ])

# Collision 2022C
steps['RunJetHT2022C_v1']={'INPUT':InputInfo(dataSet='/JetHT/Run2022C-v1/RAW',ls={356005: [[1,202]]})}
steps['RunEGamma2022C_v1']={'INPUT':InputInfo(dataSet='/EGamma/Run2022C-v1/RAW',ls={356005: [[1,202]]})}

#---------------------------------------------------------------------------------------------------
# Collision 2022C: HLT:Custom menu
steps['RunHLTPhysics22D_v1']={'INPUT':InputInfo(dataSet='/HLTPhysics/Run2022D-v1/RAW',ls={357612: [[1,200]]})}
steps['RunMuon22D_v1']={'INPUT':InputInfo(dataSet='/Muon/Run2022D-v1/RAW',ls={357899: [[1,200]]})}
steps['RunJetMET22D_v1']={'INPUT':InputInfo(dataSet='/JetMET/Run2022C-v1/RAW',ls={357442: [[1,200]]})}

steps['HLT_Collision22_v3']=merge( [ {'-s': 'L1REPACK,HLT:Custom'}, step2Defaults] )
#---------------------------------------------------------------------------------------------------
# 28 Sep 2022: Corrected process name to be used after 6.51, 6.52
steps['RECO_Collision22_v3']=merge([{
                            '-s'            : 'RAW2DIGI,L1Reco,RECO,DQM',
                            '--process'     : 'reHLT',
                            },
                            {'--customise':'Configuration/DataProcessing/RecoTLR.customisePostEra_Run3'},
                            step3Defaults])

#---------------------------------------------------------------------------------------------------
