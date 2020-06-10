import mock
import pytest
from absl import app
from project import main


@pytest.mark.sanity
@mock.patch.object(app, 'run', autospec=True)
def test_entrypoint(mock_run):
    main.entry_point()
    mock_run.assert_called_with(main.main)
