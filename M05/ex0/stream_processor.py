from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        total = sum(data)
        count = len(data)
        if count:
            avg = total / count
        else:
            avg = 0
        result = f"Processed {count} numeric values, sum={total}, avg={avg}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, list)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        char_count = len(data)
        word_count = len(data.split())

        result = f"Processed text: {char_count} characters, {word_count} words"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        if data.startswith("ERROR:"):
            level = "ERROR"
            message = data[len("ERROR:"):].strip()
            result = f"[ALERT] {level} level detected: {message}"
        else:
            result = f"Log entry: {data}"
        return self.format_output(result)

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    inputs = [numeric_data, text_data, log_data]
    for processor, data in zip(processors, inputs):
        print(f"Initializing {processor.__class__.__name__}...")
        print(f"Processing data: {data}")
        try:
            status = "Verified" if processor.validate(data) else "Failed"
            print(f"Validation: {status}")
            output = processor.process(data)
            print(output)
        except ValueError as e:
            print(f"Error: {e}")
        print()

    print("=== Polymorphic Processing Demo ===")
    for processor in processors:
        data = (
            numeric_data
            if isinstance(processor, NumericProcessor)
            else text_data
            if isinstance(processor, TextProcessor)
            else log_data
        )
        print(processor.process(data))
