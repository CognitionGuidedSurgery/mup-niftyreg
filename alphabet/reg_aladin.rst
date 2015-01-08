

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
:template: ``reg_aladin --smooR={smoothReferenceWidth} --smooF={smoothFloatingWidth} --refLowThr={referenceLowerThreshold} --refUpThr={referenceUpperThreshold} --floLowThr={floatingLowerThreshold} --floUpThr={floatingUpperThreshold} --ln={levelPyramidNumber} --lp={levelToPerformNumber} --maxit={iterationNumber} --pv={blockPercentage} --pi={inlierPercentage} --noSym={noSym} --rigOnly={rigidOnly} --affDirect={affineOnly} --nac={useHeaderOrigin} --iso={makeIsotropic} --interp={interpolation}  --aff={outputAffineFileName} --res={outputWarpedImageName}  --ref={referenceImageName} --flo={floatingImageName} --rmask={referenceMaskImageName} --fmask={floatingMaskImageName} --inaff={inputAffineName} ``


:Inputs:
    
        * **referenceImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --ref
          Reference image
          
          Reference image filename (also called Target or Fixed)

    
        * **floatingImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --flo
          Floating image
          
          Floating image filename (also called Source or moving)

    
        * **referenceMaskImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --rmask
          Ref. mask
          
          Filename of a mask image in the reference space

    
        * **floatingMaskImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --fmask
          Flo. mask
          
          Filename of a mask image in the floating space. Only used when symmetric turned on

    
        * **inputAffineName** : ['TXT', 'MAT']/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --inaff
          Input affine trans. from NiftyReg
          
          Affine registration matrix stored as a text file

    


:Output:
    
        * **outputAffineFileName** : ['TXT', 'MAT']/

          :default: outputAffineResult.txt
          :target: None
          :index: None
          :channel: output
          :cli_flag: --aff
          Output affine filename
          
          Affine registration matrix output, saved as a text file

    
        * **outputWarpedImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: outputAffineResult.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --res
          Output warped image
          
          Warped floating image

    


:Parameter:
    
        * **smoothReferenceWidth** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --smooR
          Ref .Smooth
          
          Standard deviation in mm (voxel if negative) of the Gaussian kernel used to smooth the reference image
          :Possible Values: []

    
        * **smoothFloatingWidth** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --smooF
          Flo. smooth
          
          Standard deviation in mm (voxel if negative) of the Gaussian kernel used to smooth the Floating image
          :Possible Values: []

    
        * **referenceLowerThreshold** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --refLowThr
          Ref. Low Thr.
          
          Lower threshold value applied to the reference image
          :Possible Values: []

    
        * **referenceUpperThreshold** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --refUpThr
          Ref. Up Thr.
          
          Upper threshold value applied to the reference image
          :Possible Values: []

    
        * **floatingLowerThreshold** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --floLowThr
          Flo. Low Thr.
          
          Lower threshold value applied to the floating image
          :Possible Values: []

    
        * **floatingUpperThreshold** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --floUpThr
          Flo. Up Thr.
          
          Upper threshold value applied to the floating image
          :Possible Values: []

    
        * **levelPyramidNumber** : int/

          :default: 3
          :target: None
          :index: None
          :channel: None
          :cli_flag: --ln
          Level number
          
          Number of levels to use to generate the pyramids for the coarse-to-fine approach

    
        * **levelToPerformNumber** : int/

          :default: 3
          :target: None
          :index: None
          :channel: None
          :cli_flag: --lp
          Level to perform
          
          Number of levels to use to run the registration once the pyramids have been created

    
        * **iterationNumber** : int/

          :default: 5
          :target: None
          :index: None
          :channel: None
          :cli_flag: --maxit
          Iteration number
          
          Maximal number of iterations of the trimmed least square approach to perform per level

    
        * **blockPercentage** : float/

          :default: 50
          :target: None
          :index: None
          :channel: None
          :cli_flag: --pv
          Percentage block
          
          Percentage of blocks to use in the optimisation scheme
          :Possible Values: []

    
        * **inlierPercentage** : float/

          :default: 50
          :target: None
          :index: None
          :channel: None
          :cli_flag: --pi
          Percentage inlier
          
          Percentage of blocks to consider as inlier in the optimisation scheme
          :Possible Values: []

    
        * **noSym** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --noSym
          Disable symmetry
          
          The symmetric version of the algorithm is used by default. Use this flag to disable it

    
        * **rigidOnly** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --rigOnly
          Rigid only
          
          Performs only a rigid registration, rigid then affine by default

    
        * **affineOnly** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --affDirect
          Affine only
          
          Performs only an affine registration, rigid then affine by default

    
        * **useHeaderOrigin** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --nac
          Use header
          
          Use the nifti header origin to initialise the transformation. Image centres are used by default

    
        * **makeIsotropic** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --iso
          Make images isotropic
          
          Make floating and reference images isotropic if required

    
        * **interpolation** : vector.int/

          :default: 1
          :target: None
          :index: None
          :channel: None
          :cli_flag: --interp
          Interpolation order
          
          Interpolation order to use internally to warp the floating image
          :Possible Values: ['0', '1', '3']

    
