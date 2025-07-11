class P(process):
    def setup(s:set, nrequests:int): pass # s is set of all other processes

    def mutex(task):
        -- request
        c = logical_clock()
        send(('request', c, self), to= s)
        await(each(received(('request', c2, p)),
                   has= received(('release', c2, p)) or (c, self) < (c2, p))
                and each(p in s, has= some(receiv(('ack', c2, _p)), has= c2 > c)))
        -- critical_selection
        task()
        -- release
        send(('release', c, self), to= s)

    def receive(msg= ('request', _, p)):
        send(('ack', logical_clock(), self), to= p)
    
    def run():
        def task(): output('in critical section')
        for i in range(nrequests): mutex(task)

        send(('done', self), to= s)
        await(each(p in s, has= received(('done', p))))
        output('terminating')

def main(): 
    nprocs = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    nrequests = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    config(channel= Fifo, clock= Lamport)

    ps = new(P, num= nprocs)
    for p in ps: setup(p, (ps-{p}, nrequests))
    start(ps)