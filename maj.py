import sys
import subprocess

def Telechargement_MAJ():

	print "WORLD"
	proc = subprocess.Popen(["sudo rm -rf Programmes"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	Data_Scan = out.splitlines()
	print Data_Scan
	
	proc = subprocess.Popen(["sudo git clone https://github.com/Maxim01/Programmes.git /home/Devismes_Bridge"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	Data_Scan = out.splitlines()
	print Data_Scan

def main():
	
	print("MAIN")
	print "SYS_VER:", (sys.version)
	
	Telechargement_MAJ()
  
if __name__ == "__main__":
    main()
 
