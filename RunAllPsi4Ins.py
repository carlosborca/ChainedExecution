#!/usr/bin/env python

#
# @BEGIN LICENSE
#
# RunAllPsi4Ins: The tool for the automated execution of Psi4 inputs.
#
# Copyright (c) 2020
# Carlos H. Borca
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of CrystaLattE.
#
# CrystaLattE is free software; you can redistribute it and/or modify
# it under the tesms of the GNU Lesser General Public License as
# published by the Free Software Foundation, version 3.
#
# CrystaLattE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with CrystaLattE; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA.
#
# @END LICENSE
#

# Import standard Python modules.
import os
import subprocess
import time

# ======================================================================
def main(verbose=0):

    # Start counting execution time.
    start = time.time()

    d = os.getcwd()
    cpus = str(os.cpu_count())
    
    # Input and output checklists.
    inList  = []
    outList = []

    for f in os.listdir(d):
        
        # Find input files using the default extension.
        if f.endswith(".in"):
            
            # Add input file to an input file checklist.
            inList.append(f[:-3])

    # If outputs are missing, run them.
    while inList != outList:
        
        #print(inList)  # Debug.
        #print(outList) # Debug.
        
        # Empty the checklists. This avoids an infinite loop if an
        # input is removed while the script is being executed.
        inList = []
        outList = []

        for f in os.listdir(d):
            
            # Find input files using the default extension.
            if f.endswith(".in"):
            
                # Repopulate the inputs checklist.
                inList.append(f[:-3])
                
                outf = "{}.out".format(f[:-3])

                if not os.path.exists(outf):
                    print("Executing command: {} {} {} {} {}".format("psi4", "-i", f, "-n", cpus))
                    subprocess.run(["psi4", "-i", f, "-n", cpus])

        for f in os.listdir(d):
            
            # Find input files using the default extension.
            if f.endswith(".out"):

                if not f in outList:
                    outList.append(f[:-4])

    print("All inputs have name-matching outputs. Execution terminated.")

# ======================================================================
    
if __name__ == "__main__":
    main(1)
