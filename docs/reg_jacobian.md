

# RegJacobian (NiftyReg)



NiftyReg module to create Jacobian-based images

**License** BSD
**Contributor** Marc Modat (UCL)
**Category** Registration.NiftyReg

**type** **ShellOperator**
**template** ``reg_jacobian {{tJacMatImage|option('jacM')}} {{tlogJacDetImage|option('jacL')}} {{tjacDetImage|option('jac')}}  {{InTrans|option('trans')}} {{referenceImageName|option('ref')}}``


## Inputs

* **InTrans** : TXT/

  **default** 
  **target** 
  **index** None
  **channel** input
  **cli_flag** {{InTrans|option('trans')}}

  Input Trans.
  
  Input transformation

* **referenceImageName** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** input
  **cli_flag** {{referenceImageName|option('ref')}}

  Reference image
  
  Reference image filename, required if the transformation is a spline parametrisation



## Output

* **jacDetImage** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** output
  **cli_flag** {{jacDetImage|option('jac')}}

  Jac. det. image
  
  Jacobian determinant image

* **logJacDetImage** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** output
  **cli_flag** {{logJacDetImage|option('jacL')}}

  Log. Jac. det. image
  
  Log of the Jacobian determinant image

* **JacMatImage** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** output
  **cli_flag** {{JacMatImage|option('jacM')}}

  Jac. mat. image
  
  Jacobian matrix image



## Parameter

* **tJacMatImage** : str/

  **default** 
  **target** True
  **index** 
  **channel** output
  **cli_flag** {{tJacMatImage|option('jacM')}}

  Jac. mat. image
  
  Jacobian matrix image

* **tlogJacDetImage** : str/

  **default** 
  **target** True
  **index** 
  **channel** output
  **cli_flag** {{tlogJacDetImage|option('jacL')}}

  Log. Jac. det. image
  
  Log of the Jacobian determinant image

* **tjacDetImage** : str/

  **default** 
  **target** True
  **index** 
  **channel** output
  **cli_flag** {{tjacDetImage|option('jac')}}

  Jac. det. image
  
  Jacobian determinant image

