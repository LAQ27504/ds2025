from mpi4py import MPI
import mmh3
 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()

def map(data_chunks):
   text = data_chunks[:-1].split(" ")
   mapping = [(i, 1) for i in text]
   for i in mapping:
      reducer_id = partition(i[0])
      print((i[0],reducer_id))
      
def partition(word):
   return (mmh3.hash(word) % 3) + 1


if rank > 1: 
   filePath = f"text{rank - 1}.txt"

   with open(filePath, "r") as f:
      map(f.read())


