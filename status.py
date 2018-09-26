# Mainframe library
import jclftp

import os
import binascii
def job_run(dunsnumber):        
			   # Non Ascii
			   #Myzftp = jclftp.Zftp('159.137.156.61','PFMTT','MAY018',timeout=500.0,sbdataconn='(ibm-1147,iso8859-1)')
			   # Ascii format
			   Myzftp = jclftp.Zftp('159.137.156.61','BPOPU','NOV2018',timeout=500.0,sbdataconn='(IBM-1047,ISO8859-1)')
		       # easy job for zos:			   
			   print (dunsnumber)
			   print (type(dunsnumber))
			   #if os.path.isfile("duns.txt"):
				#   os.remove("duns.txt")
    
			   #file = open('duns.txt','w')
			   #file.write(dunsnumber)
			   #file.close() 
			   # UPLOAD ASCII FORMAT TEXT	
			   # Myzftp.upload_text('duns.txt', 'BPO.DAT.PU.GDMI.INPUT', sitecmd='')

			   # Print Status of jobs
			   for row in Myzftp.list_jes_spool(jobmask='', owner='', status='ALL'):
				   print(row)
      		     
				 
			   # Get PDS Menbers 
			   for member in Myzftp.get_pds_directory('BPO.CIS.PU.EXTRA.JOBS', attrs=False, samples=None):
			       print(member)      		     			   


			   exit()
			   job = Myzftp.submit_wait_job("",jfile="gdmi3900.jcl",purge=False) #True or False	
			   print ("rc1:"+ job["rc"])
			   if os.path.isfile("Output.txt"):
				   os.remove("Output.txt")			   
			   Myzftp.download_text('PFM.DAT.TT.TEST', 'Output.txt')
			   with open('Output.txt') as f:
				   first_line = f.readline()
				   #print(first_line)
				   return first_line

job_run('1234567@1')				   