from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()

def log(msg, *args):
    if rank == 0:
        print (msg % args)

info = MPI.INFO_NULL
service = "pyeval"
log("looking-up service '%s'", service)
port = MPI.Lookup_name(service)
log("service located  at port '%s'", port)

root = 0
log('waiting for server connection...')
comm = MPI.COMM_WORLD.Connect(port, info, root)
log('server connected...')