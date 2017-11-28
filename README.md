# RockETS Basestation 

>This project is a python project developped for a student club called RockETS at ETS (École de Technologie Supérieure). RockETS participate anually to the IREC (Intercollegiate Rocket Engineering Competition). The goal of the competition is to develop, build and launch a sounding rocket, reach a precise altitude, perform a scientific experience during the flight and recover the rocket in good shape. To do so, tracking the rocket is essential. This project is the base station that will be used to track the rocket during the flight, get the telemetry data, review the logs, etc., using different serial devices such as a RFD900 and GPS. This version is a V2 version which has been developped with reusability as the main goal as the club will have to eventually monitor a rocket motor. That said, the hard client base station has been converted to a web base application using websockets to update the different dashboard's widgets. The software as it is is not optimized as it has been quickly developped for the last IREC competition and the project is in need of LOVE. The team considers this version of the base station as a proof of concept for a web based base station and not a full working product.

#### Setup
> pip install -r [path/to/requirements.txt]

> Install Redis from https://github.com/MSOpenTech/redis/releases

> Install MongoDB following https://www.mkyong.com/mongodb/how-to-install-mongodb-on-windows/

#### How to contribute ?
- [X] Create a branch by feature and/or bug fix
- [X] Get the code
- [X] Commit and push
- [X] Create a pull request

#### Branch naming

##### Feature branch
> feature/ [Short feature description] [Issue number]

##### Bug branch
> fix/ [Short fix description] [Issue number]

#### Commits syntax:

##### Adding code:
> \+ Added [Short Description] [Issue Number]

##### Deleting code:
> \- Deleted [Short Description] [Issue Number]

##### Modifying code:
> \* Changed [Short Description] [Issue Number]

##### Merging branches:
> Y Merged [Short Description]

Icons made by <a href="http://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>
