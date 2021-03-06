""" intent
Facade is a structural design pattern that provides a simplified interface
to a library, a framework, or any other complex set of classes.
"""


class CPU:
    """Complex system parts"""

    def __init__(self):
        pass

    def freeze(self):
        pass

    def jump(self):
        pass

    def execute(self):
        pass


class Memory:
    def __init__(self):
        # ...
        pass

    def load(self, position, data):
        # ...
        pass


class HardDrive:
    def __init__(self):
        # ...
        pass

    def read(self, lba, size):
        # ...
        pass


# Facade
class Computer:
    BOOT_ADDRESS = "some address"
    BOOT_SECTOR = "boot sector"
    SECTOR_SIZE = 1

    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hard_drive = HardDrive()

    def start_computer(self):
        self._cpu.freeze()
        self._memory.load(
            self.BOOT_ADDRESS, self._hard_drive.read(self.BOOT_SECTOR, self.SECTOR_SIZE)
        )
        self._cpu.jump()
        self._cpu.execute()


if __name__ == "__main__":
    facade = Computer()
    facade.start_computer()
