`default_nettype none
`timescale 1ns/1ps
module LFSRmod (CLOCK, RESET, ENABLE, OUTDATA);
	input wire CLOCK, RESET, ENABLE;
	output reg [4:0] OUTDATA;

	reg value;
	reg [18:0] out;

	always @(*) begin
		value = ~(out[18] ^ out[5] ^ out[1] ^ out[0]);
		OUTDATA = out[18:14];
	end

	always @(posedge CLOCK) begin
		if (RESET) begin
			out <= 19'h1;
		end

		else begin
			if(ENABLE)
			begin
				out[18:0] <= { value , out[18:1] };
			end
		end
	end
endmodule
