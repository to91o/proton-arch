"""Exercise safe CLI boundaries without changing the host network or packages."""
import pathlib
import subprocess
import unittest

CLI = pathlib.Path(__file__).resolve().parents[1] / "proton-arch"


class CommandTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(["bash", str(CLI), *args], capture_output=True, text=True)

    def test_help(self):
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("install|doctor|launch", result.stdout)

    def test_unknown_command_fails(self):
        result = self.run_cli("invalid-command")
        self.assertEqual(result.returncode, 2)

    @unittest.skipIf(pathlib.Path("/etc/arch-release").exists(), "non-Arch guard")
    def test_install_refuses_non_arch(self):
        result = self.run_cli("install")
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires Arch Linux", result.stderr)

    @unittest.skipIf(pathlib.Path("/etc/arch-release").exists(), "non-Arch guard")
    def test_launch_refuses_non_arch(self):
        result = self.run_cli("launch")
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires Arch Linux", result.stderr)
