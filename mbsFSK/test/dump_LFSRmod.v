module dump();
    initial begin
        $dumpfile ("LFSRmod.vcd");
        $dumpvars (0, LFSRmod);
        #1;
    end
endmodule

