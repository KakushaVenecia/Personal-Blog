# Personal Blog

## Description

Personal blog that consumes the a quotes API

## Author



### Running the Application

1. Pre-requisites

   - Ensure to activate virtual environment called virtual,using:

     - source virtual/bin/activate

   - Install flask and pip
   - Install flask_script

2. Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app ('development')
3. Add the export configurations in a start.sh

   - export SECRET_KEY= "Your secret key"
   - export API_KEY= "Your Api key"

4. Run using the executable file ,with command :
   - ./start.sh


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between Subscribe and login|

## Contact Information

For any further inquiries or contributions or comments, reach me at [Kakusha Venecia](https://github.com/KakushaVenecia)

### License

[MIT License](https://github.com/KakushaVenecia/Personal-Blog/blob/main/license)

Copyright (c) 2022
