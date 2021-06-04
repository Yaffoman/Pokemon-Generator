***Most taken from https://github.com/forcecore/Keras-GAN-Animeface-Character ***

### General Structure
* args.py - contains hyperparameters used in training
* augment.py - augments a dataset by flipping in three directions (individually and combined) and added noise
    * results in 5x more data
  
* data.py - Resizes a dataset and converts to hdf5 file for easy ingestion
* gan.py - Actual training script, build_networks() is where to tinker with learning rate and optimizer
* nets.py - Defines the discriminator and generator networks in keras
* randomGen.py - Used to generate random names
* script.py - Used to cartoonize results for cleaner Pokemon

### Training Steps:
* Acquire dataset of images
* Run data.py to resize them (size taken from Args.sz) by changing the path at the bottom
    * Optionally run test in data.py to make sure values got put into [0,1] range
* Change gan.py at the bottom to pick which functions to run
* Run gan.py
    * Loss for d0 and d1 should be under 1 while gen loss should be between 1 and 4

### Generate Steps:
* uncomment generate line in gan.py with desired number of samples

