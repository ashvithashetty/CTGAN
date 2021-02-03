from unittest import TestCase
from ctgan.synthesizers import TVAESynthesizer, Decoder, Encoder, loss_function

class TestEncoder(TestCase):

    # METHOD: __init__(self, data_dim, compress_dims, embedding_dim)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: forward(self, input)
    # VALIDATE:
    #     * returned values
    def test_forward(self):
        """Make sure it computes the gradients for all modules, and check
           whether the std is positive."""
        pass


class TestDecoder(TestCase):

    # METHOD: __init__(self, embedding_dim, decompress_dims, data_dim)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: forward(self, input)
    # VALIDATE:
    #     * returned values
    def test_forward(self):
        """Make sure it computes the gradients for all modules, and check
           whether the std is positive."""
        pass


class TestLossFunction(TestCase):

    # METHOD: loss_function(recon_x, x, sigmas, mu, logvar, output_info, factor)
    # VALIDATE:
    #     * assigned values
    def test_loss_function(self):
        """ """
        pass


class TestTVAESynthesizer(TestCase):

    # METHOD: __init__(
    #    self,
    #    embedding_dim=128,
    #    compress_dims=(128, 128),
    #    decompress_dims=(128, 128),
    #    l2scale=1e-5,
    #    batch_size=500,
    #    epochs=300)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        """ """
        pass


    # METHOD: fit(self, train_data, discrete_columns=tuple())
    # VALIDATE:
    #     * returned values
    def test_fit(self):
        """ """
        pass


    # METHOD: _sample(self, samples)
    # VALIDATE:
    #     * returned values
    def test_sample(self):
        """ """
        pass


    # METHOD: set_device(self, device)
    # VALIDATE:
    #     * returned values
    def test_set_device(self):
        """ """
        pass




    def test_continuous(self):
        """Test training the TVAE synthesizer on a small continuous dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a kstest.
        pass

    def test_categorical(self):
        """Test training the TVAE synthesizer on a small categorical dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a cstest.
        pass

    def test_mixed(self):
        """Test training the TVAE synthesizer on a small mixed-type dataset."""
        # verify that the distribution of the samples is close to the distribution of the data
        # using a kstest for continuous + a cstest for categorical.
        pass

