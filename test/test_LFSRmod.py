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
    # set ENABLE to 0
    dut.ENABLE <= 0
    await reset(dut)

	# check that output is all 0's
    assert(dut.OUTDATA == 0)
    
	# wait 10 clock cycles, raise ENABLE
    await ClockCycles(dut.CLOCK,10)
    dut.ENABLE <= 1
    await ClockCycles(dut.CLOCK,1)
	
	# assert that internal reg value is 0
    assert(dut.value == 0)

	# set READY signal
    #dut.READY <= 1
    #await ClockCycles(dut.CLOCK,2)
	
	# assert that internal address updated
    #assert(dut.dataADDR_d == 1)

    # extra clock cycles for GTKWave viewing
    await ClockCycles(dut.CLOCK,20)
