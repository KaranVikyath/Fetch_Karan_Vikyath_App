# Fetch_Karan_Vikyath_App

You can run the webservice in two ways:

Method 1: Running the app directly
1. Download the files from the repository
2. After navigating to current directory in command prompt, run the below command to install all dependencies
   pip install -r requirements.txt
3. Then run the below command to start the app
   python app.py
4. Once the app starts running copy the url mentioned or http://127.0.0.1:5000/ in your browser and press Enter.
   
Method 2: Using Docker Container
1. If you dont have Docker installed, install it and run the below command on your command prompt
   docker pull karanvikyath/fetch_karan_vikyath_app:latest
2. Then run the below command after pulling the above docker image
   docker run -p 5000:5000 karanvikyath/fetch_karan_vikyath_app:latest
3. Once the app starts running copy the url mentioned or http://127.0.0.1:5000/ in your browser and press Enter.
