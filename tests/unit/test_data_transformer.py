from unittest import TestCase
from ctgan.data_transformer import DataTransformer

class TestDataTransformer(TestCase):

    # METHOD: __init__(self, max_clusters=10, weight_threshold=0.005)
    # VALIDATE:
    #     * attribute values
    def test___init__(self):
        pass

    # METHOD: _fit_continuous(self, column_name, raw_column_data)
    # VALIDATE:
    #     * returned values
    def test___fit_coninuous_(self):
        """Test on a simple coninuous column."""
        pass
    
    # METHOD: _fit_discrete(self, column_name, raw_column_data)
    # VALIDATE:
    #     * returned values
    def test___fit_discrete_(self):
        """Test on a simple discrete column."""
        pass

    # METHOD: fit(self, raw_data, discrete_columns=tuple())
    # VALIDATE:
    #     * attribute values
    def test_fit(self):
        """ """
        pass

    # METHOD: _transform_continuous(self, column_transform_info, raw_column_data)
    # VALIDATE:
    #     * returned values
    def test__transform_continuous(self):
        """ """
        pass

    # METHOD: _transform_discrete(self, column_transform_info, raw_column_data)
    # VALIDATE:
    #     * returned values
    def test__transform_discrete(self):
        """ """
        pass

    # METHOD: transform(self, raw_data)
    # VALIDATE:
    #     * returned values
    def test_transform(self):
        """ """
        pass

    # METHOD: _inverse_transform_continuous(self, column_transform_info, column_data, sigmas, st)
    # VALIDATE:
    #     * returned values
    def test__inverse_transform_continuous(self):
        """ """
        pass

    # METHOD: _inverse_transform_discrete(self, column_transform_info, column_data)
    # VALIDATE:
    #     * returned values
    def test__inverse_transform_discrete(self):
        """ """
        pass 

    # METHOD: inverse_transform(self, data, sigmas=None)
    # VALIDATE:
    #     * returned values
    def test_inverse_transform(self):
        """ """
        pass

    # METHOD: convert_column_name_value_to_id(self, column_name, value)
    # VALIDATE:
    #     * returned values
    def test_convert_column_name_value_to_id(self):
        """ """
        pass




    def test_constant(self):
        """Test transforming a dataframe containing constant values."""
        pass

    def test_df_continuous(self):
        """Test transforming a dataframe containing only continuous values."""
        # validate output ranges [0, 1]
        # validate output shape (# samples, # output dims)
        # validate that forward transform is **not** deterministic
        # make sure it can be inverted
        pass

    def test_df_categorical(self):
        """Test transforming a dataframe containing only categorical values."""
        # validate output ranges [0, 1]
        # validate output shape (# samples, # output dims)
        # validate that forward transform is deterministic
        # make sure it can be inverted
        pass

    def test_df_mixed(self):
        """Test transforming a dataframe containing mixed data types."""
        pass

    def test_df_mixed_nan(self):
        """Test transforming a dataframe containing mixed data types + NaN for categoricals."""
        pass

    def test_np_continuous(self):
        """Test transforming a np.array containing only continuous values."""
        pass

    def test_np_categorical(self):
        """Test transforming a np.array containing only categorical values."""
        pass

    def test_np_mixed(self):
        """Test transforming a np.array containing mixed data types."""
        pass
