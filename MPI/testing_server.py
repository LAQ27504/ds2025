from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()

def log(msg, *args):
    if rank == 0:
        print (msg % args)

log('')

info = MPI.INFO_NULL

port = MPI.Open_port(info)
log("opened port: '%s'", port)

service = 'pyeval'
MPI.Publish_name(service, port, info)
log("published service: '%s'", service)

root = 0
log('waiting for client connection...')
comm = MPI.COMM_WORLD.Accept(port, info, root)
log('client connected...')