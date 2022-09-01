import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout

@cocotb.test()
async def test_all(dut):
    clock = Clock(dut.clk, 25, units="ns") # 40M
    cocotb.fork(clock.start())
    
    dut.RSTB <= 0
    dut.power1 <= 0;
    dut.power2 <= 0;
    dut.power3 <= 0;
    dut.power4 <= 0;

    await ClockCycles(dut.clk, 8)
    dut.power1 <= 1;
    await ClockCycles(dut.clk, 8)
    dut.power2 <= 1;
    await ClockCycles(dut.clk, 8)
    dut.power3 <= 1;
    await ClockCycles(dut.clk, 8)
    dut.power4 <= 1;

    await ClockCycles(dut.clk, 80)
    dut.RSTB <= 1

	#wait with_timeout(RisingEdge(dut.uut.mprj.wrapped_mbsFSK.SHIFT), 500, 'us')
    await with_timeout(RisingEdge(dut.FWRDY), 650, 'us')
    print("firmware ready")

    # wait for SAMPLE signal to go high
    await RisingEdge(dut.READY)
    #assert that pulseCount rolls over
    assert(dut.COUNT==0)
    await RisingEdge(dut.clk)

    # assert that SHIFT and SAMP are of opposite polarity
    assert(dut.SHIFT != dut.READY)

    # wait for several more clocks
    await ClockCycles(dut.clk, 10)
    #assert that pulseCount continues counting
    assert(dut.COUNT==10)


    # wait
#    await ClockCycles(dut.clk, 6000)

    # assert something
 #   assert(0 == 25)

