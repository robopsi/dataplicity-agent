from dataplicity.subcommands.version import Version
from dataplicity import __version__


def test_version(capsys):
    version = Version(None)
    version.run()
    out, err = capsys.readouterr()

    assert out == __version__
    assert err == ''