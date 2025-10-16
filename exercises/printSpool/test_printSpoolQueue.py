import pytest
from printSpool import PrintSpoolerList,PrintSpoolerQueue
from printSpool import simulate



@pytest.mark.parametrize ('cmds,expected', [
    (['SEND test', 'NEXT', 'PRINT'], ['Next is test','Printing test']),
    (['SEND test', 'NEXT', 'NEXT','PRINT'], ['Next is test','Next is test','Printing test']),
    ([], []),
    (['PRINT'], ['No documents waiting']),
    (['NEXT'],['Queue empty']),
    (['SEND test2'], [])

])
def test_simple(cmds, expected):
    assert simulate(cmds) == expected

@pytest.mark.parametrize ('cmds,expected', [
    (['SEND test1', 'NEXT', 'PRINT','NEXT','PRINT'], ['Next is test1','Printing test1','Queue empty','No documents waiting']),
    (['NEXT', 'NEXT','PRINT', 'SEND test1'], ['Queue empty','Queue empty','No documents waiting']),
    (['SEND test1', 'SEND test2', 'SEND test3', 'NEXT', 'SEND test4', 'PRINT', 'SEND test5', 'NEXT', 'PRINT', 'PRINT'], ['Next is test1', 'Printing test1', 'Next is test2','Printing test2','Printing test3']),
    (['SEND test1', 'NEXT', 'SEND test2', 'NEXT','PRINT','SEND test3', 'NEXT', 'SEND test4', 'NEXT','PRINT', 'PRINT','PRINT','PRINT'], ['Next is test1', 'Next is test1', 'Printing test1','Next is test2','Next is test2','Printing test2','Printing test3','Printing test4','No documents waiting'])

])
def test_longer(cmds, expected):
    assert simulate(cmds) == expected



#AI generated tests below


class TestPrinterSpooler:
    def test_add_and_len(self):
        spooler = PrintSpoolerList()
        assert len(spooler) == 0
        spooler.add_document("doc1")
        spooler.add_document("doc2")
        assert len(spooler) == 2

    def test_peek_does_not_remove(self):
        spooler = PrintSpoolerList()
        spooler.add_document("doc1")
        spooler.add_document("doc2")
        assert spooler.peek() == "doc1"
        assert len(spooler) == 2

    def test_print_next_removes(self):
        spooler = PrintSpoolerList()
        spooler.add_document("doc1")
        spooler.add_document("doc2")
        assert spooler.print_next() == "doc1"
        assert len(spooler) == 1
        assert spooler.print_next() == "doc2"
        assert len(spooler) == 0
        assert spooler.print_next() is None

    def test_peek_on_empty(self):
        spooler = PrintSpoolerList()
        assert spooler.peek() is None


class TestSimulate:
    def test_basic_flow(self):
        commands = [
            "SEND a",
            "SEND b",
            "NEXT",
            "PRINT",
            "NEXT",
            "PRINT",
            "PRINT",
        ]
        output = simulate(commands)
        assert output == [
            "Next is a",
            "Printing a",
            "Next is b",
            "Printing b",
            "No documents waiting",
        ]

    def test_empty_queue_behavior(self):
        commands = ["NEXT", "PRINT"]
        output = simulate(commands)
        assert output == ["Queue empty", "No documents waiting"]

    def test_invalid_command(self):
        commands = ["SEND good", "BOGUS", "SEND fine"]
        output = simulate(commands)
        # Should reject invalid and keep processing
        assert output == [
            "Invalid command: BOGUS",
        ]

    def test_mixed_long_sequence(self):
        commands = [
            "SEND alpha",
            "SEND beta",
            "NEXT",
            "SEND gamma",
            "PRINT",
            "PRINT",
            "NEXT",
            "PRINT",
            "PRINT",  # extra to test empty
        ]
        output = simulate(commands)
        assert output == [
            "Next is alpha",
            "Printing alpha",
            "Printing beta",
            "Next is gamma",
            "Printing gamma",
            "No documents waiting",
        ]

    def test_case_sensitivity(self):
        # Optional: depending on how strict you want
        commands = ["send test"]
        output = simulate(commands)
        assert output == ["Invalid command: send test"]
    
    def test_long_sequence(self):
        # Build 100 SEND commands
        send_cmds = [f"SEND doc{i}" for i in range(100)]
        # Interleave PRINT commands for first 50
        commands = []
        for i in range(50):
            commands.append(send_cmds[i])
            commands.append("PRINT")
        # Add the rest without printing yet
        commands.extend(send_cmds[50:])
        # Peek at the next item, then drain them all
        commands.append("NEXT")
        commands.extend(["PRINT"] * 60)  # 50 left + 10 extra empties

        output = simulate(commands)

        # First 50 should print immediately
        expected_first_50 = [f"Printing doc{i}" for i in range(50)]
        # Next command after loading doc50–doc99 is NEXT
        expected_next = ["Next is doc50"]
        # Then 50 prints
        expected_prints = [f"Printing doc{i}" for i in range(50, 100)]
        # Final 10 "No documents waiting"
        expected_tail = ["No documents waiting"] * 10

        expected_output = expected_first_50 + expected_next + expected_prints + expected_tail

        assert output == expected_output

    def test_very_long_sequence(self):
        # Build 1000 SEND commands
        send_cmds = [f"SEND doc{i}" for i in range(10000)]
        # Interleave PRINT commands for first 500
        commands = []
        for i in range(5000):
            commands.append(send_cmds[i])
            commands.append("PRINT")
        # Add the rest without printing yet
        commands.extend(send_cmds[5000:])
        # Peek at the next item, then drain them all
        commands.append("NEXT")
        commands.extend(["PRINT"] * 5010)  # 50 left + 10 extra empties

        output = simulate(commands)

        # First 50 should print immediately
        expected_first_50 = [f"Printing doc{i}" for i in range(5000)]
        # Next command after loading doc50–doc99 is NEXT
        expected_next = ["Next is doc5000"]
        # Then 50 prints
        expected_prints = [f"Printing doc{i}" for i in range(5000, 10000)]
        # Final 10 "No documents waiting"
        expected_tail = ["No documents waiting"] * 10

        expected_output = expected_first_50 + expected_next + expected_prints + expected_tail

        assert output == expected_output


if __name__ == "__main__":
    pytest.main([__file__])

