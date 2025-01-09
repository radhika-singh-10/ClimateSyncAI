Uncompress the temperature_prediction folder under src/phase3 folder, which has our user interface code. 

After uncompressing, go to inside the folder temperature_prediction, and open the terminal pointing to the base or the root of the project. 

Click on the link https://ubuffalo-my.sharepoint.com/personal/ritikare_buffalo_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fritikare%5Fbuffalo%5Fedu%2FDocuments%2FDICPhase3Models&ct=1702174519027&or=OWA%2DNT&cid=00912ea4%2D3afa%2D903f%2D6b26%2Dd7df88633177&ga=1&WSL=1 and download the sarimax_models.zip. The pickle files are uploaded in the UB Box as the size was greater than 2GB which is the ma limit of UB brightspace. 

Once you download the zip, go inside the temperature_prediciton folder and paste the zip and uncompress the zip and the output folder would be “sarimax_models”. 

Run pip install -r requirements.txt to download all the python dependencies. 

For running the application, run python flask.py. 

On your local setup, it would run in debug mode. 

However, if you want to run the app in non-debug mode, you can remove the debug=True from app.run(debug=True) 

After running the application, the user interface would be fetched on the localhost (127.0.0.1) and the default port would be 5000 in case this port is free. 