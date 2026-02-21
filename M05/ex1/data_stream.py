from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count
        }

class SensorStream(DataProcessor):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures = [
                float(item.split(":")[1])
                for item in data_batch
                if item.startswith("temp:") and isinstance(item, str)
            ]

            self.processed_count += len(data_batch)

            avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0
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
