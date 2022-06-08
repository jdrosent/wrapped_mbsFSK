
`timescale 1ns/1ps
module top_tb ();
  initial begin
    $dumpfile("top_tb.vcd");
    $dumpvars;
  end

  reg clk;
  reg SW1, SW2;
  wire led0,led1,led2,led3,sdat,d0,sclk,spidatardy,sclk2,d1,sdat2,gpio2,gpio1, usbpu,dOut,ready;
  integer f,i;

  initial begin
		clk = 1'b0;
	end

  always begin
    #40 clk = ~clk;
  end

  initial begin
    f = $fopen("GPIOoutput.csv","w");
    // f = $fopen("LFSRoutput.txt","w");
    SW1 <= 1'b1; SW2 <= 1'b1;
    repeat(20) @(posedge clk);
    SW1 <= 1'b0; SW2 <= 1'b0;

    for (i = 0; i<100000; i=i+1) begin
      @(posedge clk);
      // $display("Ready %b, Shift %b, GPIO2 %b, GPIO1 %b", led0, led1, gpio2, gpio1);
      // $fwrite(f,"%b, %b, %b, %b\n", led0, led1, led2, led3); //led2 = outReal, led3 = outImag
      if(ready)
      begin
        $fwrite(f,"%b, %b, %b, %b, %b\n", led0, led1, led2, led3, dOut);
      end
    end

    $fclose(f);
    // repeat(1000000) @(posedge clk);
    $finish;
  end

  mbsFSK dut (.CLK(clk),
         // .PIN_23(SW1),
         .PIN_24(SW2),
         // .PIN_1(led0),
         // .PIN_2(led1),
         // .PIN_3(led2),
         // .PIN_4(led3),
         // .PIN_10(sdat),
         // .PIN_11(d0),
         // .PIN_12(sclk),
         // // .PIN_13(dOut),
         // .PIN_14(spidatardy),
         // .PIN_15(sclk2),
         // .PIN_16(d1),
         // .PIN_17(sdat2),
         .PIN_18(gpio2),
         .PIN_19(gpio1));
         // // .PIN_20(ready),
         // .USBPU(usbpu));

endmodule // tb

