#!/usr/bin/env python

import os
import subprocess
from avocado import Test
from avocado.utils import process, git

class testin(Test):

    def setUp(self):
        self.url = 'https://github.com/linux-test-project/ltp.git'
        self.destination = '/root'
        git.get_repo(self.url,destination_dir = self.destination)

    def test(self):
        print "done"
        subprocess.call(['cd /root/ltp'])
        print "done"
        subprocess.call(['make','menuconfig'])
        subprocess.call(['make', '-j', 'vmlinux'])
        subprocess.call(['make'])
        print "done"
        subprocess.call(['make', '-j','modules'])
        subprocess.call(['make','modules_install'])
  
    def cleanUp(self):
        subprocess.call(['make','clean'])

