

# RegResample (NiftyReg)



NiftyReg module for resampling using input transformation

**License** BSD
**Contributor** Marc Modat (UCL)
**Category** Registration.NiftyReg

**type** **ShellOperator**
**template** ``reg_resample {{twarpedGrid|option('blank')}} {{twarpedImage|option('res')}} {{interpolation|option('inter')}} {{paddingValue|option('pad')}}  {{referenceImageName|option('ref')}} {{floatingImageName|option('flo')}} {{inputTransformation|option('trans')}}``


## Inputs

* **referenceImageName** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** input
  **cli_flag** {{referenceImageName|option('ref')}}

  Reference image
  
  Reference image filename (also called Target of Fixed)

* **floatingImageName** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** input
  **cli_flag** {{floatingImageName|option('flo')}}

  Floating image
  
  Floating image filename (also called Source of moving)

* **inputTransformation** : TXT/

  **default** 
  **target** 
  **index** None
  **channel** input
  **cli_flag** {{inputTransformation|option('trans')}}

  Input trans.
  
  Input transformation



## Output

* **warpedImage** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** output
  **cli_flag** {{warpedImage|option('res')}}

  Warped image
  
  Warped floating image

* **warpedGrid** : PNG/

  **default** 
  **target** 
  **index** None
  **channel** output
  **cli_flag** {{warpedGrid|option('blank')}}

  Grid image
  
  Warped blank grid image



## Parameter

* **twarpedGrid** : str/

  **default** 
  **target** True
  **index** 
  **channel** output
  **cli_flag** {{twarpedGrid|option('blank')}}

  Grid image
  
  Warped blank grid image

* **twarpedImage** : str/

  **default** 
  **target** True
  **index** 
  **channel** output
  **cli_flag** {{twarpedImage|option('res')}}

  Warped image
  
  Warped floating image

* **interpolation** : vector.int/

  **default** 
  **target** 
  **index** None
  **channel** None
  **cli_flag** {{interpolation|option('inter')}}

  Interpolation order
  
  Interpolation order to use to warp the floating image
  :Possible Values: ['0', '1', '3', '4']

* **paddingValue** : float/

  **default** 
  **target** 
  **index** None
  **channel** None
  **cli_flag** {{paddingValue|option('pad')}}

  Padding value
  
  Padding value
  :Possible Values: []

