from avocado import Test
from avocado.utils import archive
from avocado.utils import process, build
import os

class testin(Test):

    def setUp(self):
        self.url = self.params.get('url', default = ' ')
        tarball = self.fetch_asset(self.url, expire='7d')
        archive.extract(tarball, self.srcdir)

    def test(self):
        print self.srcdir
        self.path = os.path.join(self.srcdir, 'pub_scm_linux_kernel_git_powerpc_linux.git_fixes')
        print self.path
        build.make(self.path, extra_args = 'pseries_le_defconfig')
        build.make(self.path, extra_args ='-j')
        build.make(self.path, extra_args = '-j modules')
        build.make(self.path, extra_args = '-j modules_install')
 
    def tearDown(self):
        build.make(self.path, extra_args = 'clean')

