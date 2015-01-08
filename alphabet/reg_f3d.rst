

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
:template: ``reg_f3d --sx={xAxisSpacing} --sy={yAxisSpacing} --sz={zAxisSpacing} --smooR={smoothReferenceWidth} --smooF={smoothFloatingWidth} --rbn={ReferenceBinNumber} --fbn={FloatingBinNumber} --rLwTh={ReferenceIntensityLowerThreshold} --rUpTh={ReferenceIntensityUpperThreshold} --fLwTh={FloatingIntensityLowerThreshold} --fUpTh={FloatingIntensityUpperThreshold} --be={BendingEnergyPenaltyTermWeight} --l2={L2NormPenaltyTermWeight} --jl={JacobianBasedPenaltyTermWeight} --noAppJL={NoJacobianBasedPenaltyTermApproximation} --nmi={UseNMI} --ssd={UseSSD} --lncc={UseLNCC} --kld={Use_KL_divergence} --ln={levelPyramidNumber} --lp={levelToPerformNumber} --maxit={iterationNumber} --noConj={NoConjugateGradient} --nopy={NoPyramid} --interp={interpolation} --vel={useVel}  --cpp={outputCPPFileName} --res={outputWarpedImageName}  --ref={referenceImageName} --flo={floatingImageName} --rmask={referenceMaskImageName} --inaff={inputAffineName} --incpp={inputControlPointPosition} --fmask={floatingMaskImageName} ``


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
          
          Reference mask image filename

    
        * **inputAffineName** : ['TXT', 'MAT']/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --inaff
          Input affine trans. from RegAladin
          
          Affine registration matrix stored as a text file

    
        * **inputControlPointPosition** : ['NII', 'NII.GZ', 'NRRD']/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --incpp
          Input trans. from RegF3D
          
          Control point position image from NiftyReg

    
        * **floatingMaskImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --fmask
          Flo. mask
          
          Floating mask image filename

    


:Output:
    
        * **outputCPPFileName** : ['NII', 'NII.GZ', 'NRRD']/

          :default: outputCPP.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --cpp
          Trans. param image
          
          Control point position image

    
        * **outputWarpedImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: outputResult.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --res
          Output warped image
          
          Warped floating image

    


:Parameter:
    
        * **xAxisSpacing** : float/

          :default: -5
          :target: None
          :index: None
          :channel: None
          :cli_flag: --sx
          x-axis spacing
          
          Control point spacing along the x-axis in mm (in voxel if negative value)
          :Possible Values: []

    
        * **yAxisSpacing** : float/

          :default: -5
          :target: None
          :index: None
          :channel: None
          :cli_flag: --sy
          y-axis spacing
          
          Control point spacing along the y-axis in mm (in voxel if negative value)
          :Possible Values: []

    
        * **zAxisSpacing** : float/

          :default: -5
          :target: None
          :index: None
          :channel: None
          :cli_flag: --sz
          z-axis spacing
          
          Control point spacing along the z-axis in mm (in voxel if negative value)
          :Possible Values: []

    
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

    
        * **ReferenceBinNumber** : float/

          :default: 64
          :target: None
          :index: None
          :channel: None
          :cli_flag: --rbn
          Ref. bin number
          
          Number of bin to use for the joint histogram computation - Reference image
          :Possible Values: []

    
        * **FloatingBinNumber** : float/

          :default: 64
          :target: None
          :index: None
          :channel: None
          :cli_flag: --fbn
          Flo. bin number
          
          Number of bin to use for the joint histogram computation - Floating image
          :Possible Values: []

    
        * **ReferenceIntensityLowerThreshold** : float/

          :default: -3.4e+38
          :target: None
          :index: None
          :channel: None
          :cli_flag: --rLwTh
          Ref. low thr.
          
          Lower threshold intensity value to apply to the reference image
          :Possible Values: []

    
        * **ReferenceIntensityUpperThreshold** : float/

          :default: 3.4e+38
          :target: None
          :index: None
          :channel: None
          :cli_flag: --rUpTh
          Ref. up thr.
          
          Upper threshold intensity value to apply to the reference image
          :Possible Values: []

    
        * **FloatingIntensityLowerThreshold** : float/

          :default: -3.4e+38
          :target: None
          :index: None
          :channel: None
          :cli_flag: --fLwTh
          Flo. low thr.
          
          Lower threshold intensity value to apply to the floating image
          :Possible Values: []

    
        * **FloatingIntensityUpperThreshold** : float/

          :default: 3.4e+38
          :target: None
          :index: None
          :channel: None
          :cli_flag: --fUpTh
          Flo. up thr.
          
          Upper threshold intensity value to apply to the floating image
          :Possible Values: []

    
        * **BendingEnergyPenaltyTermWeight** : float/

          :default: 0.005
          :target: None
          :index: None
          :channel: None
          :cli_flag: --be
          Bending Energ. weight
          
          Weight to apply to the bending energy
          :Possible Values: []

    
        * **L2NormPenaltyTermWeight** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --l2
          L2 norm weight
          
          Weight to apply to the L2 norm of the displacement
          :Possible Values: []

    
        * **JacobianBasedPenaltyTermWeight** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --jl
          Jac.-based pen. term
          
          Weight to apply to the Jacobian based penalty term
          :Possible Values: []

    
        * **NoJacobianBasedPenaltyTermApproximation** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --noAppJL
          No approx. Jac.-based term
          
          Do not approximate the Jacobian based penalty term at the control point position only

    
        * **UseNMI** : bool/

          :default: true
          :target: None
          :index: None
          :channel: None
          :cli_flag: --nmi
          Use NMI
          
          To use the NMI as a measure of similarity

    
        * **UseSSD** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --ssd
          Use SSD
          
          To use the SSD as a measure of similarity instead of the NMI used by default

    
        * **UseLNCC** : float/

          :default: -999999
          :target: None
          :index: None
          :channel: None
          :cli_flag: --lncc
          Use LNCC
          
          To use the LNCC as a measure of similarity instead of the NMI used by default and set the Gaussian standard deviation
          :Possible Values: []

    
        * **Use_KL_divergence** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --kld
          Use KLD
          
          To use the KL divergence as a measure of similarity instead of the NMI used by default

    
        * **levelPyramidNumber** : int/

          :default: 3
          :target: None
          :index: None
          :channel: None
          :cli_flag: --ln
          Level number
          
          Number of level to use to generate the pyramids for the coarse-to-fine approach

    
        * **levelToPerformNumber** : int/

          :default: 3
          :target: None
          :index: None
          :channel: None
          :cli_flag: --lp
          Level to perform
          
          Number of level to use to run the registration once the pyramids have been created

    
        * **iterationNumber** : int/

          :default: 300
          :target: None
          :index: None
          :channel: None
          :cli_flag: --maxit
          Iteration number
          
          Maximal number of iteration of the trimmed least square approach to perform per total

    
        * **NoConjugateGradient** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --noConj
          no conj. grad. ascent
          
          By default a conjugate gradient ascent is used. Active this option to use a steepest gradient ascent scheme.

    
        * **NoPyramid** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --nopy
          no pyramid
          
          Active this option to perform every level at full resolution

    
        * **interpolation** : vector.int/

          :default: 1
          :target: None
          :index: None
          :channel: None
          :cli_flag: --interp
          Interpolation order
          
          Interpolation order to use internally to warp the floating image
          :Possible Values: ['0', '1', '3']

    
        * **useVel** : bool/

          :default: false
          :target: None
          :index: None
          :channel: None
          :cli_flag: --vel
          Use F3D2
          
          Performs a symmetric registration where both, forward and backward transformations are optimised. The transformation are parametrised using a stationary velocity field

    
