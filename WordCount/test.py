from mpi4py import MPI 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 


data = 0
if rank == 0:
   comm.bcast("abc", root=0) 
else: 
   print(comm.bcast("", root=0))
