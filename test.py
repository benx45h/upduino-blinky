from nmigen import *
from nmigen.back.pysim import *

class TestModule( Elaboratable ):
    def __init__( self ):
        self.count = Signal( 16, reset = 0)
        self.ncount = Signal( 16, reset = 0)
    def elaborate (self, platform):
        m = Module()
        m.d.comb += self.ncount.eq( ~self.count )
        m.d.sync += self.count.eq( self.count + 1 ) 
        with m.If( self.count == 42 ):
            m.d.sync += self.count.eq( 0 )
        return m

if __name__ == "__main__":
    dut = TestModule()
    sim = Simulator(dut)
    with sim.write_vcd("test.vcd", "dump.gtkw"):
        def proc():
            for i in range(50):
                yield Tick()
        sim.add_clock(1e-6)
        sim.add_sync_process( proc )
        sim.run()
