| Author: Remi Martin (martinremi60@gmail.com) 	| Date: November 23rd 2022 	|
|---------------------	|-------------------------:	|

# LEMAY.AI INTERVIEW QUESTIONS

# 1) GENERAL KNOWLEDGE VIDEO DEMONSTRATION AND TECHNICAL WRITING SAMPLE
Files sent by email.

# 2) MODEL DEPLOYMENT DEMONSTRATION

- The container can be mounted and used by launching the script named 'run_docker.sh'.
- The web server may take time to fully launch as it downloads the weights of a pretrained model.
- Once the contained is executed and the web server is fully launched, you can use the notebook named 'Client.ipynb'. 
- This notebook prompts the user for an input sentence that is then completed using a Machine Learning model.
- In case the server does not respond, modify the --timeout value in the file 'docker-compose.yml'. This will give the program more time to download the pretrained model.

# 3) EXPLORATORY DATA ANALYSIS DEMONSTRATION
- The notebook named 'DataAnalysis.ipynb' contains the performed exploratory data analysis.
- The dependencies necessary to use the project are listed in the file 'req.txt'.