# Python script for generating Haptic pattern for an audio track  
  
Currently generating pattern following the syntax of [Haptica](https://github.com/efremidze/Haptica)
  
![alt text][logo]

[logo]: https://buet-edu-1.s3.amazonaws.com/auto_upload/0RMFi9mrPNe7mol2JwcZAf40F3n2/1623300841647.png "Logo Title Text 2"
  
The pattern is generated considering 3 Thresholding limits, resulting in 4 regions for '-','.','o' and 'O' , denoting __No__, __Light__, __Medium__ and __Heavy__ haptic feedback respectively.   
  
Parameter list for __*getHapticaPattern()*__

| Parameter | Type | Default Value | Description |
| --- | -- | ----------- |----|
|file|string|-|audio file location|
|thr1|float|25|1st threshold limit in percentage, denoted by green line in the graph|
|thr2|float|50|2nd threshold limit in percentage, denoted by blue line in the graph|
|thr3|float|75|3rd threshold limit in percentage, denoted by red line in the graph|
|slot|float|0.1|duration of a single pattern character|
|plot|boolean|True|plotting and showing the graph or not|
