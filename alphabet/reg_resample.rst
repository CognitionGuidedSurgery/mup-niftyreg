

.. role:: red
.. raw:: html

    <style> .red {color: #ff6b59;} </style>

RegResample (NiftyReg)
===============================




NiftyReg module for resampling using input transformation

:License: BSD
:Contributor: Marc Modat (UCL)
:Category: Registration.NiftyReg

:type: **ShellOperator**
:template: ``reg_resample --inter={interpolation} --pad={paddingValue}  --res={warpedImage} --blank={warpedGrid}  --ref={referenceImageName} --flo={floatingImageName} --trans={inputTransformation} ``


:Inputs:
    
        * **referenceImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --ref
          Reference image
          
          Reference image filename (also called Target of Fixed)

    
        * **floatingImageName** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --flo
          Floating image
          
          Floating image filename (also called Source of moving)

    
        * **inputTransformation** : ['TXT', 'MAT', 'NII', 'NII.GZ', 'NRRD']/

          :default: None
          :target: None
          :index: None
          :channel: input
          :cli_flag: --trans
          Input trans.
          
          Input transformation

    


:Output:
    
        * **warpedImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: warpedImage.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --res
          Warped image
          
          Warped floating image

    
        * **warpedGrid** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: warpedGrid.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --blank
          Grid image
          
          Warped blank grid image

    


:Parameter:
    
        * **interpolation** : vector.int/

          :default: 3
          :target: None
          :index: None
          :channel: None
          :cli_flag: --inter
          Interpolation order
          
          Interpolation order to use to warp the floating image
          :Possible Values: ['0', '1', '3', '4']

    
        * **paddingValue** : float/

          :default: 0
          :target: None
          :index: None
          :channel: None
          :cli_flag: --pad
          Padding value
          
          Padding value
          :Possible Values: []

    
