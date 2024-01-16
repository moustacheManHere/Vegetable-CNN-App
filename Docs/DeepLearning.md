Compatibility Issues:
    - Can't use my final_large.keras for this project because I use a M1 mac and have custom tensorflow which is maintained by apple 
    - ca1 keras model was saved with tenforflow version 2.13.0 and I'm using 2.15.0 so some of the layers are not compatible -> got the error "Layer 'layer_normalization_2' expected 2 variables, but received 0"
    - I tried to change the tensorflow version by downgrading my mac to 2.13.0 -> got "'Adam' object has no attribute 'build'" again due to version mismatch
    - In the end I decided to retrain the model from scratch in my Mac using the old dataset

Retraining:
    - Dataset is located in DL folder but gitignore will block it cuz its too big
    - I plan to train the model first. 