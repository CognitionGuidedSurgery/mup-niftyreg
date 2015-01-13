

.. role:: red
.. raw:: html

    <style> .red {color: #ff6b59;} </style>

RegF3D (NiftyReg)
===============================




Module/executable for local registration (non-rigid) based on a cubic B-Spline deformation model

:License: BSD
:Contributor: Marc Modat, Pankaj Daga (UCL)
:Category: Registration.NiftyReg

:type: **ShellOperator**
:template: ``reg_f3d {{toutputWarpedImageName|option('res')}} {{toutputCPPFileName|option('cpp')}} {{xAxisSpacing|option('sx')}} {{yAxisSpacing|option('sy')}} {{zAxisSpacing|option('sz')}} {{smoothReferenceWidth|option('smooR')}} {{smoothFloatingWidth|option('smooF')}} {{ReferenceBinNumber|option('rbn')}} {{FloatingBinNumber|option('fbn')}} {{ReferenceIntensityLowerThreshold|option('rLwTh')}} {{ReferenceIntensityUpperThreshold|option('rUpTh')}} {{FloatingIntensityLowerThreshold|option('fLwTh')}} {{FloatingIntensityUpperThreshold|option('fUpTh')}} {{BendingEnergyPenaltyTermWeight|option('be')}} {{L2NormPenaltyTermWeight|option('l2')}} {{JacobianBasedPenaltyTermWeight|option('jl')}} {{NoJacobianBasedPenaltyTermApproximation|flag('noAppJL')}} {{UseNMI|flag('nmi')}} {{UseSSD|flag('ssd')}} {{UseLNCC|option('lncc')}} {{Use_KL_divergence|flag('kld')}} {{levelPyramidNumber|option('ln')}} {{levelToPerformNumber|option('lp')}} {{iterationNumber|option('maxit')}} {{NoConjugateGradient|flag('noConj')}} {{NoPyramid|flag('nopy')}} {{interpolation|option('interp')}} {{useVel|flag('vel')}}  {{referenceImageName|option('ref')}} {{floatingImageName|option('flo')}} {{referenceMaskImageName|option('rmask')}} {{inputAffineName|option('inaff')}} {{inputControlPointPosition|option('incpp')}} {{floatingMaskImageName|option('fmask')}}``


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
          
          Reference mask image filename

    
        * **inputAffineName** : txt/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{inputAffineName|option('inaff')}}
          Input affine trans. from RegAladin
          
          Affine registration matrix stored as a text file

    
        * **inputControlPointPosition** : NRRD/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{inputControlPointPosition|option('incpp')}}
          Input trans. from RegF3D
          
          Control point position image from NiftyReg

    
        * **floatingMaskImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{floatingMaskImageName|option('fmask')}}
          Flo. mask
          
          Floating mask image filename

    


:Output:
    
        * **outputCPPFileName** : NRRD/

          :default: 
          :target: 
          :index: None
          :channel: output
          :cli_flag: {{outputCPPFileName|option('cpp')}}
          Trans. param image
          
          Control point position image

    
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

    
        * **toutputCPPFileName** : str/

          :default: 
          :target: True
          :index: 
          :channel: output
          :cli_flag: {{toutputCPPFileName|option('cpp')}}
          Trans. param image
          
          Control point position image

    
        * **xAxisSpacing** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{xAxisSpacing|option('sx')}}
          x-axis spacing
          
          Control point spacing along the x-axis in mm (in voxel if negative value)
          :Possible Values: []

    
        * **yAxisSpacing** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{yAxisSpacing|option('sy')}}
          y-axis spacing
          
          Control point spacing along the y-axis in mm (in voxel if negative value)
          :Possible Values: []

    
        * **zAxisSpacing** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{zAxisSpacing|option('sz')}}
          z-axis spacing
          
          Control point spacing along the z-axis in mm (in voxel if negative value)
          :Possible Values: []

    
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

    
        * **ReferenceBinNumber** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{ReferenceBinNumber|option('rbn')}}
          Ref. bin number
          
          Number of bin to use for the joint histogram computation - Reference image
          :Possible Values: []

    
        * **FloatingBinNumber** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{FloatingBinNumber|option('fbn')}}
          Flo. bin number
          
          Number of bin to use for the joint histogram computation - Floating image
          :Possible Values: []

    
        * **ReferenceIntensityLowerThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{ReferenceIntensityLowerThreshold|option('rLwTh')}}
          Ref. low thr.
          
          Lower threshold intensity value to apply to the reference image
          :Possible Values: []

    
        * **ReferenceIntensityUpperThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{ReferenceIntensityUpperThreshold|option('rUpTh')}}
          Ref. up thr.
          
          Upper threshold intensity value to apply to the reference image
          :Possible Values: []

    
        * **FloatingIntensityLowerThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{FloatingIntensityLowerThreshold|option('fLwTh')}}
          Flo. low thr.
          
          Lower threshold intensity value to apply to the floating image
          :Possible Values: []

    
        * **FloatingIntensityUpperThreshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{FloatingIntensityUpperThreshold|option('fUpTh')}}
          Flo. up thr.
          
          Upper threshold intensity value to apply to the floating image
          :Possible Values: []

    
        * **BendingEnergyPenaltyTermWeight** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{BendingEnergyPenaltyTermWeight|option('be')}}
          Bending Energ. weight
          
          Weight to apply to the bending energy
          :Possible Values: []

    
        * **L2NormPenaltyTermWeight** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{L2NormPenaltyTermWeight|option('l2')}}
          L2 norm weight
          
          Weight to apply to the L2 norm of the displacement
          :Possible Values: []

    
        * **JacobianBasedPenaltyTermWeight** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{JacobianBasedPenaltyTermWeight|option('jl')}}
          Jac.-based pen. term
          
          Weight to apply to the Jacobian based penalty term
          :Possible Values: []

    
        * **NoJacobianBasedPenaltyTermApproximation** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{NoJacobianBasedPenaltyTermApproximation|flag('noAppJL')}}
          No approx. Jac.-based term
          
          Do not approximate the Jacobian based penalty term at the control point position only

    
        * **UseNMI** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{UseNMI|flag('nmi')}}
          Use NMI
          
          To use the NMI as a measure of similarity

    
        * **UseSSD** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{UseSSD|flag('ssd')}}
          Use SSD
          
          To use the SSD as a measure of similarity instead of the NMI used by default

    
        * **UseLNCC** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{UseLNCC|option('lncc')}}
          Use LNCC
          
          To use the LNCC as a measure of similarity instead of the NMI used by default and set the Gaussian standard deviation
          :Possible Values: []

    
        * **Use_KL_divergence** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{Use_KL_divergence|flag('kld')}}
          Use KLD
          
          To use the KL divergence as a measure of similarity instead of the NMI used by default

    
        * **levelPyramidNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{levelPyramidNumber|option('ln')}}
          Level number
          
          Number of level to use to generate the pyramids for the coarse-to-fine approach

    
        * **levelToPerformNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{levelToPerformNumber|option('lp')}}
          Level to perform
          
          Number of level to use to run the registration once the pyramids have been created

    
        * **iterationNumber** : int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{iterationNumber|option('maxit')}}
          Iteration number
          
          Maximal number of iteration of the trimmed least square approach to perform per total

    
        * **NoConjugateGradient** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{NoConjugateGradient|flag('noConj')}}
          no conj. grad. ascent
          
          By default a conjugate gradient ascent is used. Active this option to use a steepest gradient ascent scheme.

    
        * **NoPyramid** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{NoPyramid|flag('nopy')}}
          no pyramid
          
          Active this option to perform every level at full resolution

    
        * **interpolation** : vector.int/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{interpolation|option('interp')}}
          Interpolation order
          
          Interpolation order to use internally to warp the floating image
          :Possible Values: ['0', '1', '3']

    
        * **useVel** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{useVel|flag('vel')}}
          Use F3D2
          
          Performs a symmetric registration where both, forward and backward transformations are optimised. The transformation are parametrised using a stationary velocity field

    
