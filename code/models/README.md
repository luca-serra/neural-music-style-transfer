# Models

This folder contains the diverse models which have been developped for this project.
___
## Models overview

### Music generation
First iteration:
- `MLP_GAN`: Multi-Layer Perceptron models are used (for both discriminator and generator).
- `DCGAN_unrolled`: Deep Convolutional unrolled GAN.

Second iteration (note attacked or sustained):
- `DCGAN_tanh`: Deep Convolutional unrolled GAN using tanh as activation function and three values for the state of the note.
- `DCGAN_3D`: Deep Convolutional unrolled GAN using 3-dimension kernels.

### Style transfer
`CYCLE_GAN`: Cycle GAN

___
## Data and instructions 
In order to run these programs, one may download the desired `.ipynb` file and run it in Google Colab. For the `MLP_GAN` and `DCGAN_unrolled` models, the data used was already preprocessed and stored in numpy files (`.npy`), available [here](https://drive.google.com/file/d/1zyN4IEM8LbDHIMSwoiwB6wRSgFyz7MEH/view) (used in [this study](https://arxiv.org/pdf/1809.07575.pdf)). The `JC_J` and `JC_C` folders must then be stored in a `_data.zip` file and uploaded to the Google Colab run time.

For the rest of the models, the data used is the one used in [this study](https://arxiv.org/pdf/1708.03535.pdf). The dataset is composed of MIDI files and has to be preprocessed to be used, using `preprocessing.ipynb` and then uploading the zip file to the Colab run time. Thus, one may be able to use his own MIDI dataset if s.he wants!

___
## Results

Each file contains a part which enables to export the generated music. One must use the `raw_to_midi` function and then use a MIDI to mp3 converter. We advise to use [this online converter](https://onlinesequencer.net/import), very easy to use and which proposes a nice display of the notes played.
