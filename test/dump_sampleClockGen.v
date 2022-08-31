module dump();
    initial begin
        $dumpfile ("sampleClockGen.vcd");
        $dumpvars (0, sampleClockGen);
        #1;
    end
endmodule

