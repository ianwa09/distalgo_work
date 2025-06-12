import sys
from da import DistProcess

class P(DistProcess):
    def setup(self, s, nrequests):
        self.s = s
        self.nrequests = nrequests

    def run(self):
        for i in range(self.nrequests):
            self.output(f'Process {self} in critical section')
        
        self.output(f'Process {self} terminating')

class Main(DistProcess):
    def __init__(self, nprocs, nrequests):
        super().__init__()
        self.nprocs = nprocs
        self.nrequests = nrequests
    
    def run(self):
        # Create child processes using self.new()
        ps = self.new(P, num=self.nprocs)
        
        # Setup each process
        for p in ps:
            others = ps - {p}
            p.setup(others, self.nrequests)
        
        # Start all processes
        for p in ps:
            p.start()
        
        # Wait for completion
        for p in ps:
            p.join()

def main():
    nprocs = int(sys.argv[1] if len(sys.argv) > 1 else 3)
    nrequests = int(sys.argv[2] if len(sys.argv) > 2 else 1)

    # Skip global_init for now and try to create processes directly
    try:
        main_proc = Main(nprocs, nrequests)
        main_proc.start()
        main_proc.join()
    except Exception as e:
        print(f"Error: {e}")
        print("Let's try a different approach...")

if __name__ == '__main__':
    main()