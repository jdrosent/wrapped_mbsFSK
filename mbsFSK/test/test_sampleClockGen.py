import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles

async def reset(dut):
    dut.RESET<= 1
    await ClockCycles(dut.CLOCK, 50)
    dut.RESET<= 0;
    await ClockCycles(dut.CLOCK, 50)


@cocotb.test()
async def test_mbsFSK(dut):
    clock = Clock(dut.CLOCK, 10, units="ns")
    cocotb.fork(clock.start())
    await reset(dut)
        # wait pwm level clock steps
      #  await ClockCycles(dut.clk, i)

        # assert still high
      #  assert(dut.out)

    # wait for SAMPLE signal to go high
    await RisingEdge(dut.SAMP)
	#assert that pulseCount rolls over
    assert(dut.pulseCount==0)
    await RisingEdge(dut.CLOCK)
    
	# assert that SHIFT and SAMP are of opposite polarity
    assert(dut.SHIFT != dut.SAMP)
	
	# wait for several more clocks
    await ClockCycles(dut.CLOCK, 10)
	#assert that pulseCount continues counting
    assert(dut.pulseCount==10)
