`default_nettype none
`timescale 1ns/1ps
module mbsFSK (
    input clk,    // 16MHz clock
    input reset,     //reset
    output READY,
    output SHIFT,
    output [4:0] LFSR,
    output [6:0] COUNT,
    output GPIO2,    //OUT2
    output GPIO1     //OUT1
);

    reg reset_d, reset_sync;
    wire outReal, outImag, ready, shift;
    wire [4:0] dataOut;
    wire [6:0] count;

    assign READY = ready;
    assign SHIFT = shift;
    assign LFSR  = dataOut;
    assign COUNT = count;
    assign GPIO2 = outReal;
    assign GPIO1 = outImag;

    //synchronize external reset
    always @(posedge clk)
    begin
        reset_d      <= reset;
        reset_sync   <= reset_d;
    end

    //MODULE INSTANTIATION
    sampleClockGen #(.CLK_DIV(1),  .CLK_TOTAL(128)) sampClockBlock (
        .CLOCK(clk),
        .RESET(reset_sync),
        .COUNT(count),
        .SAMP(ready),
        .SHIFT(shift));

    SymbLUT symbolLUT (
        .CLOCK(clk),
        .RESET(reset_sync),
        .READY(ready),
        .SHIFT(shift),
        .ADDRESS(dataOut),
        .DOUTREAL(outReal),
        .DOUTIMAG(outImag));

    LFSRmod prnGen (
        .CLOCK(clk),
        .RESET(reset_sync),
        .ENABLE(ready),
        .OUTDATA(dataOut));

endmodule

