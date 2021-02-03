from unittest import TestCase
from ctgan.synthesizers import CTGANSynthesizer, Discriminator, Residual, Generator

class TestDiscriminator(TestCase):

    # METHOD: __init__(self, input_dim, discriminator_dim, pack=10)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: calc_gradient_penalty(self, real_data, fake_data, device='cpu', pac=10, lambda_=10)
    # VALIDATE:
    #     * returned values
    def test_calc_gradient_penalty(self):
        """ """
        pass

    # METHOD: forward(self, input)
    # VALIDATE:
    #     * returned values
    def test_forward(self):
        """ """
        pass


class TestResidual(TestCase):

    # METHOD: __init__(self, i, o)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: forward(self, input)
    # VALIDATE:
    #     * returned values
    def test_forward(self):
        """ """
        pass


class TestGenerator(TestCase):

    # METHOD: __init__(self, embedding_dim, generator_dim, data_dim)
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: forward(self, input)
    # VALIDATE:
    #     * returned values
    def test_forward(self):
        """ """
        pass


class TestCTGANSynthesizer(TestCase):

    # METHOD: __init__(self, embedding_dim=128, generator_dim=(256, 256), discriminator_dim=(256, 256),
    #                  generator_lr=2e-4, generator_decay=1e-6, discriminator_lr=2e-4,
    #                  discriminator_decay=0, batch_size=500, discriminator_steps=1, log_frequency=True,
    #                  verbose=False, epochs=300):
    # VALIDATE:
    #     * assigned values
    def test___init__(self):
        pass

    # METHOD: _gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)
    # VALIDATE:
    #     * returned values
    def test__gumbel_softmax(self):
        """ """
        pass

    # METHOD: _apply_activate(self, data)
    # VALIDATE:
    #     * returned values
    def test__apply_activate(self):
        """ """
        pass

    # METHOD: _cond_loss(self, data, c, m)
    # VALIDATE:
    #     * returned values
    def test__cond_loss(self):
        """ """
        pass

    # METHOD: _validate_discrete_columns(self, train_data, discrete_columns)
    # VALIDATE:
    #     * returned values
    def test__validate_discrete_columns(self):
        """ """
        pass

    # METHOD: fit(self, train_data, discrete_columns=tuple(), epochs=None)
    # VALIDATE:
    #     * assigned values
    def test_fit(self):
        """ """
        pass

    # METHOD: sample(self, n, condition_column=None, condition_value=None)
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
        """Test training the CTGAN synthesizer on a continuous dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using kstest:
        #   - uniform (assert p-value > 0.05)
        #   - gaussian (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_categorical(self):
        """Test training the CTGAN synthesizer on a categorical dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using cstest:
        #   - uniform (assert p-value > 0.05)
        #   - very skewed / biased? (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_categorical_log_frequency(self):
        """Test training the CTGAN synthesizer on a small categorical dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using cstest:
        #   - uniform (assert p-value > 0.05)
        #   - very skewed / biased? (assert p-value > 0.05)
        #   - inversely correlated (assert correlation < 0)
        pass

    def test_mixed(self):
        """Test training the CTGAN synthesizer on a small mixed-type dataset."""
        # assert the distribution of the samples is close to the distribution of the data
        # using a kstest for continuous + a cstest for categorical.
        pass

    def test_conditional(self):
        """Test training the CTGAN synthesizer and sampling conditioned on a categorical."""
        # verify that conditioning increases the likelihood of getting a sample with the specified
        # categorical value
        pass

    def test_batch_size_pack_size(self):
        """Test that if batch size is not a multiple of pack size, it raises a sane error."""
        pass
