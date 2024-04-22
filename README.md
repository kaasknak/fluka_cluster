### Input file generator for FLUKA on cluster systems.
These python3 scripts can be used to generate fluka inputfiles for cluster systems that don't allow access to flair.
In case the cluster uses *slurm* and you push your simulations using an array, the system requires iterative numbering of the input file.

### Pushing a simulation to the cluster.
On your (local/remote) machine place *push.py* in the same folder as your input file and execute in a terminal

```shell
python3 push.py filename.inp 1 10 folder
```
 1. *filename.inp* is your inputfile. 
 2. *1* is the first number you will start with.
 3. *10* is the final number on the input file.
 4. *folder* is a folder that will be created where the inputfiles are placed.

The inputfiles in the folder will follow the logic ***filename_i.inp*** where *i* indicates the number of the newly created inputfile.
The random seed will be changed for every individual inputfile automatically.

(Optional) If working on the local machine, you should be able to enter the folder and upload all the files to your desired location on the cluster and start the calculation there.

### Processing your simulation data in flair.
After the cluster is done with your simulations you can enter into the folder created using *push.py* and make sure *pull.py* is placed in the same folder. Than execute in a terminal:

```shell
python3 pull.py file_stem
```
 1. *file_stem* is the main repeatable part of the original inputfile.

This action should rename all filenames back to the logic flair uses.
You should now be able to open *filename.inp* using flair and all data should be present.

### Limitations
*push.py* can only generate inputfiles for 676 parallel jobs (but it is rather unlikely you have that many CPUs available anyway).
*pull.py* can only convert files back if the number of cycles wasn't higher than nine

### Execution of simulations
```shell
 $FLUPRO/flutil/rfluka -N0 -MX inputfile
````
*X* is the number of cycles.

This script starts counting from 1. Not from 0. If you ask it to start at 0 it will crash.

### Dependencies
*push.py* requires the following programs to be installed:
 1. python3
 2. GNU sed
 3. The python packages os, sys

*pull.py* requires the following programs to be installed:
 1. python3
 3. The python packages os, sys, re

### How do I get these scripts without copy pasting?
Easiest way is just to use git. Open the terminal and type
```shell
git clone https://github.com/kaasknak/fluka_cluster.git
```
And you should find everything in the folder called *fluka_cluster*
