import glob
import subprocess


# create lines of code with necessary imports
def write_imports(filename):
    with open(filename, "w") as f:
        f.write("""# -*- coding: cp1251 -*-
import time
import math
import numpy
from math import log
from mne.time_frequency import psd_multitaper
import numpy as np
import matplotlib.pyplot as plt
import mne
import math
import os
import sys
import csv
from mod import *
""")


# create line of code like "out_var1, out_var2 = function(arg1, arg2, arg3)"
def write_op(filename, input_var_names, output_var_names, function_to_call):
    with open(filename, "a") as f:

        for out_var in output_var_names:
            if out_var == output_var_names[len(output_var_names) - 1]:
                args = ""
                for in_var in input_var_names:
                    if in_var == input_var_names[len(input_var_names) - 1]:
                        args += in_var
                    else:
                        args += in_var + ", "
                f.write(out_var + " = " + function_to_call + "(" + args + ")\n")
            else:
                f.write(out_var + ", ")


# create line of code like "input_var = "value"" or "input_var = ["val1", "val2", "val3"]"
def write_var(filename, var, value):
    with open(filename, "a") as f:
        if isinstance(value, list):
            value_str = ""
            for elem in value:
                if elem == value[0]:
                    value_str += "[\"" + elem + "\", "
                elif elem == value[len(value) - 1]:
                    value_str += "\"" + elem + "\"]\n"
                else:
                    value_str += "\"" + elem + "\", "
            f.write(var + " = " + value_str)
        elif isinstance(value, str):
            f.write(var + " = \"" + value + "\"\n")


# combine imports and lines of code in one file
def copy_file_content(filename, filename_final):
    with open(filename_final, "a") as fFinal, open(filename, "r") as f:
        for line in f:
            fFinal.write(line)


def clean_file(filename):
    with open(filename, "w") as f:
        f.write("")


# create .sh script which will be used to submit job on hpc
def write_sh_script():
    python_run_line = "python full_proc_eeg.py"
    sh_script = "#!/bin/bash\n#SBATCH --nodes=1\n#SBATCH --threads-per-core=1\n#SBATCH --time=0-10\n#SBATCH --job-name=aka\n#SBATCH -p knl-alone\n#SBATCH --ntasks-per-node=1\nsource ../../env/bin/activate\n" + python_run_line + "\ndeactivate\n"
    f = open("api/hpc_scripts/run.sh", "w")
    f.write(sh_script)
    f.close()


def do_remote_bash_cmd(bash_cmd):
    process = subprocess.Popen(bash_cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')


# check if submitted job on hpc is still running
def job_is_alive(job_id):
    output = do_remote_bash_cmd(
        "ssh gorodnichev_m_a@nks-1p.sscc.ru -i /Users/someo/.ssh/id_rsa \"squeue --jobs " + job_id + " --users gorodnichev_m_a\"")
    if job_id in output:
        print("Service: JOB IS ALIVE")
        return True
    else:
        print("Service: JOB IS NOT ALIVE")
        return False


def image_is_in_service_context(image_path):
    for file_name in glob.glob("api/hpc_scripts/*.png"):
        if image_path in file_name:
            return True
    return False