

.. role:: red
.. raw:: html

    <style> .red {color: #ff6b59;} </style>

RegJacobian (NiftyReg)
===============================




NiftyReg module to create Jacobian-based images

:License: BSD
:Contributor: Marc Modat (UCL)
:Category: Registration.NiftyReg

:type: **ShellOperator**
:template: ``reg_jacobian  --jac={jacDetImage} --jacL={logJacDetImage} --jacM={JacMatImage}  --trans={InTrans} --ref={referenceImageName} ``


:Inputs:
    
        * **InTrans** : ['NII', 'NII.GZ', 'NRRD', 'TXT', 'MAT']/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --trans
          Input Trans.
          
          Input transformation

    
        * **referenceImageName** : Image.NII,Image.NII..GZ,Image.NRRD,Image.PNG/

          :default: required
          :target: None
          :index: None
          :channel: input
          :cli_flag: --ref
          Reference image
          
          Reference image filename, required if the transformation is a spline parametrisation

    


:Output:
    
        * **jacDetImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: jacDetImage.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --jac
          Jac. det. image
          
          Jacobian determinant image

    
        * **logJacDetImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: logJacDetImage.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --jacL
          Log. Jac. det. image
          
          Log of the Jacobian determinant image

    
        * **JacMatImage** : Image.NII,Image.NII.GZ,Image.NRRD,Image.PNG/

          :default: JacMatImage.nii
          :target: None
          :index: None
          :channel: output
          :cli_flag: --jacM
          Jac. mat. image
          
          Jacobian matrix image

    


:Parameter:
    
