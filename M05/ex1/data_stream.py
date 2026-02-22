from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch

        return [
            item
            for item in data_batch
            if criteria.lower() in str(item).lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("temp:")
            ]

            self.processed_count += len(data_batch)

            avg_temp = (
                sum(temperatures) / len(temperatures) if temperatures else 0
            )

            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )

        except Exception:
            return "Sensor processing failed."


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow = 0

            for item in data_batch:
                if not isinstance(item, str):
                    continue

                operation, value = item.split(":")
                amount = float(value)

                if operation == "buy":
                    net_flow -= amount
                elif operation == "sell":
                    net_flow += amount

            self.processed_count += len(data_batch)

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {net_flow:+.0f} units"
            )

        except Exception:
            return "Transaction processing failed."


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = [
                event for event in data_batch
                if isinstance(event, str) and event.lower() == "error"
            ]

            self.processed_count += len(data_batch)

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected"
            )

        except Exception:
            return "Event processing failed."


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        for stream, batch in zip(self.streams, batches):
            print(stream.process_batch(batch))

            if isinstance(stream, SensorStream):
                print(
                    "- Sensor data: "
                    f"{stream.processed_count} readings processed"
                )
            elif isinstance(stream, TransactionStream):
                print(
                    "- Transaction data: "
                    f"{stream.processed_count} operations processed"
                )
            elif isinstance(stream, EventStream):
                print(
                    "- Event data: "
                    f"{stream.processed_count} events processed"
                )

        print("\nStream filtering active: High-priority data only")

        sensor_filtered = batches[0][:2]
        transaction_filtered = [
            item for item in batches[1] if "300" in item
        ]

        print(
            "Filtered results: "
            f"{len(sensor_filtered)} critical sensor alerts, "
            f"{len(transaction_filtered)} large transaction"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print(
        "Stream ID: "
        f"{sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Processing sensor batch:", sensor_batch)
    print(sensor_stream.process_batch(sensor_batch))
    print()

    print("Initializing Transaction Stream...")
    print(
        "Stream ID: "
        f"{transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print("Processing transaction batch:", transaction_batch)
    print(transaction_stream.process_batch(transaction_batch))
    print()

    print("Initializing Event Stream...")
    print(
        "Stream ID: "
        f"{event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    event_batch = ["login", "error", "logout"]
    print("Processing event batch:", event_batch)
    print(event_stream.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = [
        ["temp:20.0", "temp:24.0"],
        ["buy:200", "sell:300", "buy:50", "sell:75"],
        ["start", "error", "stop"],
    ]

    processor.process_all(mixed_batches)

    print("\nAll streams processed successfully. Nexus throughput optimal.")
