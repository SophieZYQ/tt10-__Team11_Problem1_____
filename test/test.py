# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 50

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    max_val = 255  # Maximum sum value allowed
    a_vals = [i for i in range(max_val)]  # ui_in can range from 0 to 255
    b_vals = [j for j in range(max_val)]  # uio_in can also range from 0 to 255

      integer a, b;
        for (a = 0; a < 256; a = a + 1) begin
            for (b = 0; b < 256; b = b + 1) begin
                // Set input values
                ui_in = a;
                uio_in = b;
                #10;
                
                // Calculate expected value with modulo 256 behavior
                reg [7:0] expected_uo_out;
                expected_uo_out = (a + b) % 256;
                
                // Log the output and check the assertion
                $display("Test case ui_in=%d, uio_in=%d -> uo_out=%d", a, b, uo_out);
                
                if (uo_out !== expected_uo_out) begin
                    $display("ERROR: Expected %d, but got %d", expected_uo_out, uo_out);
                end
            end
        end
        $display("Comprehensive loop testing completed.");
    end

endmodule
