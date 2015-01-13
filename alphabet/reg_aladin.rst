

.. role:: red
.. raw:: html

    <style> .red {color: #ff6b59;} </style>

RegAladin (NiftyReg)
===============================




Module/executable for global registration (rigid and/or affine) based on a block-matching approach and a trimmed least squared optimisation.

:License: BSD
:Contributor: Marc Modat, Pankaj Daga, David Cash (UCL)
:Category: Registration.NiftyReg

:type: **ShellOperator**
:template: ``reg_aladin {{toutputWarpedImageName|option('res')}} {{toutputAffineFileName|option('aff')}} {{smoothReferenceWidth|option('smooR')}} {{smoothFloatingWidth|option('smooF')}} {{referenceLowerThreshold|option('refLowThr')}} {{referenceUpperThreshold|option('refUpThr')}} {{floatingLowerThreshold|option('floLowThr')}} {{floatingUpperThreshold|option('floUpThr')}} {{levelPyramidNumber|option('ln')}} {{levelToPerformNumber|option('lp')}} {{iterationNumber|option('maxit')}} {{blockPercentage|option('pv')}} {{inlierPercentage|option('pi')}} {{noSym|flag('noSym')}} {{rigidOnly|flag('rigOnly')}} {{affineOnly|flag('affDirect')}} {{useHeaderOrigin|flag('nac')}} {{makeIsotropic|flag('iso')}} {{interpolation|option('interp')}}  {{referenceImageName|option('ref')}} {{floatingImageName|option('flo')}} {{referenceMaskImageName|option('rmask')}} {{floatingMaskImageName|option('fmask')}} {{inputAffineName|option('inaff')}}``


:Inputs:
    
        * **referenceImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{referenceImageName|option('ref')}}
          Reference image
          
          Reference image filename (also called Target or Fixed)

    
        * **floatingImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{floatingImageName|option('flo')}}
          Floating image
          
          Floating image filename (also called Source or moving)

    
        * **referenceMaskImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{referenceMaskImageName|option('rmask')}}
          Ref. mask
          
          Filename of a mask image in the reference space

    
        * **floatingMaskImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{floatingMaskImageName|option('fmask')}}
          Flo. mask
          
          Filename of a mask image in the floating space. Only used when symmetric turned on

    
        * **inputAffineName** : txt/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{inputAffineName|option('inaff')}}
          Input affine trans. from NiftyReg
          
          Affine registration matrix stored as a text file

    


:Output:
    
        * **outputAffineFileName** : txt/

          :default: 
          :target: 
          :index: None
          :channel: output
          :cli_flag: {{outputAffineFileName|option('aff')}}
          Output affine filename
          
          Affine registration matrix output, saved as a text file

    
        * **outputWarpedImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: output
          :cli_flag: {{outputWarpedImageName|option('res')}}
          Output warped image
          
          Warped floating image

    


:Parameter:
    
        * **toutputWarpedImageName** : str/

          :default: 
          :target: True
          :index: 
          :channel: output
          :cli_flag: {{toutputWarpedImageName|option('res')}}
          Output warped image
          
          Warped floating image

    
        * **toutputAffineFileName** : str/

          :default: 
          :target: True
          :index: 
          :channel: output
          :cli_flag: {{toutputAffineFileName|option('aff')}}
          Output affine filename
          
          Affine registration matrix output, saved as a text file

    
        * **smoothReferenceWidth** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{smoothReferenceWidth|option('smooR')}}
          Ref .Smooth
          
          Standard deviation in mm (voxel if negative) of the Gaussian kernel used to smooth the reference image
          :Possible Values: []

    
        * **smoothFloatingWidth** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{smoothFloatingWidth|option('smooF')}}
          Flo. smooth
          
          Standard deviation in mm (voxel if negative) of the Gaussian kernel used to smooth the Floating image
          :Possible Values: []

    
        * **referenceLowerThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{referenceLowerThreshold|option('refLowThr')}}
          Ref. Low Thr.
          
          Lower threshold value applied to the reference image
          :Possible Values: []

    
        * **referenceUpperThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{referenceUpperThreshold|option('refUpThr')}}
          Ref. Up Thr.
          
          Upper threshold value applied to the reference image
          :Possible Values: []

    
        * **floatingLowerThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{floatingLowerThreshold|option('floLowThr')}}
          Flo. Low Thr.
          
          Lower threshold value applied to the floating image
          :Possible Values: []

    
        * **floatingUpperThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{floatingUpperThreshold|option('floUpThr')}}
          Flo. Up Thr.
          
          Upper threshold value applied to the floating image
          :Possible Values: []

    
        * **levelPyramidNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{levelPyramidNumber|option('ln')}}
          Level number
          
          Number of levels to use to generate the pyramids for the coarse-to-fine approach

    
        * **levelToPerformNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{levelToPerformNumber|option('lp')}}
          Level to perform
          
          Number of levels to use to run the registration once the pyramids have been created

    
        * **iterationNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{iterationNumber|option('maxit')}}
          Iteration number
          
          Maximal number of iterations of the trimmed least square approach to perform per level

    
        * **blockPercentage** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{blockPercentage|option('pv')}}
          Percentage block
          
          Percentage of blocks to use in the optimisation scheme
          :Possible Values: []

    
        * **inlierPercentage** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{inlierPercentage|option('pi')}}
          Percentage inlier
          
          Percentage of blocks to consider as inlier in the optimisation scheme
          :Possible Values: []

    
        * **noSym** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{noSym|flag('noSym')}}
          Disable symmetry
          
          The symmetric version of the algorithm is used by default. Use this flag to disable it

    
        * **rigidOnly** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{rigidOnly|flag('rigOnly')}}
          Rigid only
          
          Performs only a rigid registration, rigid then affine by default

    
        * **affineOnly** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{affineOnly|flag('affDirect')}}
          Affine only
          
          Performs only an affine registration, rigid then affine by default

    
        * **useHeaderOrigin** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{useHeaderOrigin|flag('nac')}}
          Use header
          
          Use the nifti header origin to initialise the transformation. Image centres are used by default

    
        * **makeIsotropic** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{makeIsotropic|flag('iso')}}
          Make images isotropic
          
          Make floating and reference images isotropic if required

    
        * **interpolation** : vector.int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{interpolation|option('interp')}}
          Interpolation order
          
          Interpolation order to use internally to warp the floating image
          :Possible Values: ['0', '1', '3']

    
