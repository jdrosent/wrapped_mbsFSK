# FPGA variables
#PROJECT = fpga/mbs_fsk
#SOURCES= src/mbsFSK.v src/sampleClockGen.v src/LFSRmod.v src/SymbLUT.v
#ICEBREAKER_DEVICE = up5k
#ICEBREAKER_PIN_DEF = fpga/icebreaker.pcf
#ICEBREAKER_PACKAGE = sg48
#SEED = 1

# COCOTB variables
export COCOTB_REDUCED_LOG_FMT=1
export PYTHONPATH := test:$(PYTHONPATH)
export LIBPYTHON_LOC=$(shell cocotb-config --libpython)

all: test_mbsFSK test_sampleClockGen test_LFSRmod test_SymbLUT

# if you run rules with NOASSERT=1 it will set PYTHONOPTIMIZE, which turns off assertions in the tests
test_top:
	echo "the top module was renamed to mbsFSK. Please run make test_mbsFSK instead"

test_mbsFSK:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s mbsFSK -s dump -g2012 src/mbsFSK.v test/dump_mbsFSK.v src/ src/sampleClockGen.v src/LFSRmod.v src/SymbLUT.v
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_mbsFSK vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

test_sampleClockGen:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s sampleClockGen -s dump -g2012 test/dump_sampleClockGen.v src/sampleClockGen.v
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_sampleClockGen vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

test_LFSRmod:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s LFSRmod -s dump -g2012 src/LFSRmod.v test/dump_LFSRmod.v
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_LFSRmod vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

test_SymbLUT:
	rm -rf sim_build/
	mkdir sim_build/
	iverilog -o sim_build/sim.vvp -s SymbLUT -s dump -g2012 src/SymbLUT.v test/dump_SymbLUT.v
	PYTHONOPTIMIZE=${NOASSERT} MODULE=test_SymbLUT vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

show_%: %.vcd %.gtkw
	gtkwave $^

# FPGA recipes

show_synth_%: src/%.v
	yosys -p "read_verilog $<; proc; opt; show -colors 2 -width -signed"

%.json: $(SOURCES)
	yosys -l fpga/yosys.log -p 'synth_ice40 -top mbsFSK -json $(PROJECT).json' $(SOURCES)

%.asc: %.json $(ICEBREAKER_PIN_DEF) 
	nextpnr-ice40 -l fpga/nextpnr.log --seed $(SEED) --freq 20 --package $(ICEBREAKER_PACKAGE) --$(ICEBREAKER_DEVICE) --asc $@ --pcf $(ICEBREAKER_PIN_DEF) --json $<

%.bin: %.asc
	icepack $< $@

prog: $(PROJECT).bin
	iceprog $<

# general recipes

lint:
	verible-verilog-lint src/*v --rules_config verible.rules

clean:
	rm -rf *vcd sim_build fpga/*log fpga/*bin test/__pycache__

.PHONY: clean
