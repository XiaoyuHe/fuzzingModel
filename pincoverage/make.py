#! /usr/bin/env python
### BEGIN LICENSE ###
### Use of the CERT Basic Fuzzing Framework and related source code
### is subject to the terms of the following licenses:
### 
### GNU Public License (GPL) Rights pursuant to Version 2, June 1991
### Government Purpose License Rights (GPLR) pursuant to DFARS
### 252.227.7013
### 
### NO WARRANTY
### 
### ANY INFORMATION, MATERIALS, SERVICES, INTELLECTUAL
### PROPERTY OR OTHER PROPERTY OR RIGHTS GRANTED OR
### PROVIDED BY CARNEGIE MELLON UNIVERSITY PURSUANT TO
### THIS LICENSE (HEREINAFTER THE "DELIVERABLES") ARE ON
### AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES
### NO WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED
### AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO,
### WARRANTY OF FITNESS FOR A PARTICULAR PURPOSE,
### MERCHANTABILITY, INFORMATIONAL CONTENT,
### NONINFRINGEMENT, OR ERROR-FREE OPERATION. CARNEGIE
### MELLON UNIVERSITY SHALL NOT BE LIABLE FOR INDIRECT,
### SPECIAL OR CONSEQUENTIAL DAMAGES, SUCH AS LOSS OF
### PROFITS OR INABILITY TO USE SAID INTELLECTUAL
### PROPERTY, UNDER THIS LICENSE, REGARDLESS OF WHETHER
### SUCH PARTY WAS AWARE OF THE POSSIBILITY OF SUCH
### DAMAGES. LICENSEE AGREES THAT IT WILL NOT MAKE ANY
### WARRANTY ON BEHALF OF CARNEGIE MELLON UNIVERSITY,
### EXPRESS OR IMPLIED, TO ANY PERSON CONCERNING THE
### APPLICATION OF OR THE RESULTS TO BE OBTAINED WITH
### THE DELIVERABLES UNDER THIS LICENSE.
### 
### Licensee hereby agrees to defend, indemnify, and hold harmless
### Carnegie Mellon University, its trustees, officers, employees,
### and agents from all claims or demands made against them (and any
### related losses, expenses, or attorney's fees) arising out of, or
### relating to Licensee's and/or its sub licensees' negligent use or
### willful misuse of or negligent conduct or willful misconduct
### regarding the Software, facilities, or other rights or assistance
### granted by Carnegie Mellon University under this License,
### including, but not limited to, any claims of product liability,
### personal injury, death, damage to property, or violation of any
### laws or regulations.
### 
### Carnegie Mellon University Software Engineering Institute
### authored documents are sponsored by the U.S. Department of
### Defense under Contract F19628-00-C-0003. Carnegie Mellon
### University retains copyrights in all material produced under this
### contract. The U.S.  Government retains a non-exclusive,
### royalty-free license to publish or reproduce these documents, or
### allow others to do so, for U.S.  Government purposes only
### pursuant to the copyright license under the contract clause at
### 252.227.7013.
### END LICENSE ###

# as of 5/7/2013, the directions here don't work:
# http://software.intel.com/sites/landingpage/pintool/docs/58423/Pin/html/
import subprocess, shlex, platform, os

bin = "coverage.so"

machine = platform.machine()
if machine == "i686":
    machine = "x86"
    srcdir = "obj-ia32"
else:
    srcdir = "obj-intel64"
src = os.path.join(srcdir, bin)
dstdir = "."
dst = os.path.join(dstdir, bin)

cmd = "make PIN_ROOT=/home/fuzz/pin"
print cmd
subprocess.call(shlex.split(cmd))

cmd = "mkdir -p %s" % dstdir
print cmd
subprocess.call(shlex.split(cmd))

cmd = "mv %s %s" % (src, dst)
print cmd
subprocess.call(shlex.split(cmd))

cmd = "rm -rf %s" % srcdir
print cmd
subprocess.call(shlex.split(cmd))
