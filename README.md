### Input file generator for FLUKA on cluster systems.
These python3 programs can be used to generate fluka inputfiles for cluster systems that don't allow you access to flair.
In case these systems use slurm and you push your simulations using an array the system requires iterative numbering of the input file.

### Pushing a simulation to the cluster.
On your local machine place place push.py in the same folder as your input file and type

```shell
python3 push.py filename.inp 1 10 folder
```
 1. *filename.inp* is your inputfile. 
 2. *1* is the first number you will start with.
 3. *10* is the final number on the input file.
 4. *folder* is a folder that will be created where the inputfiles are placed.
The inputfiles in the folder will follow the logic *filename_i.inp* where *i* is the number of the inputfile.
The random seed will be changed for every individual inputfile automatically.
You should be able to enter the folder and upload all the files to your desired folder on a cluster and start the calculation there.

### Processing your simulation data in flair.
After the cluster is done with your simulations you can download all files created to the folder created using *push.py* and after making sure pull.py is in this folder type

```shell
python3 pull.py filename.inp 1 10 5
```
 1. *filename.inp* is your original inputfile.
 2. *1* is the first number you will start with.
 3. *10* is the final number on the input file.
 4. *5* is the number of cycles you ran.
This should change all the filenames back to the logic flair uses.
You should now be able to open *filename.inp* using flair and all data should be present.

### Limitations
*push.py* can only generate inputfiles for 676 parallel jobs (but it is rather unlikely you have that many CPUs available anyway).
*pull.py* can only convert files back for 676 parallel jobs and only if the number of cycles wasn't higher than nine
```shell
 $FLUPRO/flutil/rfluka -N0 -MX inputfile
````
*X* is the number of cycles.

This script starts counting from 1. Not from 0. If you ask it to start at 0 it will crash.

### Dependencies
*push.py* requires the following programs to be installed:
 1. python3
 2. GNU sed
 3. The python packages system and os

*pull.py* requires the following programs to be installed:
 1. python3
 2. rename
    ```shell
    sudo apt install rename
    ```
 3. The python packages system and os

With the exception of *rename* all of these should come preinstalled on Ubuntu 18.04, 20.04 and many more distributions.
If you are not using a Ubuntu you probably know how to install this yourself.

### How do I get these scripts without copy pasting?
Easiest way is just to use git. Open the terminal and type
```shell
git clone https://github.com/kaasknak/fluka_cluster.git
```
And you should find everything in the folder called *fluka_cluster*
