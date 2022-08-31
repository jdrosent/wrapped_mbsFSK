module dump();
    initial begin
        $dumpfile ("SymbLUT.vcd");
        $dumpvars (0, SymbLUT);
        #1;
    end
endmodule

