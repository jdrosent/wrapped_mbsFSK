import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles
import random

async def reset(dut):
    dut.reset <= 1

    await ClockCycles(dut.clk, 50)
    dut.reset <= 0;

@cocotb.test()
async def test_mbsFSK(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())
    await reset(dut)
	
    # wait for READY signal to go high
    await RisingEdge(dut.READY)
    #assert that pulseCount rolls over
    assert(dut.COUNT==0)
    await RisingEdge(dut.clk)
 
    # assert that SHIFT and READY are of opposite polarity
    assert(dut.SHIFT != dut.READY)

	# wait for several more clocks
    await ClockCycles(dut.clk, 10)
     #assert that pulseCount continues counting
    assert(dut.COUNT==10)



