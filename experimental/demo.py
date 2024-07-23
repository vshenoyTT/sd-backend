import subprocess

# Define the two scripts to run
script1 = "pytest models/demos/wormhole/stable_diffusion/demo/experimental/jsonSDserver.py"
script2 = "python models/demos/wormhole/stable_diffusion/demo/experimental/flaskserver.py"

# Start both scripts using subprocess.Popen
process1 = subprocess.Popen(script1, shell=True)
process2 = subprocess.Popen(script2, shell=True)

