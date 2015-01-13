

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
:template: ``reg_tools {{convertToFloat|flag('float')}} {{downSample|flag('down')}} {{binarize|flag('bin')}} {{isotropic|flag('iso')}} {{addConst|option('add')}} {{subConst|option('sub')}} {{mulConst|option('mul')}} {{divConst|option('div')}} {{smooth|option('smo')}} {{smooth|option('smoG')}} {{threshold|option('thr')}}  {{inputImageName|option('in')}} {{rmsImages|option('rms')}} {{maskImage|option('nan')}} {{addImage|option('add')}} {{subtractImage|option('sub')}} {{multiplyImage|option('mul')}} {{divideImage|option('div')}}``


:Inputs:
    
        * **inputImageName** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{inputImageName|option('in')}}
          Input image
          
          Input image filename

    
        * **rmsImages** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{rmsImages|option('rms')}}
          Compute RMS 
          
          Compute the mean rms between this image and the input image

    
        * **maskImage** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{maskImage|option('nan')}}
          Mask Image
          
          This image is used to mask the input image. Voxels outside of the mask are set to nan

    
        * **addImage** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{addImage|option('add')}}
          Add Images
          
          This image is added to the input image

    
        * **subtractImage** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{subtractImage|option('sub')}}
          Subtract Images
          
          This image is subtracted from the input image

    
        * **multiplyImage** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{multiplyImage|option('mul')}}
          Multiply Images
          
          This image is multiplied with input image

    
        * **divideImage** : PNG/

          :default: 
          :target: 
          :index: None
          :channel: input
          :cli_flag: {{divideImage|option('div')}}
          Divide Input Image
          
          The input image is divided by this image

    


:Output:
    


:Parameter:
    
        * **convertToFloat** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{convertToFloat|flag('float')}}
          Convert to float
          
          The input image is converted to float

    
        * **downSample** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{downSample|flag('down')}}
          Downsample
          
          The input image is downsampled 2 times

    
        * **binarize** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{binarize|flag('bin')}}
          Binarize
          
          Binarise the input image (val!=0?val=1:val=0) 

    
        * **isotropic** : bool/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{isotropic|flag('iso')}}
          Make Isotropic
          
          The resulting image is made isotropic

    
        * **addConst** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{addConst|option('add')}}
          Add
          
          Add the constant value to the input image
          :Possible Values: []

    
        * **subConst** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{subConst|option('sub')}}
          Subtract
          
          Subtract the constant value from the input image
          :Possible Values: []

    
        * **mulConst** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{mulConst|option('mul')}}
          Multiply
          
          Multiply the input image with the constant value
          :Possible Values: []

    
        * **divConst** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{divConst|option('div')}}
          Divide
          
          Divide the input image with the constant value
          :Possible Values: []

    
        * **smooth** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{smooth|option('smo')}}
          Smooth (B-Spline)
          
          The input image is smoothed using a cubic b-spline kernel
          :Possible Values: []

    
        * **smooth** : vector.float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{smooth|option('smoG')}}
          Smooth (Gaussian)
          
          The input image is smoothed using Gaussian kernel

    
        * **threshold** : float/

          :default: 
          :target: 
          :index: None
          :channel: None
          :cli_flag: {{threshold|option('thr')}}
          Threshold image
          
          Threshold the input image (val<thr?val=0:val=1) 
          :Possible Values: []

    
