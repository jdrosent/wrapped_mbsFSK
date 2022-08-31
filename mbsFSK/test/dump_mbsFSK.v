module dump();
    initial begin
        $dumpfile ("mbsFSK.vcd");
        $dumpvars (0, mbsFSK);
        #1;
    end
endmodule

