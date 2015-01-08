

.. role:: red
.. raw:: html

    <style> .red {color: #ff6b59;} </style>

RegTools (NiftyReg)
===============================




NiftyReg module under construction

:License: BSD
:Contributor: Marc Modat (UCL)
:Category: Registration.NiftyReg

:type: **ShellOperator**
:template: ``reg_tools --float={convertToFloat} --down={downSample} --bin={binarize} --iso={isotropic} --add={addConst} --sub={subConst} --mul={mulConst} --div={divConst} --smo={smooth} --smoG={smooth} --thr={threshold}   --in={inputImageName} --rms={rmsImages} --nan={maskImage} --add={addImage} --sub={subtractImage} --mul={multiplyImage} --div={divideImage} ``


:Inputs:
    
        * **inputImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --in
          Input image
          
          Input image filename

    
        * **rmsImages** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --rms
          Compute RMS 
          
          Compute the mean rms between this image and the input image

    
        * **maskImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --nan
          Mask Image
          
          This image is used to mask the input image. Voxels outside of the mask are set to nan

    
        * **addImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --add
          Add Images
          
          This image is added to the input image

    
        * **subtractImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --sub
          Subtract Images
          
          This image is subtracted from the input image

    
        * **multiplyImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --mul
          Multiply Images
          
          This image is multiplied with input image

    
        * **divideImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --div
          Divide Input Image
          
          The input image is divided by this image

    


:Output:
    


:Parameter:
    
        * **convertToFloat** : bool/

          :default: None
          :target: None
          :index: None
          :channel: None
          :cli_flag: --float
          Convert to float
          
          The input image is converted to float

    
        * **downSample** : bool/

          :default: None
          :target: None
          :index: None
          :channel: None
          :cli_flag: --down
          Downsample
          
          The input image is downsampled 2 times

    
        * **binarize** : bool/

          :default: None
          :target: None
          :index: None
          :channel: None
          :cli_flag: --bin
          Binarize
          
          Binarise the input image (val!=0?val=1:val=0) 

    
        * **isotropic** : bool/

          :default: None
          :target: None
          :index: None
          :channel: None
          :cli_flag: --iso
          Make Isotropic
          
          The resulting image is made isotropic

    
        * **addConst** : float/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --add
          Add
          
          Add the constant value to the input image
          :Possible Values: []

    
        * **subConst** : float/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --sub
          Subtract
          
          Subtract the constant value from the input image
          :Possible Values: []

    
        * **mulConst** : float/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --mul
          Multiply
          
          Multiply the input image with the constant value
          :Possible Values: []

    
        * **divConst** : float/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --div
          Divide
          
          Divide the input image with the constant value
          :Possible Values: []

    
        * **smooth** : float/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --smo
          Smooth (B-Spline)
          
          The input image is smoothed using a cubic b-spline kernel
          :Possible Values: []

    
        * **smooth** : float.vector/

          :default: none
          :target: None
          :index: None
          :channel: None
          :cli_flag: --smoG
          Smooth (Gaussian)
          
          The input image is smoothed using Gaussian kernel

    
        * **threshold** : float/

          :default: None
          :target: None
          :index: None
          :channel: None
          :cli_flag: --thr
          Threshold image
          
          Threshold the input image (val<thr?val=0:val=1) 
          :Possible Values: []

    
