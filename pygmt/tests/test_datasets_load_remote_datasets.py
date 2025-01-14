"""
Test the _load_remote_dataset function.
"""
import pytest
from pygmt.datasets.load_remote_dataset import _load_remote_dataset
from pygmt.exceptions import GMTInvalidInput


def load_remote_dataset_wrapper(resolution="01d", region=None, registration=None):
    """
    Wrapper for _load_remote_dataset using the earth age dataset as an example.
    """
    return _load_remote_dataset(
        dataset_name="earth_age",
        dataset_prefix="earth_age_",
        resolution=resolution,
        region=region,
        registration=registration,
    )


def test_load_remote_dataset_invalid_resolutions():
    """
    Make sure _load_remote_dataset fails for invalid resolutions.
    """
    resolutions = "1m 1d bla 60d 001m 03".split()
    resolutions.append(60)
    for resolution in resolutions:
        with pytest.raises(GMTInvalidInput):
            load_remote_dataset_wrapper(resolution=resolution)


def test_load_remote_dataset_invalid_registration():
    """
    Make sure _load_remote_dataset fails for invalid registrations.
    """
    with pytest.raises(GMTInvalidInput):
        load_remote_dataset_wrapper(registration="improper_type")


def test_load_remote_dataset_tiled_grid_without_region():
    """
    Make sure _load_remote_dataset fails when trying to load a tiled grid
    without specifying a region.
    """
    with pytest.raises(GMTInvalidInput):
        load_remote_dataset_wrapper(resolution="01m")


def test_load_remote_dataset_incorrect_resolution_registration():
    """
    Make sure _load_remote_dataset fails when trying to load a grid
    registration with an unavailable resolution.
    """
    with pytest.raises(GMTInvalidInput):
        load_remote_dataset_wrapper(
            resolution="01m", region=[0, 1, 3, 5], registration="pixel"
        )
