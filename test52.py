class ExtendedBrainfuckInterpreter:
    def __init__(self):
        self.memory = [0] * 30000  # Brainfuck memory tape with 30,000 cells
        self.pointer = 0  # Memory pointer
        self.input_buffer = []  # Input buffer for user input
        self.output_buffer = []  # Output buffer for program output
        self.log_enabled = True

    def execute(self, code_file):
        with open(code_file, 'r') as f:
            code = self.clean_code(f.read())
        
        code_pointer = 0

        while code_pointer < len(code):
            instruction = code[code_pointer]

            if instruction == '@':
                break
            elif instruction == '$':
                self.overwrite_memory_with_storage()
            elif instruction == '!':
                self.overwrite_storage_with_memory()
            elif instruction == '}':
                self.single_right_logical_shift()
            elif instruction == '{':
                self.single_left_logical_shift()
            elif instruction == '~':
                self.bitwise_not()
            elif instruction == '^':
                self.bitwise_xor()
            elif instruction == '&':
                self.bitwise_and()
            elif instruction == '|':
                self.bitwise_or()
            elif instruction == '+':
                self.increment_memory()
            elif instruction == '-':
                self.decrement_memory()
            elif instruction == '>':
                self.increment_pointer()
            elif instruction == '<':
                self.decrement_pointer()
            elif instruction == '.':
                self.output_buffer.append(chr(self.memory[self.pointer]))
            elif instruction == ',':
                if not self.input_buffer:
                    user_input = input("Enter a single character: ")
                    self.input_buffer.extend(user_input)
                self.memory[self.pointer] = ord(self.input_buffer.pop(0))
            elif instruction == '[':
                if self.memory[self.pointer] == 0:
                    loop_depth = 1
                    while loop_depth > 0:
                        code_pointer += 1
                        if code[code_pointer] == '[':
                            loop_depth += 1
                        elif code[code_pointer] == ']':
                            loop_depth -= 1
                else:
                    pass  # Move to the next instruction
            elif instruction == ']':
                if self.memory[self.pointer] != 0:
                    loop_depth = 1
                    while loop_depth > 0:
                        code_pointer -= 1
                        if code[code_pointer] == ']':
                            loop_depth += 1
                        elif code[code_pointer] == '[':
                            loop_depth -= 1
                else:
                    pass  # Move to the next instruction

            if self.log_enabled:
                self.log_state(code, code_pointer)

            code_pointer += 1

        return "".join(self.output_buffer)

    def overwrite_memory_with_storage(self):
        self.memory[self.pointer] = self.memory[-1]

    def overwrite_storage_with_memory(self):
        self.memory[-1] = self.memory[self.pointer]

    def single_right_logical_shift(self):
        self.memory[self.pointer] = (self.memory[self.pointer] >> 1) & 0xFF

    def single_left_logical_shift(self):
        self.memory[self.pointer] = (self.memory[self.pointer] << 1) & 0xFF

    def bitwise_not(self):
        self.memory[self.pointer] = (~self.memory[self.pointer]) & 0xFF

    def bitwise_xor(self):
        self.memory[self.pointer] = (self.memory[self.pointer] ^ self.memory[-1]) & 0xFF

    def bitwise_and(self):
        self.memory[self.pointer] = (self.memory[self.pointer] & self.memory[-1]) & 0xFF

    def bitwise_or(self):
        self.memory[self.pointer] = (self.memory[self.pointer] | self.memory[-1]) & 0xFF

    def increment_memory(self):
        self.memory[self.pointer] = (self.memory[self.pointer] + 1) & 0xFF

    def decrement_memory(self):
        self.memory[self.pointer] = (self.memory[self.pointer] - 1) & 0xFF

    def increment_pointer(self):
        self.pointer = (self.pointer + 1) % len(self.memory)

    def decrement_pointer(self):
        self.pointer = (self.pointer - 1) % len(self.memory)

    def clean_code(self, code):
        # Remove any characters that are not valid Brainfuck instructions
        valid_chars = "@$!}{~^&|+-><.,[]"
        return "".join(c for c in code if c in valid_chars)

    def log_state(self, code, code_pointer):
        start = max(0, code_pointer - 5)
        end = min(len(code), code_pointer + 6)
        code_slice = code[start:end]
        current_instruction = code_slice[5]
        log_message = (
            f"here ({current_instruction}) {''.join(code_slice[:5])}^{''.join(code_slice[6:])} "
            f"Memory: {self.memory[:10]} "
            f"Pointer: {self.pointer} "
            f"Output: {''.join(self.output_buffer)}"
        )
        print(log_message)

if __name__ == "__main__":
    interpreter = ExtendedBrainfuckInterpreter()
    code_file = input("Enter the path to the Brainfuck code file: ")
    result = interpreter.execute(code_file)
    print("\nOutput:")
    print(result)
