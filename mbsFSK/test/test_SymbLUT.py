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
    # check that address is 5'b00000
    assert(dut.dataADDR_d == 0)
    dut.ADDRESS <= 1
    await ClockCycles(dut.CLOCK,1)
	# assert that internal address is still 5'b00000
    assert(dut.dataADDR_d == 0)

	# set READY signal
    dut.READY <= 1
    await ClockCycles(dut.CLOCK,2)
	# assert that internal address updated
    assert(dut.dataADDR_d == 1)

    await ClockCycles(dut.CLOCK,10)
    # wait for next rising clk edge
    #await RisingEdge(dut.SAMP)
    #assert(dut.pulseCount==0)
    #await RisingEdge(dut.CLOCK)
        # assert pwm goes low
    #assert(dut.SHIFT != dut.SAMP)
    #assert(dut.pulseCount==0)
    #await ClockCycles(dut.CLOCK, 10)
    #assert(dut.pulseCount==10)
