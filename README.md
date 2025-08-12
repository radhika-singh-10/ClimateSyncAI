## ClimateSyncAI

- Implemented a low-latency Flask application to forecast temperature trends for 100 major cities, enabling real-time climate
insights.

- Integrated 13 SARIMAX-based time-series models with K-Means clustering to capture regional patterns in weather behavior
dynamically.



### Steps to be followed - 


i. You would need to uncompress the temperature_prediction folder under src/phase3 folder, which has the user interface codebase. 

ii. After uncompressing, go inside the folder temperature_prediction, and open the terminal pointing to the base or the root of the project. 

iii. To access the models, click on the link (https://drive.google.com/file/d/1TsB8m9uY5CZq-qKkUTxdmvWHI8sWj_MG/view?usp=sharing) and download the sarimax_models.zip. The pickle files are uploaded in the UB Box as the size was greater than 2GB which is the ma limit of UB brightspace. 

iv. Once you download the zip, go inside the temperature_prediction folder, paste the zip, uncompress the zip, and the output folder would be “sarimax_models”. 



### Requirements - 

 To create a virtual environment

```bash
python -m venv climate_venv
```

To download all the Python dependencies. 
```bash
pip install -r requirements.txt
```

To run the application, run 
```bash
python flask.py. 
```

```plaintext
Note -

On your local setup, it would run in debug mode by default. 

However, if you want to run the app in non-debug mode, you can remove the debug=True from app.run(debug=True) 

After running the application, the user interface would be fetched on the localhost (127.0.0.1) and the default port would be 5000 in case this port is free. 
```

To deactivate the virtual environment
```bash
deactivate
```

### Note - The application can be deployed on AWS. Please follow the below steps - 

- Put the 13 models in S3
```
BUCKET=climatesyncai-artifacts           
aws s3 mb s3://$BUCKET || true
aws s3 sync ./sarimax_models s3://$BUCKET/sarimax_models/
```

- Give the EC2 instances S3 read access: The policy (aws-elasticbeanstalk-ec2-role) is attached to a read-only S3 policy to the EB instance profile
```
{
  "Version": "2012-10-17",
  "Statement": [
    {"Effect": "Allow", "Action": ["s3:ListBucket"], "Resource": "arn:aws:s3:::climatesyncai-artifacts"},
    {"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::climatesyncai-artifacts/sarimax_models/*"}
  ]
}
```

- Initialize and create the EB environment
```
pip install awsebcli
aws configure  

eb init -p docker ClimateSyncAI --region us-east-1
eb create climatesyncai-env --single
```

```
eb setenv MODEL_BUCKET=climatesyncai-artifacts MODEL_PREFIX=sarimax_models/
# (Optional) set Flask for the prod env:
eb setenv FLASK_ENV=production
```

- Deploy
```
eb deploy
eb open
eb logs --all
``` 




### If you have any queries, you can reach out to the collaborators - 

-  Radhika Singh - rsingh57@buffalo.edu
-  Ritika Rekhi - ritikare@buffalo.edu
