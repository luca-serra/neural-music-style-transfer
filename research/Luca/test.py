import numpy as np
import os

DATA_PATH = "../_data"


def get_samples(style="J", train=True, n=100, random=False):
    """Return the preprocessed samples

    Parameters
    ----------
    style : str, optional
        Style of the music, one of {"J", "C"} (for "Jazz" and "Classic"), by default "J"
    train : bool, optional
        Whether to choose the train or validation set, by default True
    n : int, optional
        Number of samples which will be returned, by default 100
    random : bool, optional
        Whether to randomize the samples or not, by default False

    Returns
    -------
    List (of Numpy arrays)
        List of samples
    """
    if style == "J":
        folder = "JC_J"
        prefix = "jazz"
    elif style == "C":
        folder = "JC_C"
        prefix = "classic"
    else:
        raise Exception("'style' must be one of {'J', 'C'}")

    train_or_valid = "train" if train else "test"

    nb_samples = sum(
        1
        for item in os.listdir(f"{DATA_PATH}/{folder}/{train_or_valid}")
        if os.path.isfile(os.path.join(f"{DATA_PATH}/{folder}/{train_or_valid}", item))
    )
    numbers = list(range(1, nb_samples))
    if random:
        np.random.shuffle(numbers)
    numbers = numbers[:n]

    samples = []
    for number in numbers:
        sample = np.load(
            f"{DATA_PATH}/{folder}/{train_or_valid}/{prefix}_piano_{train_or_valid}_{number}.npy"
        )
        samples.append(sample[:, :, 0].astype(int))

    return samples


l = get_samples(n=2)
print(l)


NUM_CONV_1 = 10
NUM_CONV_2 = 20

class Discriminator(nn.Module):
    def __init__(self, sz):
        super(Discriminator, self).__init__()
        n_features = 64 * 84
        n_out = 1

        self.conv_1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=5, stride=1)
        self.conv_2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1)
        # self.conv_2 = nn.Conv2d(NUM_CONV_1,NUM_CONV_2,5,1) # kernel_size = 5
        # self.drop = nn.Dropout2d()
        self.fc_1 = nn.Linear(4*4* 64, 100)
        self.fc_2 = nn.Linear(100, 2)

    def forward(self, x):
        x = F.relu(self.conv_1(x))
        x = F.relu(self.conv_2(x))
        x = x.view(-1,4*4*64)
        x = F.relu(self.fc_1(x))
        x = self.fc_2(x)
        return x

class Generator(nn.Module):
    def __init__(self, sz_latent, sz_hidden):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(sz_latent, sz_hidden)
        self.fc2 = nn.Linear(sz_hidden, sz_hidden)
        self.fout = nn.Linear(sz_hidden, 64 * 84)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fout(x)
        return x