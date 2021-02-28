# Models

This folder contains the diverse models which have been developped for this project.

## Model overview


## Data and instructions 
In order to execute these programs, one may download the desired `.ipynb` file and run it in Google Colab. For the `MLP_GAN` and `DCGAN_unrolled` models, the data used was already preprocessed and stored in numpy files (`.npy`), available [here](https://drive.google.com/file/d/1zyN4IEM8LbDHIMSwoiwB6wRSgFyz7MEH/view) and used in [this study](https://arxiv.org/pdf/1809.07575.pdf). The `JC_J` and `JC_C` folders must then be stored in a `_data.zip` file and uploaded to the Google Colab run time.

For the rest of the models, the data used is the one used in [this study](https://arxiv.org/pdf/1708.03535.pdf). The dataset is composed of MIDI files and has to be preprocessed to be used, using `preprocessing.ipynb` and then uploading the zip file to the Colab run time. Thus, one may be able to use his own MIDI dataset if s.he wants!

## Results

Each file contains a part which enables to export the generated music. One must use the `raw_to_midi` function and then use a MIDI to mp3 converter. We advise to use [this online converter](https://onlinesequencer.net/import), very easy to use and which proposes a nice display of the notes played.
