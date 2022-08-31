`default_nettype none
`timescale 1ns/1ps
module sampleClockGen #(parameter CLK_DIV = 2,  CLK_TOTAL=127)(
            input CLOCK, RESET,
            output [6:0] COUNT,
            output SAMP, SHIFT
            );

    reg sample, shift;
    reg [6:0] pulseCount;

    assign COUNT = pulseCount;
    assign SAMP  = sample;
    assign SHIFT = shift;


    always @(posedge CLOCK)
        begin
            if(RESET)
            begin
                pulseCount <= 0;
                sample     <=  0;
                shift      <=  0;
            end
            else
            begin
                if(pulseCount == CLK_TOTAL-1)
                begin
                    pulseCount <= 0;
                    sample     <=  1;
                    shift      <=  0;   //consider leaving shift 0 when new samples are taken
                end
                else
                begin
                    pulseCount <= pulseCount + 1'b1;
                    sample     <=  0;
                    shift      <=  1;
                end
            end
        end

endmodule



