import pytest
from unittest.mock import patch
from gifsicle import app
import os


@pytest.fixture
def mock_subprocess_call():
    with patch('subprocess.call') as mock_call:
        yield mock_call


@pytest.fixture
def mock_getsize():
    with patch('gifsicle.app._getsize', return_value="1 MB") as mock_getsize:
        yield mock_getsize


@pytest.fixture
def mock_sys_argv():
    def _mock_sys_argv(args):
        return ['gifsicle/app.py'] + args
    return _mock_sys_argv


def test_optimize_command(mock_subprocess_call, mock_getsize, mock_sys_argv):
    """
    Tests the optimize command.
    """
    input_file = 'test.gif'
    output_file = 'test_o.gif'
    with patch('sys.argv', mock_sys_argv(['optimize', input_file])):
        app.gif_run()

    expected_call = [
        app.__GIF_EXE,
        '-O2',
        input_file,
        '-o',
        output_file
    ]
    mock_subprocess_call.assert_called_once_with(expected_call)


def test_optimize_command_with_output(mock_subprocess_call, mock_getsize, mock_sys_argv):
    """
    Tests the optimize command with a specified output file.
    """
    input_file = 'test.gif'
    output_file = 'optimized.gif'
    with patch('sys.argv', mock_sys_argv(['optimize', input_file, '-o', output_file])):
        app.gif_run()

    expected_call = [
        app.__GIF_EXE,
        '-O2',
        input_file,
        '-o',
        output_file
    ]
    mock_subprocess_call.assert_called_once_with(expected_call)


def test_resize_command(mock_subprocess_call, mock_getsize, mock_sys_argv):
    """
    Tests the resize command.
    """
    input_file = 'test.gif'
    output_file = 'test_o.gif'
    with patch('sys.argv', mock_sys_argv(['resize', input_file, '--width', '100', '--height', '80'])):
        app.gif_run()

    expected_call = [
        app.__GIF_EXE,
        input_file,
        '-o',
        output_file,
        '--resize',
        '100x80'
    ]
    mock_subprocess_call.assert_called_once_with(expected_call)


def test_scale_command(mock_subprocess_call, mock_getsize, mock_sys_argv):
    """
    Tests the scale command.
    """
    input_file = 'test.gif'
    output_file = 'test_o.gif'
    with patch('sys.argv', mock_sys_argv(['scale', input_file, '--factor', '1.5'])):
        app.gif_run()

    expected_call = [
        app.__GIF_EXE,
        input_file,
        '-o',
        output_file,
        '--scale',
        '1.5'
    ]
    mock_subprocess_call.assert_called_once_with(expected_call)


def test_no_command(mock_subprocess_call, mock_sys_argv):
    """
    Tests that the help message is shown when no command is provided.
    """
    with patch('sys.argv', mock_sys_argv([])):
        with pytest.raises(SystemExit):
            app.gif_run()

    expected_call = [
        app.__GIF_EXE,
        '-h'
    ]
    mock_subprocess_call.assert_called_once_with(expected_call)
