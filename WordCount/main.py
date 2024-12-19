from mpi4py import MPI
def mapping(data_chunks):
   print(data_chunks)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank != 0: 
   filePath = f"text{rank}.txt"

   with open(filePath, "r") as f:
      print(f.read())
